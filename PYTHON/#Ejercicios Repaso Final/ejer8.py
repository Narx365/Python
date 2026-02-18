class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.notas = []

    def agregar_nota(self, nota):
        self.notas.append(nota)

    def calcular_media(self):
        return sum(self.notas) / len(self.notas) if self.notas else 0

class Profesor(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad)
        self.asignaturas = [] # Lista de strings

    def agregar_asignatura(self, asig):
        self.asignaturas.append(asig)

escuela = [] # Lista mixta de alumnos y profesores

# Datos precargados para probar
a1 = Alumno("Javi", 15); a1.notas = [5, 6, 7]
a2 = Alumno("Lucía", 16); a2.notas = [9, 10, 9]
p1 = Profesor("Marta", 40); p1.asignaturas = ["Matemáticas", "Física"]

escuela.extend([a1, a2, p1])

while True:
    print("\n--- GESTIÓN ESCOLAR ---")
    print("1. Añadir Alumno")
    print("2. Añadir Profesor")
    print("3. Mostrar Alumnos Aprobados")
    print("4. Mejor Alumno")
    print("5. Buscar Profesores por Asignatura")
    print("6. Salir")
    op = input("Opción: ")

    if op == "1":
        nom = input("Nombre: ")
        alum = Alumno(nom, 15)
        # Notas rápidas
        notas_str = input("Notas separadas por espacio: ")
        alum.notas = [float(x) for x in notas_str.split()]
        escuela.append(alum)

    elif op == "2":
        nom = input("Nombre: ")
        prof = Profesor(nom, 35)
        asigs = input("Asignaturas separadas por espacio: ")
        prof.asignaturas = asigs.split()
        escuela.append(prof)

    elif op == "3":
        print("\nALUMNOS APROBADOS (Media >= 5):")
        for p in escuela:
            if isinstance(p, Alumno) and p.calcular_media() >= 5:
                print(f"- {p.nombre} (Media: {p.calcular_media():.2f})")

    elif op == "4":
        # Filtramos solo alumnos
        alumnos = [p for p in escuela if isinstance(p, Alumno)]
        if alumnos:
            mejor = max(alumnos, key=lambda x: x.calcular_media())
            print(f"🥇 Mejor alumno: {mejor.nombre} con {mejor.calcular_media():.2f}")

    elif op == "5":
        busqueda = input("Asignatura a buscar: ")
        print(f"Profesores de {busqueda}:")
        for p in escuela:
            if isinstance(p, Profesor) and busqueda in p.asignaturas:
                print(f"- {p.nombre}")

    elif op == "6":
        break