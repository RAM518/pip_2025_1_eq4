archivo=open(r"C:\6to Semestre\Programacion de interfaces y puertos\pip_2025_1_eq4\Archivo\Calificaciones-nombre-file.csv")
contenido = archivo.readlines()

print(contenido)
datos = [i.split(",") for i in contenido]
print(datos)

datos = [[i[0], list(map(int,i[1:])) ] for i in datos]
print(datos)

#calcular el promedio de cada alumno y agregar el resultado a la
#lista asociada al usuario

datos= [[ i [0], i[1], sum( i [1])/len(i[1])] for i in datos]
print(datos)

nombres = [i[0]for i in datos]
promedios = [i[2]for i in datos]

from matplotlib import pyplot as plt
plt.bar (nombres, promedios)

plt.title("Histograma de caificaciones")
plt.xlabel("Nombre")
plt.ylabel("Promedio")
plt.ylim(0,12)

plt.show()