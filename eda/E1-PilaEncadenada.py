class Celda:
    def __init__(self,elemento, sig):
        self.__elemento = elemento
        self.__sig = sig
        
    def obtener_elemento(self):
        return self.__elemento
    
    def cargar_elemento(self,elemento):
        self.__elemento = elemento
        
    def cargar_siguiente(self,tope):
        self.__sig = tope
        
    def obtener_siguiente(self):
        return self.__sig

class Pila_enc:
    __cant: int
    __tope: None
    
    def __init__(self,tope=None,cant=0):
        self.__cant = cant
        self.__tope = tope
        
    def vacia(self):
        return self.__cant == 0
    
    def insertar(self,x):
        nueva_celda = Celda(x,self.obtener_tope())
        self.cargar_tope(nueva_celda)
        self.aumentar_cantidad()
        
    def obtener_tope(self):
        return self.__tope
    
    def cargar_tope(self,dato):
        self.__tope = dato
        
    def aumentar_cantidad(self):
        self.__cant+=1
        
    def mostrar(self, aux=None):
        print("Estado actual de la pila:")
        if self.vacia():
            print("La pila está vacía")
        else:
            actual = self.__tope
            while actual is not None:
                if actual == self.__tope:
                    print(f"[ {actual.obtener_elemento()} ]  <-- tope")
                else:
                    print(f"[ {actual.obtener_elemento()} ]")
                actual = actual.obtener_siguiente()
        print("-" * 40)

    def suprimir(self):
        if self.vacia():
            return None
        else:
            self.cargar_tope(self.obtener_tope().obtener_siguiente()) 
            self.disminuir_cantidad()
            
    def disminuir_cantidad(self):
        self.__cant-=1
        
    def __len__(self):
        return self.__cant
        
if __name__=="__main__":
    pila_enc = Pila_enc()
    pila_enc.insertar(1)
    pila_enc.insertar(2)
    pila_enc.insertar(3)
    print(f"La pila tiene antes de suprimir {len(pila_enc)} elementos.")
    print("-" * 40)
    pila_enc.suprimir()
    pila_enc.mostrar(pila_enc.obtener_tope())
    print(f"La pila tiene despues de suprimir {len(pila_enc)} elementos.")
