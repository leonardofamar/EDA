class datoEsp:
    def __init__(self,dato,esp):
        self.dato=dato
        self.espacio=esp
    def getEsp(self):
        return self.getEsp()

class Celda:
    def __init__(self,dato,esp):
        self.celda = datoEsp(dato,esp)
        self.siguiente = None
    def obtener_elemento(self):
        return self.getDato()
    def getEsp(self):
        return self.getEsp()
    def cargar_elemento(self,elemento):
        self.celda = elemento
        
    def cargar_siguiente(self,tope):
        self.__siguiente = tope
        
    def obtener_siguiente(self):
        return self.__siguiente
    def set_siguiente(self,sig):
        self.__siguiente=sig

    
class ListaEncadenada:
    def __init__(self):
        self.cabeza = None 

    def esta_vacia(self):
        return self.cabeza is None
    def obtenerelem(self):
        return Celda.obtener_elemento()

    def insertar_al_inicio(self, dato,esp):
        nuevo = Celda(dato,esp)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self,dato,esp):
        nuevo = Celda(dato,esp)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def eliminar(self, dato):
        actual = self.cabeza
        anterior = None
        while actual is not None and actual.celda.dato != dato:
            anterior = actual
            actual = actual.siguiente

        if actual is None:
            print("Elemento no encontrado")
            return

        if anterior is None:
            # El elemento está en la cabeza
            self.cabeza = actual.siguiente
        else:
            anterior.siguiente = actual.siguiente

    def buscar(self, dato):
        actual = self.cabeza
        posicion = 0
        while actual is not None:
            if actual.celda.dato == dato:
                return posicion
            actual = actual.siguiente
            posicion += 1
        return -1  

    def obtener(self, posicion):
        actual = self.cabeza
        index = 0
        while actual is not None:
            if index == posicion:
                return actual.celda.dato
            actual = actual.siguiente
            index += 1
        print("Posición inválida")
        return None

    def mostrar(self):
        actual = self.cabeza
        print("Lista:", end=" ")
        while actual is not None:
            print(actual.celda.dato, end=" -> ")
            print(actual.celda.espacio, end=" -> ")
            actual = actual.siguiente
        print("None")
