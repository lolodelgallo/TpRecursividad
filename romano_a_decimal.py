"""
Punto 5: conversión de números romanos a decimales.
"""


_VALORES = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def _valor_simbolo(c: str) -> int:
    if c not in _VALORES:
        raise ValueError(f"Carácter no válido en romano: {c!r}")
    return _VALORES[c]


def romano_a_decimal(romano: str) -> int:
    """
    Convierte una cadena en notación romana a entero (base 10).
    Soporta notación clásica con resta (IV, IX, etc.).
    """
    if not romano or not romano.isalpha():
        raise ValueError("Se esperaba un número romano no vacío (letras I, V, X, L, C, D, M).")

    r = romano.strip().upper()
    total = 0
    i = 0
    while i < len(r):
        v_actual = _valor_simbolo(r[i])
        if i + 1 < len(r):
            v_sig = _valor_simbolo(r[i + 1])
            if v_actual < v_sig:
                total += v_sig - v_actual
                i += 2
                continue
        total += v_actual
        i += 1
    return total


if __name__ == "__main__":
    pruebas = ["I", "IV", "IX", "XXVII", "CDXLIV", "MCMXCIV", "MMXXVI"]
    for s in pruebas:
        print(f"{s!r} -> {romano_a_decimal(s)}")
