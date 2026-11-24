from ..domain import classical_ciphers as cipher
from ..domain.normalization import detect_alphabet


class CryptoService:
    def run(self, data):
        params = data["algorithm_params"]
        config = params["classical"]
        marks = params["preserved"]
        rows = []
        for message in data["messages"]:
            language, text = message["alphabet"], message["text"]
            alphabet = params["alphabets"][language]
            detected = detect_alphabet(text, params["alphabets"], marks)
            operations = {
                "caesar": (cipher.caesar, (config["shift"], alphabet, marks)),
                "atbash": (cipher.atbash, (alphabet, marks)),
                "polybius": (cipher.polybius, (params["polybius"][language], marks,
                                               params["aliases"][language])),
                "vigenere": (cipher.vigenere, (config["keys"][language], alphabet, marks)),
                "permutation": (cipher.permutation, (config["permutation"],)),
                "rotor": (cipher.rotor, (config["wiring"][language], config["offset"],
                                          alphabet, marks)),
            }
            for name in message["algorithms"]:
                function, args = operations[name]
                encrypted = function(text, *args)
                if encrypted.status != "ok":
                    rows.append({"id": message["id"], "name": name, "encrypted": encrypted,
                                 "status": "error"})
                    continue
                recovered = (function(encrypted.result, *args) if name == "atbash" else
                             function(encrypted.result, *args, decrypt=True))
                expected = text
                if name == "polybius":
                    for alias, letter in params["aliases"][language].items():
                        expected = expected.replace(alias, letter).replace(alias.lower(), letter.lower())
                passed = recovered.status == "ok" and recovered.result == expected
                passed = passed and detected.status == "ok" and detected.result == language
                rows.append({"id": message["id"], "name": name, "encrypted": encrypted,
                             "recovered": recovered.result, "match": passed,
                             "status": "ok" if passed else "error"})
        return rows
