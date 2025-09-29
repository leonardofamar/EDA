class NodoAVL:
    def __init__(self, clave):
        self.clave = clave
        self.izq = None
        self.der = None
        self.altura = 1

class AVL:
    def __init__(self):
        self.raiz = None

    # Obtener altura del nodo
    def _altura(self, nodo):
        return nodo.altura if nodo else 0

    # Obtener factor de balance
    def _balance(self, nodo):
        if not nodo:
            return 0
        return self._altura(nodo.izq) - self._altura(nodo.der)

    # Rotación derecha
    def _rot_der(self, y):
        x = y.izq
        T2 = x.der

        x.der = y
        y.izq = T2

        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))
        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))

        return x

    # Rotación izquierda
    def _rot_izq(self, x):
        y = x.der
        T2 = y.izq

        y.izq = x
        x.der = T2

        x.altura = 1 + max(self._altura(x.izq), self._altura(x.der))
        y.altura = 1 + max(self._altura(y.izq), self._altura(y.der))

        return y

    # Inserción
    def _insertar(self, nodo, clave):
        if not nodo:
            return NodoAVL(clave)

        if clave < nodo.clave:
            nodo.izq = self._insertar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._insertar(nodo.der, clave)
        else:
            return nodo  # no se permiten duplicados

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Casos de desequilibrio
        if balance > 1 and clave < nodo.izq.clave:
            return self._rot_der(nodo)

        if balance < -1 and clave > nodo.der.clave:
            return self._rot_izq(nodo)

        if balance > 1 and clave > nodo.izq.clave:
            nodo.izq = self._rot_izq(nodo.izq)
            return self._rot_der(nodo)

        if balance < -1 and clave < nodo.der.clave:
            nodo.der = self._rot_der(nodo.der)
            return self._rot_izq(nodo)

        return nodo

    def insertar(self, clave):
        self.raiz = self._insertar(self.raiz, clave)

    # Obtener el nodo con la clave mínima
    def _min_valor(self, nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual

    # Eliminación
    def _eliminar(self, nodo, clave):
        if not nodo:
            return nodo

        if clave < nodo.clave:
            nodo.izq = self._eliminar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self._eliminar(nodo.der, clave)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            temp = self._min_valor(nodo.der)
            nodo.clave = temp.clave
            nodo.der = self._eliminar(nodo.der, temp.clave)

        nodo.altura = 1 + max(self._altura(nodo.izq), self._altura(nodo.der))
        balance = self._balance(nodo)

        # Rebalancear si es necesario
        if balance > 1 and self._balance(nodo.izq) >= 0:
            return self._rot_der(nodo)

        if balance > 1 and self._balance(nodo.izq) < 0:
            nodo.izq = self._rot_izq(nodo.izq)
            return self._rot_der(nodo)

        if balance < -1 and self._balance(nodo.der) <= 0:
            return self._rot_izq(nodo)

        if balance < -1 and self._balance(nodo.der) > 0:
            nodo.der = self._rot_der(nodo.der)
            return self._rot_izq(nodo)

        return nodo

    def eliminar(self, clave):
        self.raiz = self._eliminar(self.raiz, clave)

    # Recorrido in-order (corregido)
    def _in_order(self, nodo):
        if nodo:
            self._in_order(nodo.izq)
            print(nodo.clave, end=' ')
            self._in_order(nodo.der)

    def in_order(self):
        self._in_order(self.raiz)

    # Imprimir estructura del árbol
    def imprimir(self, nodo=None, nivel=0, prefijo="Raíz: "):
        if nodo is None and nivel == 0:
            nodo = self.raiz
        if nodo is not None:
            print(" " * (nivel * 4) + prefijo + str(nodo.clave))
            if nodo.izq or nodo.der:
                if nodo.izq:
                    self.imprimir(nodo.izq, nivel + 1, "Izq: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "Izq: None")
                if nodo.der:
                    self.imprimir(nodo.der, nivel + 1, "Der: ")
                else:
                    print(" " * ((nivel + 1) * 4) + "Der: None")


if __name__ == "__main__":

    avl = AVL()

    # Inserciones
    for clave in [8,6,1,2,5,4,3,7,9,14,15,11]:
        avl.insertar(clave)

    print("Árbol tras inserciones:")
    avl.imprimir()

    # Eliminaciones
    for clave in [4, 8, 6, 5, 2, 1, 7]:
        print(f"\nEliminando {clave}...")
        avl.eliminar(clave)
        avl.imprimir()

    print("\nRecorrido in-order final:")
    avl.in_order()
    print()
