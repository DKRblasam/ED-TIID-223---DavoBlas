def suma_lista_profunda(lista: list) -> int:
    total = 0
    for elemento in lista:
        if isinstance(elemento, list):  # Si es sublista, resolver recursivamente
            total += suma_lista_profunda(elemento)
        else:                          # Caso base implícito (es un número)
            total += elemento
    return total

# Ejemplo de uso
datos = [1, [2, [3, 4]], 5, [6, 7]]
print(suma_lista_profunda(datos))  # Resultado: 28