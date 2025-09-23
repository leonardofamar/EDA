class dato:
    def __init__(self,coeficiente,exponente):
        self.coeficiente=coeficiente
        self.exponente=exponente
    def getCo(self):
        return self.coeficiente
    def getExp(self):
        return self.exponente

class celda:
    def __init__(self,c,e):
        self.celda = dato(c,e)
        self.siguiente = None
    def obtenerCo(self):
        return self.celda.getCo()
    def obtenerExp(self):
        return self.celda.getExp()
        
    def cargar_siguiente(self,tope):
        self.siguiente = tope
        
    def obtener_siguiente(self):
        return self.siguiente
    def set_siguiente(self,sig):
        self.siguiente=sig

class lista5:
    def __init__(self):
        self.cabeza = None 

    def esta_vacia(self):
        return self.cabeza is None
    def obtenerCo(self):
        return self.celda.getCo()
    def obtenerExp(self):
        return self.celda.getExp()
    def insertar_al_inicio(self,c,e):
        nuevo = celda(c,e)
        nuevo.siguiente = self.cabeza
        self.cabeza = nuevo

    def insertar_al_final(self,c,e):
        nuevo = celda(c,e)
        if self.esta_vacia():
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo

    def mostrar(self):
        actual = self.cabeza
        polinomio_str = ""
        while actual is not None:
            coef = actual.obtenerCo()
            exp = actual.obtenerExp()
            if exp == 0:
                termino = f"{coef}"
            elif exp == 1:
                termino = f"{coef}x"
            else:
                termino = f"{coef}x^{exp}"

            if polinomio_str == "":
                polinomio_str = termino
            else:
                if coef >= 0:
                    polinomio_str += " + " + termino
                else:
                    polinomio_str += " - " + str(abs(coef)) + ("x" if exp > 0 else "")

            actual = actual.obtener_siguiente()

        print(polinomio_str if polinomio_str != "" else "0")
"""def sumar(poli1,poli2,poliRes):
    p1=poli1.cabeza
    p2=poli2.cabeza
    
    while p1 is not None and p2 is not None:

        if p1  is None:
            poliRes.insertar_al_final(p2.obtenerCo(),p2.obtenerExp())
            p1=p1.obtener_siguiente()
        elif p2  is None:
            poliRes.insertar_al_final(p1.obtenerCo(),p1.obtenerExp())
            p2=p2.obtener_siguiente()
        elif p1.obtenerExp()== p2.obtenerExp():
            suma=p1.obtenerCo()+p2.obtenerCo()
            poliRes.insertar_al_final(suma,p1.obtenerExp())
            p1=p1.obtener_siguiente()
            p2=p2.obtener_siguiente()
        print(f"{suma}")"""
def sumar(poli1, poli2, poliRes):
    p1 = poli1.cabeza
    p2 = poli2.cabeza

    while p1 is not None and p2 is not None:
        if p1.obtenerExp() == p2.obtenerExp():
            suma = p1.obtenerCo() + p2.obtenerCo()
            if suma != 0: 
                poliRes.insertar_al_final(suma, p1.obtenerExp())
            p1 = p1.obtener_siguiente()
            p2 = p2.obtener_siguiente()
        elif p1.obtenerExp() > p2.obtenerExp():
            poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
            p1 = p1.obtener_siguiente()
        else: 
            poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
            p2 = p2.obtener_siguiente()

    while p1 is not None:
        poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
        p1 = p1.obtener_siguiente()

    while p2 is not None:
        poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
        p2 = p2.obtener_siguiente()
def restar(poli1, poli2, poliRes):
    p1 = poli1.cabeza
    p2 = poli2.cabeza

    while p1 is not None and p2 is not None:
        if p1.obtenerExp() == p2.obtenerExp():
            suma = p1.obtenerCo() - p2.obtenerCo()
            if suma != 0: 
                poliRes.insertar_al_final(suma, p1.obtenerExp())
            p1 = p1.obtener_siguiente()
            p2 = p2.obtener_siguiente()
        elif p1.obtenerExp() > p2.obtenerExp():
            poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
            p1 = p1.obtener_siguiente()
        else: 
            poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
            p2 = p2.obtener_siguiente()

    while p1 is not None:
        poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
        p1 = p1.obtener_siguiente()

    while p2 is not None:
        poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
        p2 = p2.obtener_siguiente()
def multiplicar(poli1, poli2, poliRes):
    p1 = poli1.cabeza
    p2 = poli2.cabeza

    while p1 is not None and p2 is not None:
        if p1.obtenerExp() == p2.obtenerExp():
            suma = p1.obtenerCo() * p2.obtenerCo()
            if suma != 0: 
                poliRes.insertar_al_final(suma, p1.obtenerExp())
            p1 = p1.obtener_siguiente()
            p2 = p2.obtener_siguiente()
        elif p1.obtenerExp() > p2.obtenerExp():
            poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
            p1 = p1.obtener_siguiente()
        else: 
            poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
            p2 = p2.obtener_siguiente()

    while p1 is not None:
        poliRes.insertar_al_final(p1.obtenerCo(), p1.obtenerExp())
        p1 = p1.obtener_siguiente()

    while p2 is not None:
        poliRes.insertar_al_final(p2.obtenerCo(), p2.obtenerExp())
        p2 = p2.obtener_siguiente()
                                
    

if __name__=="__main__":
    poliResultado=lista5()
    poli1=lista5()
    poli2=lista5()
    poli1.insertar_al_final(2,4)
    poli1.insertar_al_final(2,3)
    poli1.insertar_al_final(3,2)
    poli1.insertar_al_final(2,1)
    poli2.insertar_al_final(3,3)
    poli2.insertar_al_final(3,2)
    poli2.insertar_al_final(3,1)
    #sumar(poli1,poli2,poliResultado)
    #restar(poli1,poli2,poliResultado)
    multiplicar(poli1,poli2,poliResultado)
    poliResultado.mostrar()