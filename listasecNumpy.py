import numpy as np

class ListaSecuencial:
    def __init__(self, capacidad_maxima):
        self.capacidad = capacidad_maxima
        self.datos = np.empty(capacidad_maxima, dtype=int)  # Arreglo de enteros
        self.tamaño = 0  # Elementos actualmente en la lista

    def esta_vacia(self):
        return self.tamaño == 0

    def esta_llena(self):
        return self.tamaño == self.capacidad

    def insertar(self, elemento, posicion):
        if self.esta_llena():
            print("Error: La lista está llena")
            return
        if posicion < 0 or posicion > self.tamaño:
            print("Error: Posición inválida")
            return
        
        # Desplazar elementos hacia la derecha
        for i in range(self.tamaño, posicion, -1):
            self.datos[i] = self.datos[i - 1]

        self.datos[posicion] = elemento
        self.tamaño += 1

    def eliminar(self, posicion):
        if self.esta_vacia():
            print("Error: La lista está vacía")
            return
        if posicion < 0 or posicion >= self.tamaño:
            print("Error: Posición inválida")
            return

        # Desplazar elementos hacia la izquierda
        for i in range(posicion, self.tamaño - 1):
            self.datos[i] = self.datos[i + 1]

        self.tamaño -= 1  # Solo "olvidamos" el último elemento

    def buscar(self, elemento):
        for i in range(self.tamaño):
            if self.datos[i] == elemento:
                return i
        return -1  # No encontrado

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamaño:
            print("Error: Posición inválida")
            return None
        return self.datos[posicion]

    def mostrar(self):
        print("Lista:", end=" ")
        for i in range(self.tamaño):
            print(self.datos[i], end=" ")
        print()
if __name__=="__main__":
    lista = ListaSecuencial(5)

lista.insertar(10, 0)
lista.insertar(20, 1)
lista.insertar(15, 1)
lista.mostrar()  # Lista: 10 15 20

print("Buscar 15:", lista.buscar(15))  # 1

lista.eliminar(1)
lista.mostrar()  # Lista: 10 20

print("Elemento en posición 1:", lista.obtener(1))  # 20

