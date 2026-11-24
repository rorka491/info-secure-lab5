import json
from collections import Counter

from .contracts import CryptoResult
from .validation import checked, require


@checked("incidents")
def summarize(cards):
    require(isinstance(cards, list) and bool(cards), "Нет карточек инцидентов.")
    return CryptoResult("incidents", "compare", "", json.dumps(cards, ensure_ascii=False, indent=2))


@checked("network_log")
def inspect_log(events, rules):
    fields = {"time", "destination", "protocol", "bytes_out", "process", "check"}
    require(isinstance(events, list) and all(isinstance(row, dict) and fields <= row.keys()
            and type(row["bytes_out"]) is int and row["bytes_out"] >= 0 for row in events),
            "Поля журнала отсутствуют или объём некорректен.")
    counts = Counter((row["process"], row["destination"]) for row in events)
    findings = []
    for row in events:
        flags = [
            label for label, condition in (
                ("большой исходящий объём", row["bytes_out"] >= rules["large_bytes"]),
                ("новый процесс", row["process"] not in rules["known_processes"]),
                ("повторяющиеся соединения",
                 counts[row["process"], row["destination"]] >= rules["repeat_count"]),
                ("неизвестный узел", row["destination"] not in rules["known_hosts"]),
            ) if condition
        ]
        if flags:
            findings.append({**row, "flags": flags})
    return CryptoResult("network_log", "inspect", str(len(events)),
                        json.dumps(findings, ensure_ascii=False, indent=2),
                        explanation="Признаки требуют проверки. HTTPS сам по себе не признак атаки.")
