import json

from .contracts import CryptoResult
from .normalization import apply_format, in_alphabet, letter_positions
from .validation import checked, require, require_text


def direction(decrypt):
    return "decrypt" if decrypt else "encrypt"


@checked("caesar")
def caesar(text, shift, alphabet, preserved, decrypt=False):
    positions = letter_positions(text, alphabet, preserved)
    require(type(shift) is int, "Сдвиг должен быть целым числом.")
    shift %= len(alphabet)
    offset = -shift if decrypt else shift
    letters = [alphabet[(alphabet.index(text[i].upper()) + offset) % len(alphabet)]
               for i in positions]
    return CryptoResult("caesar", direction(decrypt), text,
                        apply_format(text, positions, letters), {"shift": shift})


@checked("atbash")
def atbash(text, alphabet, preserved):
    positions = letter_positions(text, alphabet, preserved)
    letters = [alphabet[-alphabet.index(text[i].upper()) - 1] for i in positions]
    return CryptoResult("atbash", "transform", text, apply_format(text, positions, letters))


@checked("vigenere")
def vigenere(text, key, alphabet, preserved, decrypt=False):
    positions = letter_positions(text, alphabet, preserved)
    require(isinstance(key, str) and bool(key) and all(in_alphabet(c, alphabet) for c in key),
            "Ключ Виженера должен состоять из букв выбранного алфавита.")
    shifts = [alphabet.index(c.upper()) for c in key]
    sign = -1 if decrypt else 1
    letters = [alphabet[(alphabet.index(text[i].upper()) + sign * shifts[j % len(key)])
                       % len(alphabet)] for j, i in enumerate(positions)]
    return CryptoResult("vigenere", direction(decrypt), text,
                        apply_format(text, positions, letters), {"key": key})


@checked("polybius")
def polybius(text, square, preserved, aliases, decrypt=False):
    require_text(text)
    cells = {letter: (row, col) for row, line in enumerate(square, 1)
             for col, letter in enumerate(line, 1) if letter}
    if decrypt:
        lookup = {position: letter for letter, position in cells.items()}
        tokens = json.loads(text)
        require(isinstance(tokens, list) and bool(tokens), "Ожидается список координат.")
        output = []
        for token in tokens:
            if isinstance(token, str) and len(token) == 1 and token in preserved:
                output.append(token)
                continue
            require(isinstance(token, list) and len(token) == 3
                    and type(token[0]) is int and type(token[1]) is int
                    and type(token[2]) is bool and tuple(token[:2]) in lookup,
                    "Некорректная координата или регистр.")
            letter = lookup[tuple(token[:2])]
            output.append(letter.lower() if token[2] else letter)
        result = "".join(output)
    else:
        output = []
        for char in text:
            if char in preserved:
                output.append(char)
                continue
            letter = aliases.get(char.upper(), char.upper())
            require(letter in cells, "Символ отсутствует в квадрате Полибия.")
            output.append([*cells[letter], char.islower()])
        result = json.dumps(output, ensure_ascii=False)
    return CryptoResult("polybius", direction(decrypt), text, result,
                        {"aliases": aliases})


@checked("permutation")
def permutation(text, key, decrypt=False):
    require_text(text)
    require(isinstance(key, (list, tuple)) and bool(key)
            and all(type(i) is int for i in key) and sorted(key) == list(range(len(key))),
            "Ключ должен быть перестановкой индексов от 0 до размера блока минус 1.")
    order = [key.index(i) for i in range(len(key))] if decrypt else key
    output = []
    for start in range(0, len(text), len(key)):
        block = text[start:start + len(key)]
        short_key = [i for i in key if i < len(block)]
        short_order = [short_key.index(i) for i in range(len(block))] if decrypt else short_key
        output.extend(block[i] for i in (order if len(block) == len(key) else short_order))
    return CryptoResult("permutation", direction(decrypt), text, "".join(output), {"key": key})


@checked("rotor")
def rotor(text, wiring, offset, alphabet, preserved, decrypt=False):
    positions = letter_positions(text, alphabet, preserved)
    require(isinstance(wiring, str) and sorted(wiring) == sorted(alphabet)
            and type(offset) is int, "Некорректная проводка или начальная позиция ротора.")
    source, target = (wiring, alphabet) if decrypt else (alphabet, wiring)
    size = len(alphabet)
    output = []
    for step, index in enumerate(positions):
        position = (offset + step) % size
        shifted = alphabet[(alphabet.index(text[index].upper()) + position) % size]
        mapped = target[source.index(shifted)]
        output.append(alphabet[(alphabet.index(mapped) - position) % size])
    return CryptoResult("rotor", direction(decrypt), text, apply_format(text, positions, output),
                        {"offset": offset % size, "wiring": wiring},
                        explanation="Упрощённая роторная модель, не полная историческая Энигма.")
