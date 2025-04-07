"""import random
#1. Operadores, comparaciones y conversión de variables
#Ejercicio 1: Verificar edades

usuarioEdad = int(input("Decime tu edad"))

if usuarioEdad >= 18:
    print("Sos mayor de edad")
else:
    print("Sos menor de edad")

#Ejercicio 2: Comparar números

primerNumero = int(input("Decime un número"))
segundoNumero = int(input("Decime otro número"))

if primerNumero < segundoNumero:
    print(primerNumero)
    print(segundoNumero)
else:
    print(segundoNumero)
    print(primerNumero)

#Ejercicio 3: Conversión de tipos

numeroDecimal = float(input("Decime un número decimal"))
numeroFinal = int(numeroDecimal)

print(numeroFinal)

#2. Strings y manipulación de texto
#Ejercicio 4: Mayúsculas y minúsculas

frase = input("Decime una frase")
print("En mayúsculas:", frase.upper())
print("En minúsculas:", frase.lower())
print("La primera letra de cada palabra en mayúsculas:", frase.title())

#Ejercicio 5: Primer palabra

otraFrase = input("Dime una frase")
print(otraFrase.split()[0])

#3. Condicionales (if, elif, else)
#Ejercicio 7: Clima y ropa

temperatura = int(input("Ingresá la temperatura actual"))

if temperatura < 10:
    print("Usá un abrigo pesado")
elif temperatura < 20:
    print("Usá un buzo")
else: 
    print("Usá una remera")

#Ejercicio 8: Notas y calificaciones

nota = int(input("Decime una nota"))

if nota > 6:
    print("Excelente")
elif nota >= 4 and nota <= 6:
    print("Aprobado")
else:
    print("Aplazado")

#4 Listas y acceso a elementos
#Ejercicio 9: Crear una lista de compras

listaVacia = []
producto1 = input("Ingrese el primer producto")
producto2 = input("Ingrese el segundo producto")
producto3 = input("Ingrese el tercer producto")
listaVacia.append(producto1)
listaVacia.append(producto2)
listaVacia.append(producto3)
print("Lista completa: ", listaVacia)

#Ejercicio 10: Acceder a elementos de una lista

otraListaVacia = []
primerNombre = input("Ingrese el primer nombre")
segundoNombre = input("Ingrese el segundo nombre")
tercerNombre = input("Ingrese el tercer nombre")

otraListaVacia.append(primerNombre)
otraListaVacia.append(segundoNombre)
otraListaVacia.append(tercerNombre)

print(len(otraListaVacia))
print(otraListaVacia)

print(otraListaVacia[0])
print(otraListaVacia[2])

#Ejercicio 11: Agregar elementos

otraLista = []
primerFruta = input("Ingresá la primer fruta")
segundaFruta = input("Ingresá la segunda fruta")
tercerFruta = input("Ingresá la tercer fruta")

otraLista.append(primerFruta)
otraLista.append(segundaFruta)
otraLista.append(tercerFruta)

print(otraLista)

otraFruta = input("Agregá otra fruta")

otraLista.append(otraFruta)
print(otraLista)

#Ejercicio 12: Unir dos listas

listaVacia1 = []
primerNombre = input("Decime tu nombre")
segundoNombre = input("Decime tu apellido")

listaVacia1.append(primerNombre)
listaVacia1.append(segundoNombre)

print(listaVacia1)

listaVacia2 = []
primerNombre = input("Decime tu nombre")
segundoNombre = input("Decime tu apellido")

listaVacia2.append(primerNombre)
listaVacia2.append(segundoNombre)

print(listaVacia2)

sumaListas = (listaVacia1 + listaVacia2)
print(sumaListas)

#5. Bucles (while y for)
#Ejercicio 13: Contador con while

contador = 1
miNumero = int(input("Dame un numero"))
while contador <= miNumero:
    print(contador)
    contador += 1

#Ejercicio 14: Ingresar hasta acertar

numeroAleatorio = 7
numeroAdivinar = int(input("Adiviná el número"))

while numeroAdivinar != numeroAleatorio:
    print("Intentalo de nuevo!")
    numeroAdivinar = int(input("Adiviná el número"))
print("Adivinaste!")

#Ejercicio 15: Lista con for

listaVacia = []
primerElemento = input("Decime un elemento")
segundoElemento = input("Decime un segundo elemento")
tercerElemento = input ("Decime un tercer elemento")
cuartoElemento = input ("Decime un cuarto elemento")
quintoElemento = input ("Decime un quinto elemento")

listaVacia.append(primerElemento)
listaVacia.append(segundoElemento)
listaVacia.append(tercerElemento)
listaVacia.append(cuartoElemento)
listaVacia.append(quintoElemento)

for elementos in listaVacia:
    print(elementos)

#Ejercicio 16: Números con for

listaVacia = []
primerNumero = int(input("Decime un numero"))
segundoNumero = int(input("Decime un segundo numero"))
tercerNumero = int(input ("Decime un tercer numero"))
cuartoNumero = int(input ("Decime un cuarto numero"))
quintoNumero = int(input ("Decime un quinto numero"))

listaVacia.append(primerNumero)
listaVacia.append(segundoNumero)
listaVacia.append(tercerNumero)
listaVacia.append(cuartoNumero)
listaVacia.append(quintoNumero)

for elementos in listaVacia:
    print(elementos)

#Ejercicio 17: Numerar lista

palabras = []

palabras.append(input("Decime una palabra"))
palabras.append(input("Decime otra palabra"))

for i in range(len(palabras)):
        print(i, palabras[i])

#6. Ejercicios combinados avanzados
#Ejercicio 18: Adivina el número

numeroAleatorio= random.randint(1,10)
print("El número aleatorio para el programador es", numeroAleatorio)
numeroAdivinar = int(input("Adiviná el número"))
while numeroAdivinar != numeroAleatorio:
    print("Intentalo de nuevo!")
    numeroAdivinar = int(input("Adiviná el número"))

print("Adivinaste!")

# Ejercicio 19: Cargar lista hasta escribir "fin"

palabras = []

palabra = input("Escribí una palabra (o fin para terminar)")

while palabra != "fin":
    palabras.append(palabra)
    palabra = input("Escribí otra palabra (o fin para terminar)")

print("Las palabras que escribiste son:", palabras)

#Ejercicio 20: Filtrar palabras largas

palabrasLargas = []
contador = 0

while contador < 5:
    palabra = input("Escribí una palabra: ")
    if len(palabra) > 5:
        palabrasLargas.append(palabra)
    contador += 1

print("Palabras con más de 5 letras:", palabrasLargas)

#🎯 Desafío Final: "Palabras que empiezan con vocal”

listaVacia = []
for i in range(3): 
    palabra = input("Escribí una palabra: ")
    listaVacia.append(palabra)

print("Palabras ingresadas:", listaVacia)

nuevaLista = ['a', 'e', 'i', 'o', 'u']

palabrasVocal = []

for palabra in listaVacia:
    for vocal in nuevaLista:
        if palabra[0].lower() == vocal:
            palabrasVocal.append(palabra)
            break 

print("Palabras que empiezan con vocal:", palabrasVocal)

#Mini Repaso: for i in range()
#Ejercicio Simple: Cuenta Regresiva

numero = int(input("Decime un número"))
for i in range(numero, 0, -1):
    print(i)

#Ejercicio Intermedio: Contar letras 'a'
palabra = input("Decime una palabra")

cantidad_a = palabra.lower().count("a")
print(f"La letra 'a' aparece {cantidad_a} veces en la palabra '{palabra}'.")
"""
#Ejercicio Desafiante: Tabla de Multiplicar Personalizada

usuarioNumero = int(input("Decime un número"))
for i in range(1, 11):
    multiplicacion = usuarioNumero * i
    print(f"{usuarioNumero} x {i} = {multiplicacion}")