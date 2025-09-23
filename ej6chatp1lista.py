class NodoBloque:
    def __init__(self, inicio, tamaño, libre=True, id_dato=None):
        self.inicio = inicio
        self.tamaño = tamaño
        self.libre = libre
        self.id = id_dato
        self.siguiente = None

class HeapSimulada:
    def __init__(self, tamaño_total):
        self.inicio = NodoBloque(0, tamaño_total, libre=True)

    def mostrar_estado(self):
        print("\n--- Estado de la memoria (única lista) ---")
        actual = self.inicio
        while actual:
            estado = "Libre" if actual.libre else f"Ocupado (ID: {actual.id})"
            print(f"[Inicio: {actual.inicio}, Tamaño: {actual.tamaño}, {estado}]")
            actual = actual.siguiente
        print("------------------------------------------\n")

    def almacenar(self, tamaño, id_dato):
        actual = self.inicio
        while actual:
            if actual.libre and actual.tamaño >= tamaño:
                # Caso exacto
                if actual.tamaño == tamaño:
                    actual.libre = False
                    actual.id = id_dato
                else:
                    # Dividir el bloque
                    nuevo = NodoBloque(
                        actual.inicio + tamaño,
                        actual.tamaño - tamaño,
                        libre=True
                    )
                    nuevo.siguiente = actual.siguiente

                    actual.tamaño = tamaño
                    actual.libre = False
                    actual.id = id_dato
                    actual.siguiente = nuevo
                print(f"Se almacenó '{id_dato}' en la dirección {actual.inicio} con tamaño {tamaño}.")
                return
            actual = actual.siguiente

        print(f"No hay suficiente espacio para almacenar '{id_dato}' (tamaño {tamaño}).")

    def liberar(self, id_dato):
        actual = self.inicio
        while actual:
            if not actual.libre and actual.id == id_dato:
                actual.libre = True
                actual.id = None
                self._fusionar()
                print(f"Se liberó el dato '{id_dato}'.")
                return
            actual = actual.siguiente
        print(f"No se encontró el dato '{id_dato}' para liberar.")

    def _fusionar(self):
        actual = self.inicio
        while actual and actual.siguiente:
            siguiente = actual.siguiente
            if actual.libre and siguiente.libre:
                # Fusionar los dos bloques libres
                actual.tamaño += siguiente.tamaño
                actual.siguiente = siguiente.siguiente
            else:
                actual = actual.siguiente
if __name__=="__main__":
    heap = HeapSimulada(100)

    heap.mostrar_estado()

    heap.almacenar(30, "A")
    heap.almacenar(20, "B")
    heap.almacenar(10, "C")

    heap.mostrar_estado()

    heap.liberar("B")
    heap.mostrar_estado()

    heap.almacenar(15, "D")
    heap.mostrar_estado()
