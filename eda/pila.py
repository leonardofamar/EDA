import numpy as np

class Pila:
    __cantidad: int
    __tope: int
    __arreglo: np.ndarray

    def __init__(self, cantidad=0):
        self.__cantidad = cantidad
        self.__tope = -1
        self.__arreglo = np.zeros(self.__cantidad, dtype=int)

    def vacia(self):
        if self.__tope == -1:
            return 0

    def insertar(self, x):
        if self.__tope < self.__cantidad - 1:
            self.__tope += 1
            self.__arreglo[self.__tope] = x
        else:
            return 0
        return x

    def suprimir(self):
        if self.vacia():
            print("Pila vacia")
            return 0
        else:
            self.__tope -= 1

    def mostrar(self):
        if self.vacia():
            print("Pila vacia")
        else:
             for i in range(self.__tope, -1, -1):
                print(int(self.__arreglo[i]))
    
def conversionabinario(num):
    pila = Pila(10)
    while num >= 2:
        resto = num % 2
        pila.insertar(resto)
        num = num // 2
    pila.insertar(num)
    print("El numero en binario es: ")
    pila.mostrar()


if __name__ == "__main__":
    print("Ingrese un numero entero a convertir: ")
    n = int(input())
    conversionabinario(n)
