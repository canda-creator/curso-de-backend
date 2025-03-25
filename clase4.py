#Ejercicio 1
usuarioNombre = input("Ingresá tu nombre")
usuarioHora = int(input("Ingresá la hora"))

if usuarioHora <= 12 and usuarioHora >= 0:
    print("Buenos días", usuarioNombre)
elif usuarioHora >= 13 and usuarioHora <= 19 :
    print ("Buenas tardes", usuarioNombre)
else:
    print("Buenas noches")

#Ejercicio 2
precioProducto = float(input("Decime el precio del producto"))
cuponProducto = input("Decime si tenes descuento")

descuento = (precioProducto * 20) / 100
precioFinal = precioProducto - descuento

if cuponProducto == "Sí":
    print("El precio final es: ", precioFinal)

else:
    print("El precio final es: ", precioProducto)
    
#Ejercicio 3
temperatura = int(input("Decime la temperatura en grados Celsius"))

if temperatura <= 0:
    print("Hace mucho frío")

elif temperatura >= 30:
    print("Hace mucho calor")

else:
    print("El clima está agradable")


#Operadores Lógicos
#Ejercicio 1

usuarioPromedio = float(input("Cuál es tu promedio escolar?"))
usuarioIngresos = int(input("Cuál es tu nivel de ingresos?"))

if usuarioPromedio >= 8 and usuarioIngresos < 50000:
    print("Beca concedida")


#Ejercicio 2
usuarioPeso = float(input("Cuál es tu peso?"))
usuarioAltura = float(input("Cuál es tu altura?"))
usuarioAltura = usuarioAltura / 100

indiceMasaCorporal = usuarioPeso / (usuarioAltura * usuarioAltura)

if indiceMasaCorporal < 18.5:
    print("Estás en bajo peso")
elif indiceMasaCorporal >= 18.5 and indiceMasaCorporal < 24.9:
    print("Tenés un peso normal")
elif indiceMasaCorporal >= 25 and indiceMasaCorporal < 29.9:
    print("Tenes sobrepeso")
elif indiceMasaCorporal >= 30:
    print("Tenés obesidad")


#Ejercicio 3
usuarioNota = float(input("Decime una nota"))

if usuarioNota >= 1 and usuarioNota <= 3:
    print("Muy insuficiente")

elif usuarioNota >= 4 and usuarioNota <= 5:
    print("Insuficiente")

elif usuarioNota == 6:
    print("Suficiente")

elif usuarioNota >= 7 and usuarioNota <= 8:
    print("Notable")

elif usuarioNota == 10:
    print("Sobresaliente")


#Ejercicio 4
numeroSecreto = 7
usuarioNumero = int(input("Adiviná el número"))

if usuarioNumero == numeroSecreto :
    print("¡Adivinaste!")

else:
    print("Intentá de nuevo")