import random

cuenta = int(input("Decime un número"))
while cuenta >= 1:
    print(cuenta)
    cuenta -=1

if cuenta == 0:
    print ("¡Despegue! 🚀")


numero = int(input("Decime un número"))
while numero != 0:
    print(numero)
    numero -= 1

print("¡Despegue! 🚀")



contraseña = "Python123"
contraseñaIngreso = input("Ingrese la contraseña") 

while contraseñaIngreso != contraseña:
    print("Contraseña incorrecta. Intentalo de nuevo.")
    contraseñaIngreso = input("Ingrese la contraseña") 

print("Acceso concedido!")


contraseñaPython = input("Ingrese la contraseña: ")
while contraseñaPython != "Python123":
    print("Contraseña incorrecta")
    contraseñaPython = input("Ingrese la contraseña: ") 

print("Acceso concedido!")


cero = 0
numeroUsuario = int(input("Ingresá un número"))

while numeroUsuario != 0:
    cero += numeroUsuario
    numeroUsuario = int(input("Ingresá un numero"))

print("La suma total es: ", cero)


numeroAleatorio= random.randint(1,10)
print("El numero aleatorio es: ", numeroAleatorio)

numeroAdivinar = int(input("Adiviná el número"))

while numeroAdivinar != numeroAleatorio:
    print("Intentalo de nuevo!")
    numeroAdivinar = int(input("Adiviná el número"))

print("Adivinaste!")


intentos = 5
numeroSecreto = random.randint(1,20)
print("El numero secreto es: ", numeroSecreto)

while intentos > 0:
    adivinar = int(input("🎲 Adivina el número (1-20). Tenés 5 intentos."))
    if adivinar == numeroSecreto :
        print("🎉 ¡Adivinaste!")
        break

    elif adivinar >= numeroSecreto:
        print("🔹 Muy alto.")

    elif adivinar <= numeroSecreto:
        print("🔹 Muy bajo.")
    
    intentos -= 1
    print(f"Incorrecta, te quedan {intentos} intentos")
    
if intentos == 0:
    print("No te quedan intentos. El número secreto es: ", numeroSecreto)