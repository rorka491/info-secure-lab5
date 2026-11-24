import json

from ..domain.classical_ciphers import caesar
from ..domain.steganography import cardano, embed, extract


class StegoService:
    def run(self, data):
        p = data["algorithm_params"]
        row = data["messages"][0]
        text, lang = row["text"], row["alphabet"]
        encrypted = caesar(text, p["classical"]["shift"], p["alphabets"][lang], p["preserved"])
        carrier = [p["lsb"]["value"]] * p["lsb"]["pixels"]
        plain = embed(text, carrier)
        combined = embed(encrypted.result, carrier)
        if plain.status != "ok" or combined.status != "ok":
            return [plain, combined]
        decoded = extract(plain.result)
        hidden_cipher = extract(combined.result)
        recovered = caesar(hidden_cipher.result, p["classical"]["shift"], p["alphabets"][lang],
                           p["preserved"], decrypt=True)
        altered = json.loads(plain.result)
        altered[0] ^= 1
        damaged = extract(json.dumps(altered))
        altered = json.loads(plain.result)
        altered[39] ^= 1
        changed_payload = extract(json.dumps(altered))
        grille = p["cardano"]
        args = (grille["size"], grille["holes"], grille["pad"])
        scrambled = cardano(grille["text"], *args)
        restored = cardano(scrambled.result, *args, length=len(grille["text"]))
        return [{"plain": decoded.result, "hidden_ciphertext": hidden_cipher.result,
                 "after_deciphering": recovered.result, "header_flip": damaged.explanation,
                 "payload_flip": changed_payload.result, "payload_changed": changed_payload.result != text,
                 "changed_pixels": sum(a != b for a, b in zip(json.loads(plain.result), carrier))},
                scrambled, restored]
