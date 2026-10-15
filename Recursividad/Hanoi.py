def hanoi(n: int, origen: str, destino: str, auxiliar: str) -> None:
    if n == 1:  # Caso base
        print(f"Mover disco 1 de {origen} a {destino}")
        return
    
    # Caso recursivo
    hanoi(n - 1, origen, auxiliar, destino)
    print(f"Mover disco {n} de {origen} a {destino}")
    hanoi(n - 1, auxiliar, destino, origen)

# Ejemplo de uso con 3 discos
hanoi(3, origen="A", destino="C", auxiliar="B")