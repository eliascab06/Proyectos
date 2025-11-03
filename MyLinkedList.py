# MyLinkedList.py
# Implementación propia de una lista enlazada (Linked List)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def append(self, data):
        """Agrega un nuevo nodo al final de la lista."""
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def prepend(self, data):
        """Agrega un nuevo nodo al inicio de la lista."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete(self, data):
        """Elimina el primer nodo que contenga el valor especificado."""
        if self.is_empty():
            print("La lista está vacía.")
            return

        # Si el nodo a eliminar es la cabeza
        if self.head.data == data:
            self.head = self.head.next
            return

        # Buscar el nodo previo al que se quiere eliminar
        current = self.head
        while current.next and current.next.data != data:
            current = current.next

        if current.next is None:
            print(f"El valor '{data}' no se encontró en la lista.")
        else:
            current.next = current.next.next

    def search(self, data):
        """Busca un valor en la lista y devuelve True si lo encuentra."""
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        """Muestra todos los elementos de la lista."""
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Lista vacía.")

    def length(self):
        """Devuelve la longitud (número de nodos) de la lista."""
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count
