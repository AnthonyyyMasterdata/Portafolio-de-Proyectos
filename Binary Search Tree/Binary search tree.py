class Libro:
    def __init__(self, id=None, titulo=None, autor=None, año=None, izq=None, der=None):
        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.año = año
        self.izq = izq
        self.der = der 

# Construir la función que permita insertar un nuevo libro al arbol. 

def Insertar(arbol, id, titulo, autor, año):
    # Verificamos si el arbol esta vacio
    if arbol is None:
        return Libro(id, titulo, autor, año)
    
    # Si el id es menor: insertar subarbol izquierdo
    if id < arbol.id:
        arbol.izq = Insertar(arbol.izq, id, titulo, autor, año)

    # Si el id es mayor: insertar subarbol derecho
    elif id > arbol.id:
        arbol.der = Insertar(arbol.der, id, titulo, autor, año)

    # Si el ID ya existe -> no hacer nada 
    else:
        print(f'El id {id} ya existe')

    return arbol

def buscar(a, id): # Buscamos libros por su ID. Retonar objeto libro o False si no existe.

    # Verificamos que el arbol no este vacío. 
    if a is None:
        return False
    
    # Verificamos que el id del libro es igual al id del nodo
    if id == a.id:
        return a
    
    # Si el id es mayor: buscar subarbol izquierdo
    elif id < a.id:
        return buscar(a.izq, id)
    
    # Si el ID es menor: buscar subarbol derecho
    else:
        return buscar(a.der, id)

# Llamamos la función 
arbol = None 

# Insertamos los nodos
arbol = Insertar(arbol, 123456, "Don Quijote de La Mancha", "Miguel de Cervantes", 1605)
arbol = Insertar(arbol, 119987, "Historia de dos ciudades", "Charles Dickens", 1859)
arbol = Insertar(arbol, 287651, "El Señor de los Anillos", "J.R.R. Tolkien", 1954)
arbol = Insertar(arbol, 176539, "El Principito", "Antoine de Saint-Exupery", 1943)
arbol = Insertar(arbol, 276539, "El Hobbit", "J.R.R. Tolkien", 1937)
arbol = Insertar(arbol, 187600, "Sueño en el pabellon rojo", "Cao Xueqin", 1792)
arbol = Insertar(arbol, 253617, "Las aventuras de Alicia en el pais de las maravillas", "Lewis Carroll", 1865)
arbol = Insertar(arbol, 117766, "Diez negritos", "Agatha Christie", 1939)
arbol = Insertar(arbol, 251982, "El leon la bruja y el ropero", "C.S. Lewis", 1950)
arbol = Insertar(arbol, 138754, "Ella", "H. Rider Haggard", 1887)
arbol = Insertar(arbol, 328976, "El codigo Da Vinci", "Dan Brown", 2003)
arbol = Insertar(arbol, 266678, "El Guardian entre el Centeno", "J. D. Salinger", 1951)
arbol = Insertar(arbol, 289567, "El alquimista", "Paulo Coelho", 2000)
arbol = Insertar(arbol, 154506, "El camino a Cristo", "Ellen G. White", 1892)
arbol = Insertar(arbol, 200721, "Heidi", "Johanna Spyri", 1880)
arbol = Insertar(arbol, 234556, "Azabache", "Anna Sewell", 1877)
arbol = Insertar(arbol, 119342, "El nombre de la rosa", "Umberto Eco", 1982)


def mostrar(a):
    if a:
        print(f'{a.id} ',end="")
        mostrar(a.izq)
        mostrar(a.der)

# Llamos la funcion mostrar
mostrar(arbol)

# Llamamos la funcion buscar
resultado = buscar(arbol, 117766)
if resultado:   
    print(f'\nLibro encontrado -> ID: {resultado.id}, título: "{resultado.titulo}", año: "{resultado.año}".')
else:
    print('\nLibro no encontrado')

