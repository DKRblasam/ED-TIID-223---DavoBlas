#!/usr/bin/env python3

# Árbol binario interactivo — solo tuplas y recursión, sin colas

RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
DIM = "\033[2m"


# ── Primitivas del árbol ──────────────────────────────────────────────────────


def nodo(val, izq=None, der=None):
    return (val, izq, der)


def val(n):
    return n[0] if n else None


def izq(n):
    return n[1] if n else None


def der(n):
    return n[2] if n else None


# ── Transformaciones funcionales ──────────────────────────────────────────────


def actualizar(n, ruta, fn):
    """Aplica fn al nodo alcanzado por ruta; reconstruye el árbol en el camino."""
    if not n:
        return None
    if not ruta:
        return fn(n)
    paso, resto = ruta[0], ruta[1:]
    if paso == "L":
        return nodo(val(n), actualizar(izq(n), resto, fn), der(n))
    if paso == "R":
        return nodo(val(n), izq(n), actualizar(der(n), resto, fn))
    return n


def agregar_hijo(arbol, ruta, lado, nuevo):
    def poner(n):
        if lado == "L" and not izq(n):
            return nodo(val(n), nodo(nuevo), der(n))
        if lado == "R" and not der(n):
            return nodo(val(n), izq(n), nodo(nuevo))
        return n

    return actualizar(arbol, ruta, poner)


# ── Recorrido BFS sin deque — recursión sobre listas ─────────────────────────


def bfs(arbol):
    """Devuelve [(ruta, nodo), ...] en orden por niveles, solo con recursión."""

    def expandir(frontera):
        if not frontera:
            return []
        siguientes = []
        for ruta_actual, n in frontera:
            if izq(n):
                siguientes.append((ruta_actual + "L", izq(n)))
            if der(n):
                siguientes.append((ruta_actual + "R", der(n)))
        return frontera + expandir(siguientes)

    return expandir([("", arbol)]) if arbol else []


# ── Visualización ─────────────────────────────────────────────────────────────


def imprimir_arbol(n, nivel=0, prefijo="Raíz"):
    if not n:
        return
    conector = "──" if nivel else ""
    indent = "  " * nivel
    print(
        f"{indent}{CYAN}{conector}{RESET}{BOLD}{prefijo}:{RESET} {GREEN}{val(n)}{RESET}"
    )
    if izq(n):
        imprimir_arbol(izq(n), nivel + 1, "Izq")
    if der(n):
        imprimir_arbol(der(n), nivel + 1, "Der")


def banner():
    print(f"\n{CYAN}{'━' * 42}{RESET}")
    print(f"{BOLD}      🌲 Constructor de Árbol Binario{RESET}")
    print(f"{CYAN}{'━' * 42}{RESET}")


# ── Entrada del usuario ───────────────────────────────────────────────────────

ALIAS = {
    "1": "L",
    "i": "L",
    "l": "L",
    "izq": "L",
    "izquierda": "L",
    "2": "R",
    "d": "R",
    "r": "R",
    "der": "R",
    "derecha": "R",
    "3": "S",
    "s": "S",
    "sig": "S",
    "siguiente": "S",
    "4": "T",
    "t": "T",
    "fin": "T",
    "terminar": "T",
}


def pedir_valor(prompt):
    while True:
        v = input(f"{YELLOW}{prompt}{RESET}").strip()
        if v:
            return v


def pedir_opcion():
    ayuda = (
        f"{DIM}[1/i] Izquierda  [2/d] Derecha  [3/s] Siguiente  [4/t] Terminar{RESET}"
    )
    while True:
        print(ayuda)
        op = input(f"{YELLOW}› {RESET}").strip().lower()
        if op in ALIAS:
            return ALIAS[op]
        print(f"{RED}Opción no válida.{RESET}")


# ── Bucle principal ───────────────────────────────────────────────────────────


def construir(arbol, candidatos, idx):
    """Paso recursivo del constructor interactivo."""
    if not candidatos or idx >= len(candidatos):
        return arbol

    ruta_actual, nodo_actual = candidatos[idx]
    etiqueta = ruta_actual or "raíz"

    print(f"\n{CYAN}{'─' * 42}{RESET}")
    print(f"  Nodo: {BOLD}{GREEN}{val(nodo_actual)}{RESET}  {DIM}({etiqueta}){RESET}")
    print(
        f"  Izq: {val(izq(nodo_actual)) or '—'}   Der: {val(der(nodo_actual)) or '—'}"
    )

    op = pedir_opcion()

    if op == "T":
        return arbol

    if op == "S":
        siguiente = (idx + 1) % max(len(candidatos), 1)
        return construir(arbol, candidatos, siguiente)

    # op es "L" o "R"
    lado_nombre = "izquierda" if op == "L" else "derecha"
    hijo_actual = izq(nodo_actual) if op == "L" else der(nodo_actual)

    if hijo_actual:
        print(f"{RED}  Ya existe hijo a la {lado_nombre}: {val(hijo_actual)}{RESET}")
        return construir(arbol, candidatos, idx)

    nuevo = pedir_valor(f"  Valor para hijo {lado_nombre} de '{val(nodo_actual)}': ")
    arbol_nuevo = agregar_hijo(arbol, ruta_actual, op, nuevo)
    # Recalcula candidatos con el árbol actualizado
    return construir(arbol_nuevo, bfs(arbol_nuevo), idx)


def main():
    banner()
    raiz_val = pedir_valor("Valor de la raíz: ")
    arbol = nodo(raiz_val)

    arbol_final = construir(arbol, bfs(arbol), 0)

    print(f"\n{CYAN}{'━' * 42}{RESET}")
    print(f"{BOLD}  Árbol final{RESET}")
    print(f"{CYAN}{'━' * 42}{RESET}\n")
    imprimir_arbol(arbol_final)
    print(f"\n{CYAN}{'━' * 42}{RESET}\n")


if __name__ == "__main__":
    main()
