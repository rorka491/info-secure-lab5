import json

import pytest

from ..domain.digital_signature import generate_pair, sign, verify


@pytest.fixture
def signed():
    private, public = generate_pair()
    return sign("Example", private).result, public


def test_original_signature_valid(signed):
    assert verify("Example", *signed).result == "действительна"


def test_changed_document_detected(signed):
    assert verify("Examples", *signed).result == "документ изменён"


def test_wrong_public_key_invalid(signed):
    _, public = generate_pair()
    assert verify("Example", signed[0], public).result == "недействительна"


def test_damaged_der_signature_invalid(signed):
    envelope = json.loads(signed[0])
    changed = bytearray.fromhex(envelope["der"])
    changed[-1] ^= 1
    envelope["der"] = changed.hex()
    assert verify("Example", json.dumps(envelope), signed[1]).result == "недействительна"


def test_damaged_public_key_wrong_format(signed):
    assert verify("Example", signed[0], "broken").result == "неверный формат"


def test_missing_document_insufficient(signed):
    assert verify("", *signed).result == "недостаточно данных"
