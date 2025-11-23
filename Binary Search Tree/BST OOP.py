class Nodo: 
    def __init__(self, id, titulo, autor, año):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.izq = None
        self.der = None


class ArbolLibros:
    def __init__(self):
        self.raiz = None

    def insertar(self, id, titulo, autor, año):
        if self.raiz is None:
            self.raiz = Nodo(id, titulo, autor, año)
        else:
            self._insertar(self.raiz, id, titulo, autor, año)
    
    def _insertar(self, nodo, id, titulo, autor, año):
        if id < nodo.id:
            if nodo.izq is None:
                nodo.izq = Nodo(id, titulo, autor, año)
            else:
                self._insertar(nodo.izq, id, titulo, autor, año)
        
        elif id > nodo.id:
            if nodo.der is None:
                nodo.der = Nodo(id, titulo, autor, año)
            else:
                self._insertar(nodo.der, id, titulo, autor, año)

    def buscar(self, id):
        return self._buscar(self.raiz, id)
        
    def _buscar(self, nodo, id):
        if nodo is None:
            return False
        
        if id == nodo.id:
            return nodo
        
        elif id < nodo.id:
            return self._buscar(nodo.izq, id)
        else:
            return self._buscar(nodo.der, id)
        
    def mostrar(self, raiz):
        if raiz:
            print(f'{raiz.id} ',end="")
            self.mostrar(raiz.izq)
            self.mostrar(raiz.der)

arbol = ArbolLibros()

arbol.insertar(123456, "Don Quijote", "Miguel de Cervantes", 1605)
arbol.insertar(119987, "Historia de dos ciudades", "Dickens", 1859)
arbol.insertar(287651, "El Señor de los Anillos", "Tolkien", 1954)

arbol.mostrar(arbol.raiz)

# Llamamos la función buscar 

resultado = arbol.buscar(123456)
if resultado:
    print(f'\nLibro encontrado -> ID: {resultado.id}, título: "{resultado.titulo}", año: "{resultado.año}".')
else:
    print('Libro no encontrado')
