# Se define la estructura de los nodos.
class Nodo:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Generamos nuestra raiz
inicio = Nodo(1)

# Se definen  nodos inferiores

inicio.left = Nodo(2)

inicio.left.left = Nodo(4)
inicio.left.left.left = Nodo(7)
inicio.left.left.right = Nodo(8)

inicio.left.right = Nodo(5)
inicio.left.right.left = Nodo(9)


inicio.right = Nodo(3)

inicio.right = Nodo(6)
inicio.right.right = Nodo(10)
inicio.right.right.left = Nodo(11)
inicio.right.right.right = Nodo(12)


def print_tree(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print("    " * nivel + prefijo + str(nodo.val))
        print_tree(nodo.left, nivel + 1, "Izquierda: ")
        print_tree(nodo.right, nivel + 1, "Derecha: ")


print_tree(inicio)
