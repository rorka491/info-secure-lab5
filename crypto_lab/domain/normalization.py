from .contracts import CryptoResult
from .validation import checked, require, require_text


def validate_alphabet(alphabet):
    require(
        isinstance(alphabet, str) and len(alphabet) > 1
        and len(set(alphabet)) == len(alphabet)
        and all(letter.isalpha() and letter.isupper() for letter in alphabet),
        "Некорректный алфавит.",
    )


def letter_positions(text, alphabet, preserved):
    require_text(text)
    validate_alphabet(alphabet)
    require(isinstance(preserved, str), "Некорректный набор сохраняемых символов.")
    require(all(in_alphabet(char, alphabet) or char in preserved for char in text),
            "В тексте есть символы вне алфавита и набора допустимых знаков.")
    positions = [index for index, char in enumerate(text) if in_alphabet(char, alphabet)]
    require(bool(positions), "В тексте нет букв выбранного алфавита.")
    return positions


def in_alphabet(char, alphabet):
    upper = char.upper()
    return len(upper) == 1 and upper in alphabet and char in (upper, upper.lower())


def apply_format(text, positions, letters):
    require(len(positions) == len(letters), "Количество букв не совпадает с шаблоном.")
    output = list(text)
    for index, letter in zip(positions, letters):
        output[index] = letter.lower() if text[index].islower() else letter
    return "".join(output)


@checked("normalization")
def normalize(text, alphabet, preserved):
    positions = letter_positions(text, alphabet, preserved)
    return CryptoResult("normalization", "normalize", text,
                        "".join(text[i].upper() for i in positions), {"positions": positions})


@checked("normalization")
def detect_alphabet(text, alphabets, preserved):
    require_text(text)
    require(isinstance(alphabets, dict) and isinstance(preserved, str),
            "Некорректные настройки алфавита.")
    matches = [name for name, alphabet in alphabets.items()
               if all(in_alphabet(char, alphabet) or char in preserved for char in text)
               and any(in_alphabet(char, alphabet) for char in text)]
    require(len(matches) == 1, "Не удалось однозначно определить алфавит.")
    return CryptoResult("normalization", "detect_alphabet", text, matches[0])


@checked("normalization")
def check_symbols(text, alphabet, preserved):
    letter_positions(text, alphabet, preserved)
    return CryptoResult("normalization", "check_symbols", text, text)


@checked("normalization")
def restore_format(text, letters, alphabet, preserved):
    positions = letter_positions(text, alphabet, preserved)
    require(isinstance(letters, str) and all(c in alphabet for c in letters),
            "Преобразованные буквы вне алфавита.")
    return CryptoResult("normalization", "restore_format", text,
                        apply_format(text, positions, letters))
