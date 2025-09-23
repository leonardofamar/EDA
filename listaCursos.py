MAX = 100
NULL = -1

class ListaConCursor:
    def __init__(self):
        self.nodos = [{'dato': None, 'siguiente': i + 1} for i in range(MAX)]
        self.nodos[MAX - 1]['siguiente'] = NULL  # Último apunta a NULL
        self.inicio = NULL
        self.libre = 0  # Primer nodo libre

    def obtener_nodo_libre(self):
        if self.libre == NULL:
            return NULL
        nuevo = self.libre
        self.libre = self.nodos[nuevo]['siguiente']
        return nuevo

    def liberar_nodo(self, indice):
        self.nodos[indice]['siguiente'] = self.libre
        self.nodos[indice]['dato'] = None
        self.libre = indice

    def insertar_inicio(self, valor):
        nuevo = self.obtener_nodo_libre()
        if nuevo == NULL:
            print("Error: lista llena.")
            return
        self.nodos[nuevo]['dato'] = valor
        self.nodos[nuevo]['siguiente'] = self.inicio
        self.inicio = nuevo

    def mostrar(self):
        actual = self.inicio
        elementos = []
        while actual != NULL:
            elementos.append(self.nodos[actual]['dato'])
            actual = self.nodos[actual]['siguiente']
        print(" -> ".join(map(str, elementos)) + " -> NULL")

    def eliminar(self, valor):
        actual = self.inicio
        anterior = NULL

        while actual != NULL and self.nodos[actual]['dato'] != valor:
            anterior = actual
            actual = self.nodos[actual]['siguiente']

        if actual == NULL:
            print("Elemento no encontrado.")
            return

        if anterior == NULL:
            self.inicio = self.nodos[actual]['siguiente']
        else:
            self.nodos[anterior]['siguiente'] = self.nodos[actual]['siguiente']

        self.liberar_nodo(actual)

    def buscar(self, valor):
        actual = self.inicio
        while actual != NULL:
            if self.nodos[actual]['dato'] == valor:
                return actual
            actual = self.nodos[actual]['siguiente']
        return NULL

    def esta_vacia(self):
        return self.inicio == NULL

if __name__ == "__main__":
    lista = ListaConCursor()
    lista.insertar_inicio(10)
    lista.insertar_inicio(20)
    lista.insertar_inicio(30)
    lista.mostrar()  # 30 -> 20 -> 10 -> NULL

    lista.eliminar(20)
    lista.mostrar()  # 30 -> 10 -> NULL

    print("¿Está vacía?", lista.esta_vacia())  # False

    pos = lista.buscar(10)
    print(f"Elemento 10 encontrado en índice {pos}" if pos != NULL else "No encontrado")
