from collections import deque

cola = deque(["Ana", "Carlos"])

cola.append("Jorge")
cola.append("Andres")

print ("cola actual: ", cola)


atendido = cola.popleft()

print (f"Se atendio a : {atendido}")
print ("cola restante: ", cola)

