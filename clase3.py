#Ejercicio 1

largo = int(input("Ingresá el largo del rectángulo"))
ancho = int(input("Ingresá el ancho del rectángulo"))
areaRectangulo = largo * ancho

print("El área de tu rectángulo es", areaRectangulo)

#Ejercicio 2

nombre = input("Ingresá tu nombre")
comidaFavorita = input("Ingresá tu comida favorita")

print("Hola", nombre + ", tu comida favorita es", comidaFavorita)

#Ejercicio 3

nombreCompleto = input("Ingresá tu nombre y apellido")
nombre = nombreCompleto.split()[0]
apellido = nombreCompleto.split()[1]

print("Tu nombre es: ", nombre)
print("Tu apellido es: ", apellido)