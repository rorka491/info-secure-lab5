from copy import deepcopy
from dataclasses import asdict, is_dataclass
import json
import os
import subprocess
import sys
from tempfile import TemporaryDirectory
import xml.etree.ElementTree as ET

from ..data.repository import DataError, Repository


NOTICE = ("Учебная модель, не для реальной защиты.\n"
          "Не является юридически значимой УКЭП.\n"
          "TLS-модель не совместима с реальным протоколом.")

TITLES = {"classics": "Классические шифры", "analysis": "Криптоанализ",
          "stego": "Стеганография", "hash": "Хеш и AES-GCM", "signature": "Подпись",
          "tls": "Модель TLS", "incidents": "Инциденты", "tests": "Тесты",
          "reports": "Отчёты"}

REPORTS = {"classics": "classical_report.md", "analysis": "cryptoanalysis_report.md",
           "tests": "test_results.txt"}


def render(value):
    if isinstance(value, str):
        return value
    return json.dumps(value, default=asdict, ensure_ascii=False, indent=2)


def errors_in(value):
    if is_dataclass(value):
        return value.status == "error"
    if isinstance(value, dict):
        return value.get("status") == "error" or any(errors_in(item) for item in value.values())
    return isinstance(value, list) and any(errors_in(item) for item in value)


def classic_table(rows):
    def cell(value):
        return str(value).replace("|", "\\|").replace("\n", "<br>")

    header = ["| Набор | Алгоритм | Открытый текст | Параметры | Шифротекст | Восстановление | Проверка |",
              "| --- | --- | --- | --- | --- | --- | --- |"]
    for row in rows:
        result = row["encrypted"]
        values = (row["id"], row["name"], result.source_message, result.key_or_params,
                  result.result or result.explanation, row.get("recovered", ""), row["status"])
        header.append("| " + " | ".join(map(cell, values)) + " |")
    return "\n".join(header)


def structured_section(command, value):
    if command == "classics":
        return classic_table(value)
    if command == "analysis":
        blocks = []
        for experiment in value[:-1]:
            blocks.append(f"### {experiment['id']} · {experiment['characters']} символов")
            for name, counts in experiment["frequencies"].items():
                if is_dataclass(counts):
                    blocks.append(f"{name} — {counts.explanation}")
                    continue
                ranked = ", ".join(f"{row['letter']} {row['count']} ({row['share']:.1%})"
                                   for row in counts)
                blocks.append(f"- **{name}** — {ranked}")
            candidates = experiment.get("caesar_candidates")
            if isinstance(candidates, list):
                rows = ["| Сдвиг | Расшифровка | Баллы |", "| --- | --- | --- |"]
                for row in candidates:
                    rows.append(f"| {row['shift']} | {row['text']} | {row['score']} |")
                blocks.append("\n".join(rows))
        blocks.append("Пространства ключей для выбранных размеров — " + value[-1].result)
        blocks.append("Цезарь и Атбаш перемещают частоты между буквами. У Виженера "
                      "распределение меняется, но сдвиги повторяются с периодом ключа. "
                      "На коротком тексте выводы особенно зависят от словаря. "
                      "Пространство ключей не учитывает статистические закономерности.")
        return "\n\n".join(blocks)
    if command == "signature":
        body = render(value[:-1])
        kinds = json.loads(value[-1].result)
        table = [
            "| Вид | Механизм | Ключи | Сертификат | Проверка | Признание |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
        for row in kinds:
            table.append("| " + " | ".join(row.values()) + " |")
        return body + "\n\n### Виды электронной подписи\n\n" + "\n".join(table)
    return render(value)


class ReportService:
    def __init__(self, repo, paths, services):
        self.repo = repo
        self.paths = paths
        self.services = services

    def test_results(self):
        with TemporaryDirectory() as directory:
            xml_path = os.path.join(directory, "tests.xml")
            process = subprocess.run(
                [sys.executable, "-m", "pytest", "-q", "-p", "no:cacheprovider",
                 str(self.paths.tests), "--junitxml", xml_path],
                capture_output=True, encoding="utf-8", errors="replace", check=False,
                cwd=self.paths.package.parent,
                env={**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONDONTWRITEBYTECODE": "1"},
            )
            rows = []
            if os.path.exists(xml_path):
                for case in ET.parse(xml_path).iter("testcase"):
                    issue = next(iter(case), None)
                    actual = {"failure": "ошибка", "error": "ошибка", "skipped": "пропущен"}
                    rows.append({"input_expected": case.get("name"),
                                 "actual": "пройден" if issue is None else actual[issue.tag]})
            return {"exit_code": process.returncode, "cases": rows,
                    "pytest": (process.stdout + process.stderr).replace(xml_path, "tests.xml")}

    def defects(self, data, before):
        damaged_params = deepcopy(data)
        damaged_params["algorithm_params"]["classical"]["shift"] = "three"
        rejected = errors_in(self.services["classics"].run(damaged_params))
        with TemporaryDirectory() as directory:
            scratch = type(self.paths.data)(directory)
            for name in data:
                if name != "messages":
                    (scratch / f"{name}.json").write_text(render(data[name]), encoding="utf-8")
            try:
                Repository(scratch).load()
                missing = "Отклонение отсутствует"
            except DataError as error:
                missing = str(error)
        signature = before["signature"]
        return [
            {"defect": "Нецелое значение сдвига", "detected": rejected,
             "after_repair": not errors_in(before["classics"])},
            {"defect": "Изменение подписанного документа", "detected": signature[2].result,
             "after_repair": signature[1].result},
            {"defect": "Отсутствующий входной набор", "detected": missing,
             "after_repair": f"Загружено сообщений: {len(data['messages'])}"},
        ]

    def _write(self, name, title, body):
        self.paths.reports.mkdir(parents=True, exist_ok=True)
        (self.paths.reports / name).write_text(f"# {title}\n\n{NOTICE}\n\n{body}\n", encoding="utf-8")

    def _run(self, command, data):
        if command == "tests":
            return self.test_results()
        if command == "signature":
            self.paths.reports.mkdir(parents=True, exist_ok=True)
            return self.services[command].run(data, self.paths.reports)
        return self.services[command].run(data)

    def execute(self, command):
        try:
            if command == "reports":
                names = sorted(path.name for path in self.paths.reports.glob("*") if path.is_file())
                final = self.paths.reports / "final_report.md"
                content = final.read_text(encoding="utf-8") if final.exists() else "Запустите all."
                return True, f"{self.paths.reports}\n" + "\n".join(names) + "\n\n" + content
            if command == "tests":
                result = self.test_results()
                self._write(REPORTS[command], TITLES[command], render(result))
                return result["exit_code"] == 0, render(result)
            data = self.repo.load()
            if command == "all":
                return self.run_all(data)
            value = self._run(command, data)
            body = structured_section(command, value)
            if command in REPORTS:
                self._write(REPORTS[command], TITLES[command], body)
            return self.passed(command, value), body
        except (ValueError, OSError, KeyError, TypeError, IndexError, AttributeError) as error:
            return False, f"Ошибка сценария: {error}"

    def passed(self, command, value):
        if command == "tests":
            return value["exit_code"] == 0
        if command == "hash":
            return [result.status for result in value] == ["ok", "ok", "error", "ok", "ok", "error"]
        if command == "signature":
            return all(item.status == "ok" for item in (value[0], *value[5:])) and [
                item.result for item in value[1:5]] == [
                "действительна", "документ изменён", "недействительна", "недействительна"]
        return not errors_in(value)

    def check_scenarios(self, settings, output):
        example = next(row for row in output["classics"]
                       if row["id"] == settings["caesar_id"] and row["name"] == "caesar")
        actual = {
            "caesar_round_trip": "original_text" if example.get("match") else "mismatch",
            "aes_modified_packet": output["hash"][-1].status,
            "signature_modified_document": output["signature"][2].result,
        }
        return [{**row, "actual": actual[row["id"]], "ok": actual[row["id"]] == row["expected"]}
                for row in settings["expectations"]]

    def run_all(self, data):
        commands = [*self.services, "tests"]
        output = {command: self._run(command, data) for command in commands}
        defects = self.defects(data, output)
        sections = {command: structured_section(command, value) for command, value in output.items()}
        for command, filename in REPORTS.items():
            self._write(filename, TITLES[command], sections[command])
        self._write("integrity_signature_report.md", "Целостность и подпись",
                    sections["hash"] + "\n\n" + sections["signature"])
        checks = {command: self.passed(command, value) for command, value in output.items()}
        scenarios = self.check_scenarios(data["test_scenarios"], output)
        body = ("## Паспорт\n\nCryptoLab · лабораторная работа № 5. Вымышленные данные. "
                "JSON → репозиторий → сервисы → доменные функции → отчёт. "
                "Dishka связывает зависимости CLI и GUI.\n\n"
                "## Итог по разделам\n\n" + render(checks) + "\n\n"
                "## Учебные сообщения\n\n" + render(data["messages"]))
        for command, section in sections.items():
            body += f"\n\n## {TITLES[command]}\n\n{section}"
        body += "\n\n## Проверочные сценарии\n\n" + render(scenarios)
        body += "\n\n## Контрольные дефекты\n\n" + render(defects)
        body += ("\n\n## Выводы\n\nФорма распределения частот сохраняется при Цезаре и Атбаше. "
                 "Повтор ключа Виженера создаёт периодичность. Краткий текст даёт меньше наблюдений. "
                 "Перестановка и решётка сохраняют состав символов, Полибий раскрывает повторы "
                 "координат, а учебный ротор остаётся предсказуемой периодической моделью. "
                 "LSB скрывает наличие сообщения, сохраняя уязвимость к изменению носителя. "
                 "SHA-256 выявляет изменения при сравнении с доверенным хешем. "
                 "AES-GCM обеспечивает конфиденциальность и аутентичность при корректном управлении "
                 "ключами и nonce. ECDSA проверяет происхождение и целостность по открытому ключу. "
                 "Доверие к открытому ключу проверяется отдельно. "
                 "Учебная модель, не для реальной защиты.")
        self._write("final_report.md", "Лабораторная работа № 5 Криптография", body)
        summary = "\n".join(f"{TITLES[name]} — {'OK' if status else 'ошибка'}"
                            for name, status in checks.items())
        passed = all(checks.values()) and all(row["ok"] for row in scenarios)
        return passed, f"{summary}\n\nОтчёт: {self.paths.reports / 'final_report.md'}"
