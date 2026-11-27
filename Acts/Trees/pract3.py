class Nodo:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def print_tree(nodo, nivel=0, prefijo="Raiz: "):
    if nodo is not None:
        print(" " * nivel + prefijo + str(nodo.val))
        print_tree(nodo.left, nivel + 1, "Izquierda: ")
        print_tree(nodo.right, nivel + 1, "Derecha: ")


def main():
    print("Programa de arboles binarios.\n")

    inicio = Nodo(int(input("Ingresa el valor de la raiz: ")))
    actual = inicio

    while True:
        print("\nNodo actual:", actual.val)
        print("\n1. Agregar a la izquierda")
        print("2. Agregar a la derecha")
        print("3. Siguiente nodo")
        print("4. Terminar")

        opcion = input("\nSelecciona una opcion: ")

        if opcion == "1":
            if actual.left is None:
                valor = int(input("Ingresa el valor del nodo izquierdo: "))
                actual.left = Nodo(valor)
                print("Nodo agregado correctamente.")
            else:
                print("Ya existe un nodo a la izquierda.")

        elif opcion == "2":
            if actual.right is None:
                valor = int(input("Ingresa el valor del nodo derecho: "))
                actual.right = Nodo(valor)
                print("Nodo agregado correctamente.")
            else:
                print("Ya existe un nodo a la derecha.")

        elif opcion == "3":
            print("\n1. Ir al nodo izquierdo")
            print("2. Ir al nodo derecho")

            direccion = input("Selecciona una direccion: ")

            if direccion == "1" and actual.left is not None:
                actual = actual.left
            elif direccion == "2" and actual.right is not None:
                actual = actual.right
            else:
                print("No existe un nodo en esa direccion.")

        elif opcion == "4":
            break

        else:
            print("Opcion no valida.")

    print("\nEl arbol generado es:\n")
    print_tree(inicio)


main()
