def factorial(n):
    # Caso base: el factorial de 0 (y de 1) es 1
    if n == 0:
        return 1
    
    # Caso recursivo: n multiplicado por el factorial del número anterior
    return n * factorial(n - 1)

print(factorial(5))
# Internamente hace: 5 * (4 * (3 * (2 * (1 * 1)))) = 120