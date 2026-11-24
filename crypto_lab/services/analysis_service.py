import json

from ..domain.classical_ciphers import atbash, caesar, vigenere
from ..domain.cryptoanalysis import brute_force, frequencies, key_space


class AnalysisService:
    def run(self, data):
        p = data["algorithm_params"]
        scenarios = data["test_scenarios"]
        lookup = {row["id"]: row for row in data["messages"]}
        output = []
        for identifier in scenarios["analysis_ids"]:
            row = lookup[identifier]
            lang, text = row["alphabet"], row["text"]
            alphabet = p["alphabets"][lang]
            marks = p["preserved"]
            key = p["classical"]["keys"][lang]
            variants = {
                "original": text,
                "caesar": caesar(text, p["classical"]["shift"], alphabet, marks).result,
                "atbash": atbash(text, alphabet, marks).result,
                "vigenere": vigenere(text, key, alphabet, marks).result,
            }
            statistics = {}
            for name, value in variants.items():
                result = frequencies(value, alphabet, marks)
                statistics[name] = (json.loads(result.result) if result.status == "ok" else result)
            row = {"id": identifier, "characters": len(text), "frequencies": statistics}
            if identifier == scenarios["analysis_ids"][0]:
                result = brute_force(variants["caesar"], alphabet, marks, p["vocabulary"][lang])
                row["caesar_candidates"] = json.loads(result.result) if result.status == "ok" else result
            output.append(row)
        output.append(key_space("fixed_length", len(alphabet), len(key),
                                len(p["classical"]["permutation"])))
        return output
