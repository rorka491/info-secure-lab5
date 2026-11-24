import json
from pathlib import Path


class DataError(ValueError):
    pass


class Repository:
    def __init__(self, root: Path):
        self.root = root

    def read(self, name):
        try:
            return json.loads((self.root / f"{name}.json").read_text(encoding="utf-8"))
        except (OSError, ValueError) as error:
            raise DataError(f"Набор {name}.json недоступен или повреждён.") from error

    def load(self):
        data = {name: self.read(name) for name in
                ("messages", "algorithm_params", "test_scenarios", "documents_for_signing")}
        try:
            params = data["algorithm_params"]
            messages = data["messages"]
            if len(messages) < 8 or len({row["id"] for row in messages}) != len(messages):
                raise ValueError
            for row in messages:
                if (row["alphabet"] not in params["alphabets"] or not row["text"].strip()
                        or not row["purpose"].strip() or not row["algorithms"]):
                    raise ValueError
            scenarios = data["test_scenarios"]
            if len(scenarios["journal"]) < 20 or not data["documents_for_signing"][0]["text"].strip():
                raise ValueError
            required = {*scenarios["analysis_ids"], scenarios["caesar_id"]}
            if not required <= {row["id"] for row in messages}:
                raise ValueError
        except (KeyError, IndexError, AttributeError, TypeError, ValueError) as error:
            raise DataError("Во входных данных отсутствуют обязательные записи или поля.") from error
        return data
