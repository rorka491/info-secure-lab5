from ..domain.modern_primitives import decrypt, digest, encrypt, generate_key, verify_integrity
from ..domain.tls_model import simulate


def test_sha256_abc_vector_and_changed_document():
    expected = "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert digest("abc").result == expected
    assert verify_integrity("abc", expected).status == "ok"
    assert verify_integrity("abd", expected).status == "error"


def test_aes_gcm_nonce_fresh_and_message_round_trip():
    key = generate_key()
    first = encrypt("Учебное сообщение", key)
    second = encrypt("Учебное сообщение", key)
    assert first.key_or_params["nonce"] != second.key_or_params["nonce"]
    assert decrypt(first.result, key).result == "Учебное сообщение"


def test_aes_gcm_changed_tag_error_no_plaintext():
    key = generate_key()
    modified = bytearray.fromhex(encrypt("Example", key).result)
    modified[-1] ^= 1
    result = decrypt(modified.hex(), key)
    assert result.status == "error"
    assert not result.result


def test_tls_good_card_and_wrong_subject(params):
    config = params["tls"]
    assert simulate("Example", config).result == "Example"
    assert simulate("Example", {**config, "server": "other.example.test"}).status == "error"
