from ..domain.modern_primitives import decrypt, digest, encrypt, generate_key, verify_integrity


class IntegrityService:
    def run(self, data):
        text = data["documents_for_signing"][0]["text"]
        hashed = digest(text)
        key = generate_key()
        encrypted = encrypt(text, key)
        modified = bytearray.fromhex(encrypted.result)
        modified[-1] ^= 1
        return [hashed, verify_integrity(text, hashed.result),
                verify_integrity(text + "!", hashed.result), encrypted,
                decrypt(encrypted.result, key), decrypt(modified.hex(), key)]
