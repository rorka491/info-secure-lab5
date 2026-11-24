import json
from collections import Counter
from math import factorial
import re

from .classical_ciphers import caesar
from .contracts import CryptoResult
from .normalization import normalize
from .validation import checked, require


@checked("caesar_analysis")
def brute_force(text, alphabet, preserved, vocabulary):
    first = normalize(text, alphabet, preserved)
    require(first.status == "ok", first.explanation)
    words = set(vocabulary)
    candidates = []
    for shift in range(len(alphabet)):
        candidate = caesar(text, shift, alphabet, preserved, decrypt=True).result
        score = sum(word in words for word in re.findall(r"[^\W\d_]+", candidate.upper()))
        candidates.append({"shift": shift, "text": candidate, "score": score})
    candidates.sort(key=lambda row: (-row["score"], row["shift"]))
    return CryptoResult("caesar_analysis", "brute_force", text,
                        json.dumps(candidates, ensure_ascii=False),
                        explanation="Баллы зависят от словаря. Краткие фразы часто дают ничьи.")


@checked("frequency")
def frequencies(text, alphabet, preserved):
    normalized = normalize(text, alphabet, preserved)
    require(normalized.status == "ok", normalized.explanation)
    length = len(normalized.result)
    counts = Counter(normalized.result)
    rows = [{"letter": letter, "count": count, "share": count / length}
            for letter, count in sorted(counts.items(), key=lambda pair: (-pair[1], pair[0]))]
    return CryptoResult("frequency", "count", text, json.dumps(rows, ensure_ascii=False),
                        {"letters": length, "characters": len(text)})


@checked("key_space")
def key_space(model, alphabet_size, key_length, block_size):
    require(all(type(n) is int and 1 <= n <= 100 for n in
                (alphabet_size, key_length, block_size)), "Ожидаются размеры от 1 до 100.")
    counts = {"caesar": alphabet_size, "vigenere": alphabet_size ** key_length,
              "permutation": factorial(block_size)}
    return CryptoResult("key_space", "count", model, json.dumps(counts),
                        explanation="Размер пространства ключей не учитывает статистические атаки.")
