import hashlib
import json

from cryptography.exceptions import InvalidSignature, UnsupportedAlgorithm
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec, utils

from .contracts import CryptoResult
from .validation import checked, require, require_text


def generate_pair():
    private = ec.generate_private_key(ec.SECP256R1())
    public = private.public_key().public_bytes(
        serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    return private, public.decode("ascii")


@checked("ecdsa")
def sign(document, private):
    require_text(document)
    require(isinstance(private, ec.EllipticCurvePrivateKey), "Некорректный закрытый ключ.")
    digest = hashlib.sha256(document.encode()).digest()
    signature = private.sign(digest, ec.ECDSA(utils.Prehashed(hashes.SHA256())))
    return CryptoResult("ecdsa", "sign", document,
                        json.dumps({"digest": digest.hex(), "der": signature.hex()}))


def verify(document, envelope, public_pem):
    def outcome(verdict, status="error"):
        return CryptoResult("ecdsa", "verify", document if isinstance(document, str) else "",
                            verdict, status=status, explanation=verdict)

    if not document or not envelope or not public_pem:
        return outcome("недостаточно данных")
    try:
        require_text(document)
        value = json.loads(envelope)
        digest = bytes.fromhex(value["digest"])
        signature = bytes.fromhex(value["der"])
        utils.decode_dss_signature(signature)
        require(len(digest) == 32, "Неверная длина хеша.")
        key = serialization.load_pem_public_key(public_pem.encode())
        require(isinstance(key, ec.EllipticCurvePublicKey), "Ожидается открытый ключ ECDSA.")
        key.verify(signature, digest, ec.ECDSA(utils.Prehashed(hashes.SHA256())))
    except InvalidSignature:
        return outcome("недействительна")
    except (AttributeError, ValueError, KeyError, TypeError, UnsupportedAlgorithm):
        return outcome("неверный формат")

    if hashlib.sha256(document.encode()).digest() != digest:
        return outcome("документ изменён")
    return outcome("действительна", "ok")
