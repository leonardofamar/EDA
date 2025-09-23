class CeldaRala:
    def __init__(self, dato,fila,columna):
        self.dato = dato
        self.fila=fila
        self.columna=columna
    def mostrar(self):
        print(f"dato:{self.dato},Fila{self.fila}Columna:{self.columna}")
    def getDato(self):
        return self.dato
class Celda:
    def __init__(self,celda,f,c):
        self.celda = CeldaRala(celda,f,c)
        self.siguiente = None
    def obtener_elemento(self):
        return self.celda.getDato()
    
    def cargar_elemento(self,elemento):
        self.celda = elemento
        
    def cargar_siguiente(self,tope):
        self.siguiente = tope
        
    def obtener_siguiente(self):
        return self.siguiente
    def set_siguiente(self,sig):
        self.siguiente=sig

    
class ListaEncadenada:
    def __init__(self):
        self.cabeza = None 

    def esta_vacia(self):
        return self.cabeza is None
    def obtenerelem(self):
        return self.cabeza.obtener_elemento()

    def insertar_al_inicio(self, dato,f,c):
        nuevo = Celda(dato,f,c)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self, dato,f,c):
        nuevo = Celda(dato,f,c)
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
            actual = actual.siguiente
        print("None")

#if __name__ == "__main__":
 #   lista = ListaEncadenada()
    
#lista.insertar_al_inicio(10)
#lista.insertar_al_inicio(20)
#lista.insertar_al_inicio(5)
#lista.mostrar()  

#print("Buscar 10:", lista.buscar(10))  
#print("Elemento en posición 2:", lista.obtener(1))  

#lista.eliminar(10)
#lista.mostrar()  