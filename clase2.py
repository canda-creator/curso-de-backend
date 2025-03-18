#Primer Ejercicio
eldenCant = 3
minecraftCant = 2
cyberpunkCant = 1

eldenPrecio = 50
minecraftPrecio = 20
cyberpunkPrecio = 30

resultado = (eldenCant * eldenPrecio) + (minecraftCant * minecraftPrecio) + (cyberpunkCant * cyberpunkPrecio)
print ("Gané" , resultado)

#Segundo Ejercicio:
pikachuPeso = 6
charizardPeso = 90
bulbasaurPeso = 7

pikachuCant = 4
charizardCant = 2
bulbasaurCant = 3

pesoTotal = (pikachuPeso * pikachuCant) + (charizardPeso * charizardCant) + (bulbasaurPeso * bulbasaurCant)
cantTotal = (pikachuCant + charizardCant + bulbasaurCant)

print ("El peso total de los Pokémon es" , pesoTotal)
print ("Capturé" , cantTotal , "Pokémon.")

### Ejercitación de Input()

### 1️⃣ Biografía: Preguntas básicas

primerDato = input("¿Cuál es tu nombre?")
años = ("¿Cuántos años tenes?")
segundoDato = int(input(años))
tercerDato = input("¿De dónde sos?")

print("Hola" , primerDato , "Tenés" , segundoDato , "años." , "Sos de" , tercerDato)

### 2️⃣ Calculadora: Suma de dos números

primerNumero = int(input("Dime un número"))
segundoNumero = int(input("Dime otro número"))
resultadoSuma = primerNumero + segundoNumero

print("La suma es", resultadoSuma)

### 3️⃣ Días vividos: Conversión de edad a días
edad = int(input("Dime tu edad"))
diasVividos = edad * 365

print ("Viviste", diasVividos, "días")

### 4️⃣ Tips: Calculadora de propina
costo = float(input("Ingresá el costo de la comida: "))
propina_10 = costo * 0.10
propina_15 = costo * 0.15

print("Si querés dejar el 10%, la propina es:", propina_10)
print("Si querés dejar el 15%, la propina es:", propina_15)

### 4️⃣.1️⃣: Propina con input de %.
gasto = float(input("¿Cuánto gastaste?"))
porcentaje = float(input("¿Cuánto % querés dejar?"))
calculo = gasto * (porcentaje /100)
calculofinal = gasto + calculo

print(calculofinal)

#### Ejercitación de Strings

### 1️⃣ Nombre en diferentes formatos

nombre = input("¿Cuál es tu nombre?")

print("En mayuscula es: " , nombre.upper())
print("En minuscula es: " , nombre.lower()) 
print("La primera letra del nombre es " , nombre.title()) 

### 2️⃣ Contador de caracteres en una frase

frase = input("Dime una frase")
caracteres = len (frase)

print("La frase tiene" , caracteres, "caracteres")

### 3️⃣ Correo electrónico en minúsculas

correo = input("Dime tu correo")
minuscula = correo.lower()

print("Tu correo en minuscula es:", minuscula)

### 4️⃣ Convertir título de un libro

titulo = input("Dime tu libro favorito")
titulo2 = titulo.title()

print("Tu libro favorito es", titulo2)