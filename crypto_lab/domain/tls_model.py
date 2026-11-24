from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric.x25519 import X25519PrivateKey
from cryptography.hazmat.primitives.kdf.hkdf import HKDF

from .certificates import inspect_certificate
from .contracts import CryptoResult
from .modern_primitives import decrypt, encrypt
from .validation import checked, require, require_text


@checked("tls_model")
def simulate(text, config):
    require_text(text)
    certificate = inspect_certificate(config["certificate"], config["server"],
                                      config["as_of"], config["trusted_issuer"])
    require(certificate.status == "ok", certificate.explanation)
    client = X25519PrivateKey.generate()
    server = X25519PrivateKey.generate()
    client_secret = client.exchange(server.public_key())
    server_secret = server.exchange(client.public_key())
    context = config["context"].encode()

    def derive(secret):
        return HKDF(hashes.SHA256(), 32, None, context).derive(secret)

    packet = encrypt(text, derive(client_secret), context)
    require(packet.status == "ok", packet.explanation)
    received = decrypt(packet.result, derive(server_secret), context)
    require(received.status == "ok", received.explanation)
    return CryptoResult("tls_model", "simulate", text, received.result,
                        {"stages": ["Условная проверка карточки", "X25519", "HKDF-SHA256",
                                    "AES-GCM"], "packet": packet.result},
                        explanation="TLS-модель не совместима с реальным протоколом. "
                                    "Учебная карточка не связывает сервер с обменом ключами.")
