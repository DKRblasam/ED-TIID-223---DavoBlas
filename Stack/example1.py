# Crear pila vacia

historial = []

# Añadir elementos (Push)
historial.append("google.com")
historial.append("youtube.com")
historial.append("github.com")

print("Historial: ", historial)

# Vel el elemento superior
pagina_actual = historial[2]
print("pagina actual: ", pagina_actual)

# Eliminar el ultimo elemento (Pop)

pagina_salida = historial.pop()
print("Saliento de: ", pagina_salida)

