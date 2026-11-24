import json

from .contracts import CryptoResult
from .validation import checked, require, require_text


def pixels(values):
    require(isinstance(values, list)
            and all(type(value) is int and 0 <= value <= 255 for value in values),
            "Носитель должен быть списком целых значений от 0 до 255.")


@checked("lsb")
def embed(text, carrier):
    require_text(text)
    pixels(carrier)
    payload = text.encode("utf-8")
    require(32 + 8 * len(payload) <= len(carrier), "Недостаточная вместимость носителя.")
    frame = len(payload).to_bytes(4, "big") + payload
    bits = [int(bit) for byte in frame for bit in f"{byte:08b}"]
    output = carrier.copy()
    for i, bit in enumerate(bits):
        output[i] = (output[i] & 254) | bit
    return CryptoResult("lsb", "embed", text, json.dumps(output), {"payload_bytes": len(payload)})


@checked("lsb")
def extract(encoded):
    carrier = json.loads(encoded)
    pixels(carrier)
    require(len(carrier) >= 32, "Заголовок длины отсутствует.")

    def read(start, stop):
        return bytes(int("".join(str(value & 1) for value in carrier[i:i + 8]), 2)
                     for i in range(start, stop, 8))

    size = int.from_bytes(read(0, 32), "big")
    require(0 < size <= (len(carrier) - 32) // 8, "Длина сообщения повреждена.")
    return CryptoResult("lsb", "extract", encoded, read(32, 32 + size * 8).decode("utf-8"),
                        explanation="LSB не проверяет подлинность или целостность полезной нагрузки.")


def grille_order(size, holes):
    require(type(size) is int and 2 <= size <= 32 and size % 2 == 0,
            "Укажите чётный размер решётки от 2 до 32.")
    require(isinstance(holes, (list, tuple)) and len(holes) == size * size // 4,
            "Число отверстий должно равняться четверти числа ячеек.")
    require(all(isinstance(cell, (list, tuple)) and len(cell) == 2
                and all(type(x) is int and 0 <= x < size for x in cell) for cell in holes),
            "Координаты отверстий вне решётки.")
    order = []
    for _ in range(4):
        order.extend(row * size + col for row, col in sorted(holes))
        holes = [(col, size - 1 - row) for row, col in holes]
    require(len(set(order)) == size * size, "После поворота отверстия пересекаются.")
    return order


@checked("cardano")
def cardano(text, size, holes, pad, length=None):
    require_text(text)
    order = grille_order(size, holes)
    capacity = len(order)
    require(isinstance(pad, str) and len(pad) == 1, "Заполнитель должен быть одним символом.")
    if length is None:
        require(len(text) <= capacity, "Текст не помещается в решётку.")
        output = [pad] * capacity
        for index, char in zip(order, text):
            output[index] = char
        return CryptoResult("cardano", "encrypt", text, "".join(output), {"length": len(text)})
    require(type(length) is int and 0 < length <= capacity and len(text) == capacity,
            "Неверная длина матрицы или сообщения.")
    decoded = "".join(text[i] for i in order)
    require(decoded[length:] == pad * (capacity - length), "Заполнитель повреждён.")
    return CryptoResult("cardano", "decrypt", text, decoded[:length], {"length": length})
