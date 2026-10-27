
class Nodo:
    def __init__(self, numero):
        # Valor que tendrá el nodo
        self.numero = numero
        self.next = None


class Listlink:
    def __init__(self):
        self.head = None

    def insertLeft(self, num):
        # Se define el nuevo nodo
        newnodo = Nodo(num)

        # Si la lista está vacía, será el primer nodo
        if self.head is None:
            self.head = newnodo
            return

        # El nuevo nodo apunta al primer nodo actual
        newnodo.next = self.head

        # El nuevo nodo se convierte en la cabeza
        self.head = newnodo

    def insertRight(self, num):
        # Se define el nuevo nodo
        newNodo = Nodo(num)

        # Si la lista está vacía
        if self.head is None:
            self.head = newNodo
            return

        # Referencia al primer nodo
        actual = self.head

        # Recorrer hasta el último nodo
        while actual.next is not None:
            actual = actual.next

        # Enlazar el último nodo con el nuevo
        actual.next = newNodo

    def printList(self):
        # Referencia temporal
        actual = self.head

        # Recorrer e imprimir la lista
        while actual is not None:
            print(actual.numero, "→", end=" ")
            actual = actual.next

        print("None")


# Crear la lista enlazada
My_list = Listlink()

My_list.insertRight(2)
My_list.insertRight(3)
My_list.insertRight(4)
My_list.insertRight(5)
My_list.insertRight(6)

My_list.printList()
