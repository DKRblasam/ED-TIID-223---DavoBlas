# Se define la estructura de los nodos.
class Nodo:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Generamos nuestra raiz
raiz = Nodo(1)

# Se definen hijos
raiz.left = Nodo(2)
raiz.right = Nodo(3)

raiz.left.left = Nodo(4)
raiz.left.right = Nodo(5)

raiz.right.left = Nodo(6)
raiz.right.right = Nodo(7)


def print_tree(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print("    " * nivel + prefijo + str(nodo.val))
        print_tree(nodo.left, nivel + 1, "Izquierda: ")
        print_tree(nodo.right, nivel + 1, "Derecha: ")


print_tree(raiz)
