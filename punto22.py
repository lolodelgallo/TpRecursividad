"""
Punto 22: mochila Jedi — búsqueda recursiva del sable de luz.
La mochila se representa como un vector (lista) de objetos.
"""

SABLE_DE_LUZ = "sable de luz"


def usar_la_fuerza(mochila, indice=0):
    """Recorre la mochila (vector) de a un objeto; devuelve si hay sable y cuántos sacó hasta hallarlo."""
    if indice >= len(mochila):
        return False, None

    if mochila[indice] == SABLE_DE_LUZ:
        return True, indice + 1

    return usar_la_fuerza(mochila, indice + 1)


def enunciado_salida(mochila):
    """Texto de ejemplo para el punto (b)."""
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
