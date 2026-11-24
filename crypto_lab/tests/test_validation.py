import pytest

from ..data.repository import DataError, Repository
from ..domain.classical_ciphers import caesar, permutation, polybius, vigenere


@pytest.mark.parametrize("text,shift", [("", 3), ("A😀", 3), ("A", "3"), ("A", False), ("AЯ", 2)],
                         ids=["empty", "unsupported_emoji", "string_shift", "bool_shift", "mixed_alphabets"])
def test_caesar_invalid_inputs_error(params, text, shift):
    result = caesar(text, shift, params["alphabets"]["en"], params["preserved"])
    assert result.status == "error"
    assert result.explanation


def test_polybius_unsupported_letter_error(params):
    result = polybius("É", params["polybius"]["en"], params["preserved"], params["aliases"]["en"])
    assert result.status == "error"


def test_empty_vigenere_key_error(params):
    assert vigenere("LAB", "", params["alphabets"]["en"], params["preserved"]).status == "error"


def test_permutation_duplicate_indices_error():
    assert permutation("LAB", [1, 1]).status == "error"


def test_missing_input_dataset_controlled(tmp_path):
    with pytest.raises(DataError, match="messages.json"):
        Repository(tmp_path).load()


def test_corrupt_json_dataset_controlled(tmp_path):
    (tmp_path / "messages.json").write_text("{", encoding="utf-8")
    with pytest.raises(DataError, match="messages.json"):
        Repository(tmp_path).load()
