from listaEnc import ListaEncadenada

le=ListaEncadenada()
le2=ListaEncadenada()
lesuma=ListaEncadenada()

def cargar(lista,orden):
    i=0
    j=0
    for i in range(orden):
        for j in range(orden):
         dato=int(input(f"ingrese el dato de la fila: {i} columna: {j} dato:"))
         lista.insertar_al_final(dato,i,j)
    lista.mostrar()
def sumar(lista_resultado, lista1, lista2):
    actual1 = lista1.cabeza
    actual2 = lista2.cabeza

    while actual1 is not None and actual2 is not None:
        suma = actual1.obtener_elemento() + actual2.obtener_elemento()
        print(f"le: {actual1.obtener_elemento()} le2: {actual2.obtener_elemento()}")

        # Insertamos en la lista resultado, con la posición correspondiente
        lista_resultado.insertar_al_final(
            suma,
            actual1.celda.fila,
            actual1.celda.columna
        )

        # Avanzamos en ambas listas
        actual1 = actual1.obtener_siguiente()
        actual2 = actual2.obtener_siguiente()

    lista_resultado.mostrar()

if __name__=="__main__":
    orden=int(input("ingrese orden de la matriz cuadrada: "))
    cargar(le,orden)
    cargar(le2,orden)
    sumar(lesuma,le,le2)