
#en estas dos primeras lineas se piden el numero de preguntas habidas y acertadas en el examen hipotetico
NumPregunt=int(input("cuantas preguntas tenía la prueba?: "))
NumRespuest=int(input("cuantas respuestas ha acertado el probado?: "))

#en la siguiente linea se calcula el porcentaje de acierto del examen
porc=(NumRespuest*100)/NumPregunt

#en las siguientes lineas se comunica al usuario la nota final y el porcentaje de acierto del alumno, con comprobación para errores
if (porc<50 and porc>=0):
    print("ha sido un porcentaje de ",porc,"% y una nota insuficiente" )
elif (porc<75 and porc>=50):
    print("ha sido un porcentaje de ",porc,"% y una nota Regular" )
elif (porc<90 and porc>=75):
    print("ha sido un porcentaje de ",porc,"% y una nota Muy buena" )
elif (porc>=90 and porc<=100):
    print("ha sido un porcentaje de ",porc,"% y una nota Excelente" )
else:
    print("ha habido algun error, vuelve a intentarlo.")