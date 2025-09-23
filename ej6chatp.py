class NodoBloque:
    def __init__(self, inicio, tamaño):
        self.inicio = inicio
        self.tamaño = tamaño
        self.siguiente = None


class HeapEncadenada:
    def __init__(self, tamaño_total):
        self.inicio = NodoBloque(0, tamaño_total)  
        self.ocupados = []  

    def mostrar_estado(self):
        print("\n--- Estado de la memoria ---")
        print("Bloques libres:")
        nodo = self.inicio
        while nodo:
            print(f"  [Inicio: {nodo.inicio}, Tamaño: {nodo.tamaño}]")
            nodo = nodo.siguiente

        print("Bloques ocupados:")
        for bloque in self.ocupados:
            print(f"  [ID: {bloque['id']}, Inicio: {bloque['inicio']}, Tamaño: {bloque['tamaño']}]")
        print("----------------------------\n")

    def almacenar(self, tamaño, id_dato):
        anterior = None
        actual = self.inicio

        while actual:
            if actual.tamaño >= tamaño:
                inicio = actual.inicio
                self.ocupados.append({"id": id_dato, "inicio": inicio, "tamaño": tamaño})

                if actual.tamaño == tamaño:
                    # Eliminar nodo de la lista libre
                    if anterior:
                        anterior.siguiente = actual.siguiente
                    else:
                        self.inicio = actual.siguiente
                else:
                    # Ajustar nodo actual
                    actual.inicio += tamaño
                    actual.tamaño -= tamaño

                print(f"Se almacenó '{id_dato}' en la dirección {inicio} con tamaño {tamaño}.")
                return

            anterior = actual
            actual = actual.siguiente

        print(f"No hay suficiente espacio para almacenar '{id_dato}' (tamaño {tamaño}).")

    def liberar(self, id_dato):
        for i, bloque in enumerate(self.ocupados):
            if bloque["id"] == id_dato:
                nuevo = NodoBloque(bloque["inicio"], bloque["tamaño"])
                self._insertar_y_fusionar(nuevo)
                self.ocupados.pop(i)
                print(f"Se liberó el dato '{id_dato}'.")
                return

        print(f"No se encontró el dato '{id_dato}' para liberar.")

    def _insertar_y_fusionar(self, nuevo_bloque):
        if self.inicio is None or nuevo_bloque.inicio < self.inicio.inicio:
            nuevo_bloque.siguiente = self.inicio
            self.inicio = nuevo_bloque
        else:
            actual = self.inicio
            while actual.siguiente and actual.siguiente.inicio < nuevo_bloque.inicio:
                actual = actual.siguiente
            nuevo_bloque.siguiente = actual.siguiente
            actual.siguiente = nuevo_bloque

        # Fusionar bloques contiguos
        self._fusionar()

    def _fusionar(self):
        actual = self.inicio
        while actual and actual.siguiente:
            siguiente = actual.siguiente
            if actual.inicio + actual.tamaño == siguiente.inicio:
                actual.tamaño += siguiente.tamaño
                actual.siguiente = siguiente.siguiente
            else:
                actual = actual.siguiente

if __name__=="__main__":

    heap = HeapEncadenada(100)
    heap.mostrar_estado()

    heap.almacenar(25, "A")
    heap.almacenar(30, "B")
    heap.almacenar(10, "C")

    heap.mostrar_estado()

    heap.liberar("B")

    heap.mostrar_estado()

    heap.almacenar(20, "D")
    heap.almacenar(15, "E")

    heap.mostrar_estado()
