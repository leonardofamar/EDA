class ListaOrdenadaSecuencial:
    def __init__(self, capacidad_maxima):
        self.capacidad = capacidad_maxima
        self.datos = [None] * capacidad_maxima
        self.tamaño = 0

    def esta_vacia(self):
        return self.tamaño == 0

    def esta_llena(self):
        return self.tamaño == self.capacidad

    def insertar(self, elemento):
        if self.esta_llena():
            print("Error: Lista llena")
            return

        # Encontrar la posición donde insertar el elemento para mantener el orden
        posicion = 0
        while posicion < self.tamaño and self.datos[posicion] < elemento:
            posicion += 1

        # Desplazar elementos a la derecha
        for i in range(self.tamaño, posicion, -1):
            self.datos[i] = self.datos[i - 1]

        self.datos[posicion] = elemento
        self.tamaño += 1

    def eliminar(self, elemento):
        posicion = self.buscar(elemento)
        if posicion == -1:
            print("Error: Elemento no encontrado")
            return

        # Desplazar elementos a la izquierda
        for i in range(posicion, self.tamaño - 1):
            self.datos[i] = self.datos[i + 1]

        self.tamaño -= 1

    def buscar(self, elemento):
        # Búsqueda binaria (opcional) ya que está ordenada
        inicio = 0
        fin = self.tamaño - 1
        while inicio <= fin:
            medio = (inicio + fin) // 2
            if self.datos[medio] == elemento:
                return medio
            elif self.datos[medio] < elemento:
                inicio = medio + 1
            else:
                fin = medio - 1
        return -1  # No encontrado

    def obtener(self, posicion):
        if posicion < 0 or posicion >= self.tamaño:
            print("Error: Posición inválida")
            return None
        return self.datos[posicion]

    def mostrar(self):
        print("Lista ordenada:", end=" ")
        for i in range(self.tamaño):
            print(self.datos[i], end=" ")
        print()
if __name__=="__main__":
    lista = ListaOrdenadaSecuencial(10)

lista.insertar(10)
lista.insertar(5)
lista.insertar(7)
lista.insertar(20)
lista.mostrar()  # Lista ordenada: 5 7 10 20

print("Buscar 10:", lista.buscar(10))  # 2

lista.eliminar(7)
lista.mostrar()  # Lista ordenada: 5 10 20

print("Elemento en posición 1:", lista.obtener(1))  # 10
