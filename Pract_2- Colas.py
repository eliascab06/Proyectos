class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


from abc import ABC, abstractmethod

class QueueInterface(ABC):

    @abstractmethod
    def size(self):
        """Devuelve el número de elementos en la cola"""
        pass

    @abstractmethod
    def is_empty(self):
        """Verifica si la cola está vacía"""
        pass

    @abstractmethod
    def front(self):
        """Devuelve el primer elemento sin eliminarlo"""
        pass

    @abstractmethod
    def enqueue(self, info):
        """Agrega un nuevo elemento a la cola"""
        pass

    @abstractmethod
    def dequeue(self):
        """Devuelve y elimina el primer elemento de la cola"""
        pass

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def set_next(self, next_node):
        self.next = next_node


def print_nodes(top):
    node = top
    while node is not None:
        # Aquí puedes imprimir la información del nodo
        # Asumiendo que node.data es un objeto Order
        node.data.print()
        node = node.get_next()


if __name__ == "__main__":
    # Creamos algunos pedidos
    order1 = Order(5, "Alice")
    order2 = Order(3, "Bob")
    order3 = Order(7, "Charlie")

    # Creamos los nodos
    n1 = Node(order1)
    n2 = Node(order2)
    n3 = Node(order3)

    # Enlazamos los nodos
    n1.set_next(n2)
    n2.set_next(n3)

    # Recorremos e imprimimos
    print("Lista de pedidos:")
    print_nodes(n1)
