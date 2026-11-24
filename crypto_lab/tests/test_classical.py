import pytest

from ..domain import classical_ciphers as c
from ..domain.normalization import detect_alphabet, normalize, restore_format


@pytest.mark.parametrize("language,text,shift", [
    ("ru", "ВСТРЕЧА УЧЕБНОЙ ГРУППЫ В ДЕСЯТЬ ЧАСОВ", 3),
    ("en", "Quiet, team 42!", 3),
    ("en", "Keep Case!", 26),
    ("ru", "Ёж!", 67),
    ("en", "West", -3),
], ids=["russian_shift_3_round_trip", "latin_case_round_trip", "shift_26_identity",
        "shift_67_modulo_33", "negative_shift_round_trip"])
def test_caesar(params, language, text, shift):
    alphabet, marks = params["alphabets"][language], params["preserved"]
    encrypted = c.caesar(text, shift, alphabet, marks)
    assert encrypted.key_or_params["shift"] == shift % len(alphabet)
    assert c.caesar(encrypted.result, shift, alphabet, marks, decrypt=True).result == text


def test_caesar_known_vector(params):
    assert c.caesar("Abc, xyz!", 3, params["alphabets"]["en"], params["preserved"]).result == "Def, abc!"


def test_atbash_twice_original(params):
    args = params["alphabets"]["ru"], params["preserved"]
    assert c.atbash(c.atbash("Код 42!", *args).result, *args).result == "Код 42!"


@pytest.mark.parametrize("language,text,expected", [("en", "Jazz!", "Iazz!"), ("ru", "Ёж 3", "Ёж 3")],
                         ids=["latin_J_merges_into_I", "russian_full_alphabet"])
def test_polybius(params, language, text, expected):
    args = params["polybius"][language], params["preserved"], params["aliases"][language]
    encoded = c.polybius(text, *args)
    assert c.polybius(encoded.result, *args, decrypt=True).result == expected


def test_vigenere_repeated_letters_and_round_trip(params):
    args = "LAB", params["alphabets"]["en"], params["preserved"]
    encrypted = c.vigenere("AAA, AAA", *args)
    assert encrypted.result == "LAB, LAB"
    assert c.vigenere(encrypted.result, *args, decrypt=True).result == "AAA, AAA"


def test_permutation_partial_block_round_trip():
    key = [2, 0, 3, 1]
    encoded = c.permutation("Cipher!", key)
    assert c.permutation(encoded.result, key, decrypt=True).result == "Cipher!"


def test_rotor_round_trip(params):
    args = params["classical"]["wiring"]["en"], 2, params["alphabets"]["en"], params["preserved"]
    encoded = c.rotor("Study group!", *args)
    assert c.rotor(encoded.result, *args, decrypt=True).result == "Study group!"


def test_normalize_and_restore_russian_format(params):
    text, marks = "Ёж, 42!", params["preserved"]
    assert detect_alphabet(text, params["alphabets"], marks).result == "ru"
    args = params["alphabets"]["ru"], marks
    assert normalize(text, *args).result == "ЁЖ"
    assert restore_format(text, "АБ", *args).result == "Аб, 42!"
