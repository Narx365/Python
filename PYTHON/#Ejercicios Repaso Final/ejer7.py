class Material:
    def __init__(self, id, titulo):
        self.id = id
        self.titulo = titulo

class Libro(Material):
    def __init__(self, id, titulo, paginas, autor):
        super().__init__(id, titulo)
        self.paginas = paginas
        self.autor = autor

class Revista(Material):
    def __init__(self, id, titulo, numero):
        super().__init__(id, titulo)
        self.numero = numero

materiales = []

while True:
    print("\n1 añadir material | 2 mostrar todas | 3 buscar por titulo | 4 eliminar | 5 mostrar libros con mas de 300 paginas")
    menu = int(input("dime que desea hacer: "))
    
    if menu == 1:
        tipo = input("¿Libro (L) o Revista (R)? ").upper()
        id_mat = int(input("ID: "))
        titulo = input("Título: ")
        
        if tipo == "L":
            paginas = int(input("Páginas: "))
            autor = input("Autor: ")
            material = Libro(id_mat, titulo, paginas, autor)
        elif tipo == "R":
            numero = int(input("Número: "))
            material = Revista(id_mat, titulo, numero)
        else:
            print("Opción no válida")
            continue
        
        materiales.append(material)
        print("Material añadido exitosamente")
    
    elif menu == 2:
        if not materiales:
            print("No hay materiales registrados")
        else:
            for material in materiales:
                if isinstance(material, Libro):
                    print(f"LIBRO - ID: {material.id}, Título: {material.titulo}, Autor: {material.autor}, Páginas: {material.paginas}")
                else:
                    print(f"REVISTA - ID: {material.id}, Título: {material.titulo}, Número: {material.numero}")
    
    elif menu == 3:
        titulo_buscar = input("Título a buscar: ")
        encontrados = [m for m in materiales if titulo_buscar.lower() in m.titulo.lower()]
        if encontrados:
            for material in encontrados:
                if isinstance(material, Libro):
                    print(f"LIBRO - ID: {material.id}, Título: {material.titulo}, Autor: {material.autor}, Páginas: {material.paginas}")
                else:
                    print(f"REVISTA - ID: {material.id}, Título: {material.titulo}, Número: {material.numero}")
        else:
            print("No se encontraron resultados")
    
    elif menu == 4:
        id_eliminar = int(input("ID del material a eliminar: "))
        materiales = [m for m in materiales if m.id != id_eliminar]
        print("Material eliminado (si existía)")
    
    elif menu == 5:
        libros_grandes = [m for m in materiales if isinstance(m, Libro) and m.paginas > 300]
        if libros_grandes:
            for libro in libros_grandes:
                print(f"LIBRO - ID: {libro.id}, Título: {libro.titulo}, Autor: {libro.autor}, Páginas: {libro.paginas}")
        else:
            print("No hay libros con más de 300 páginas")
    
    else:
        print("Opción no disponible")