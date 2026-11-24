import json

from ..domain.steganography import cardano, embed, extract


def test_lsb_utf8_round_trip():
    assert extract(embed("Ёж!", [170] * 72).result).result == "Ёж!"


def test_lsb_39_pixels_rejects_one_byte():
    assert embed("A", [170] * 39).status == "error"


def test_lsb_header_flip_rejected():
    carrier = json.loads(embed("A", [170] * 40).result)
    carrier[0] ^= 1
    assert extract(json.dumps(carrier)).status == "error"


def test_lsb_payload_flip_silently_changes_text():
    carrier = json.loads(embed("A", [170] * 40).result)
    carrier[-1] ^= 1
    assert extract(json.dumps(carrier)).result == "@"


def test_cardano_round_trip_with_padding(params):
    grille = params["cardano"]
    args = grille["size"], grille["holes"], grille["pad"]
    encrypted = cardano("CODE", *args)
    assert len(encrypted.result) == 16
    assert cardano(encrypted.result, *args, length=4).result == "CODE"


def test_cardano_overlapping_mask_rejected():
    assert cardano("A", 4, [[0, 0]] * 4, ".").status == "error"
