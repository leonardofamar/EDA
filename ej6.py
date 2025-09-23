import random
from EJ6LISTA import ListaEncadenada
lista=ListaEncadenada()

def buscar(tam,dato):
    while lista.cabeza is not None:
            if lista.getEsp()==tam: 
                lista.cabeza.cargar_elemento(dato)
                 
                
if __name__=="__main__":
    tamaño=int(input("ingrese el espacio que se necesita: "))
    dato=int(input("ingrese el dato: "))
    buscar(tamaño,dato)
"""cosas del parcial
pila secuencial, encadenada
cola,secuencial,encadenada,circular
lista secuencial y encadenada por posicion,secuencial y encadenada ordenada,cursor"""

"""
Insertar
Eliminar
Buscar -solo en las listas-
Recorrer 
 va todo implementar metodos y luego seguro va simulacion de cola y algun ejercicio de las cosas
no teoria
"""