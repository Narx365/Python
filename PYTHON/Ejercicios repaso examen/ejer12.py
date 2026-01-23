
def promedio_edades(cantidad, nombre_turno):
    print(f"\n ingrese las edades de los estudiantes del turno {nombre_turno}")
    suma = 0
    for i in range(cantidad):
        edad = int(input("edad: "))
        suma += edad / cantidad

promedio_mañanas = promedio_edades(5, "mañanas")
promedio_tardes = promedio_edades(6, "tardes")
promedio_noches = promedio_noches(11, "noches")
