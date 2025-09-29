class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
class ListaOrdenadaEncadenada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza is None

    def insertar(self, dato):
        nuevo = Nodo(dato)

        # Insertar al inicio si está vacía o el nuevo dato es menor que la cabeza
        if self.esta_vacia() or dato < self.cabeza.dato:
            nuevo.siguiente = self.cabeza
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            # Buscar la posición adecuada para mantener el orden
            while actual.siguiente is not None and actual.siguiente.dato < dato:
                actual = actual.siguiente
            # Insertar el nuevo nodo
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None

        while actual is not None and actual.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Error: Elemento no encontrado")
            return

        if anterior is None:
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None and actual.dato <= dato:
            if actual.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  # No encontrado

    def obtener(self, posicion):
        actual = self.cabeza
        index = 0
        while actual is not None:
            if index == posicion:
                return actual.dato
            actual = actual.siguiente
            index += 1
        print("Error: Posición inválida")
        return None

    def mostrar(self):
        actual = self.cabeza
        print("Lista ordenada:", end=" ")
        while actual is not None:
            print(actual.dato, end=" -> ")
            actual = actual.siguiente
        print("None")
if __name__=="__main__":
    lista = ListaOrdenadaEncadenada()

lista.insertar(10)
lista.insertar(5)
lista.insertar(7)
lista.insertar(20)
lista.mostrar()  # Lista ordenada: 5 -> 7 -> 10 -> 20 -> None

print("Buscar 10:", lista.buscar(10))  # 2

lista.eliminar(7)
lista.mostrar()  # Lista ordenada: 5 -> 10 -> 20 -> None

print("Elemento en posición 1:", lista.obtener(1))  # 10
