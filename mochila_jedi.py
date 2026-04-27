"""
Punto 22: mochila Jedi — búsqueda recursiva del sable de luz.
La mochila se representa como un vector (lista) de objetos.
"""

from typing import List, Optional, Tuple

# Nombre canónico del objetivo (ajustar si hace falta, p. ej. "Sable de luz", "lightsaber")
SABLE_DE_LUZ = "sable de luz"


def usar_la_fuerza(
    mochila: List[object],
    indice: int = 0,
) -> Tuple[bool, Optional[int]]:
    """
    a) Saca/considera objetos de a uno hasta hallar un sable de luz o agotar la mochila.

    b) Devuelve (encontrado, objetos_saqueados):
       - si hay sable: (True, cuántos objetos fue necesario "sacar" hasta el primero);
       - si no hay: (False, None) — los saqueados serían len(mochila) si se vacía toda.

    c) mochila es un vector (list); no se modifica la lista original: el índice recorre
       la posición como si fuera el siguiente objeto a extraer.
    """
    if indice >= len(mochila):
        return False, None

    if mochila[indice] == SABLE_DE_LUZ:
        return True, indice + 1

    return usar_la_fuerza(mochila, indice + 1)


def enunciado_salida(mochila: List[object]) -> str:
    """Texto de ejemplo para (b)."""
    encontro, n = usar_la_fuerza(mochila)
    if encontro:
        return (
            f"Sable de luz: sí. Se necesitaron {n} objeto(s) retirado(s) para hallarlo."
        )
    n_total = len(mochila)
    return (
        f"Sable de luz: no. Se revisaron {n_total} objeto(s) sin hallarlo; la mochila quedó vacía."
    )


if __name__ == "__main__":
    ejemplos = [
        ["cuerda", "ración", SABLE_DE_LUZ, "mapa"],
        ["libro", "barras", "linterna"],
        [SABLE_DE_LUZ],
        [],
    ]
    for i, m in enumerate(ejemplos, 1):
        print(f"Mochila {i}: {m!r}")
        print(f"  {enunciado_salida(m)}")
        print()
