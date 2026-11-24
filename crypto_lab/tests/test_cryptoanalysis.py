import json

from ..domain.cryptoanalysis import brute_force, frequencies, key_space
from ..domain.incidents import inspect_log


def test_caesar_26_candidates_correct_key_present(params):
    result = brute_force("Phhw!", params["alphabets"]["en"], params["preserved"], ["MEET"])
    candidates = json.loads(result.result)
    assert len(candidates) == 26
    assert candidates[0] == {"shift": 3, "text": "Meet!", "score": 1}


def test_frequency_A3_B1(params):
    stats = frequencies("AA, B a!", params["alphabets"]["en"], params["preserved"])
    assert json.loads(stats.result) == [
        {"letter": "A", "count": 3, "share": 0.75}, {"letter": "B", "count": 1, "share": 0.25}]


def test_alphabet_26_key_3_block_4(params):
    assert json.loads(key_space("fixed", 26, 3, 4).result) == {
        "caesar": 26, "vigenere": 17576, "permutation": 24}


def test_large_https_flagged_with_unknown_process_and_host(data, params):
    result = inspect_log(data["test_scenarios"]["journal"], params["network"])
    events = json.loads(result.result)
    assert any("повторяющиеся соединения" in event["flags"] for event in events)
    assert events[-1]["protocol"] == "HTTPS"
    assert len(events[-1]["flags"]) == 3
