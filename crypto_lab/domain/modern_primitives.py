import hashlib
import hmac
import re
from os import urandom

from cryptography.exceptions import InvalidTag
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

from .contracts import CryptoResult
from .validation import checked, require, require_text


@checked("sha256")
def digest(text):
    require_text(text)
    return CryptoResult("sha256", "digest", text, hashlib.sha256(text.encode()).hexdigest())


@checked("sha256")
def verify_integrity(text, expected):
    require(isinstance(expected, str) and re.fullmatch("[0-9a-fA-F]{64}", expected),
            "Ожидается SHA-256 в виде 64 шестнадцатеричных цифр.")
    actual = digest(text)
    require(actual.status == "ok", actual.explanation)
    match = hmac.compare_digest(actual.result, expected.lower())
    return CryptoResult("sha256", "verify", text, actual.result,
                        status="ok" if match else "error",
                        explanation="Хеш совпал." if match else "Хеш изменился.")


def generate_key():
    return AESGCM.generate_key(bit_length=256)


@checked("aes_gcm")
def encrypt(text, key, aad=b""):
    require_text(text)
    nonce = urandom(12)
    encrypted = AESGCM(key).encrypt(nonce, text.encode(), aad)
    return CryptoResult("aes_gcm", "encrypt", text, (nonce + encrypted).hex(),
                        {"nonce": nonce.hex(), "tag_bytes": 16})


@checked("aes_gcm")
def decrypt(encoded, key, aad=b""):
    require_text(encoded)
    frame = bytes.fromhex(encoded)
    require(len(frame) > 28, "Ожидаются nonce, шифротекст и тег.")
    try:
        plaintext = AESGCM(key).decrypt(frame[:12], frame[12:], aad)
    except InvalidTag:
        return CryptoResult("aes_gcm", "decrypt", encoded, status="error",
                            explanation="Проверка аутентичности AES-GCM не пройдена.")
    return CryptoResult("aes_gcm", "decrypt", encoded, plaintext.decode())
