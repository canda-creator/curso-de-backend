#🎯 Desafío Final: "Adivina el número en 5 intentos" (Clase Pasada)
import random

intentos = 5
numeroSecreto = random.randint(1,20)
print("El numero secreto es:", numeroSecreto)

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


#🧠 Ejercicio 1: Contraseña con mayúsculas y minúsculas

while True:
    contraseña = input("Ingresá una contraseña: ")

    if len(contraseña) >= 6 and contraseña.lower() != contraseña and contraseña.upper() != contraseña:
        print("✅ Contraseña guardada con éxito.")
        break
    else:
        print("❌ La contraseña debe tener al menos 6 caracteres, una mayúscula y una minúscula.")

#✍️Ejercicio 2: Comparador de palabras

primeraPalabra = input("Ingresá una palabra")
segundaPalabra = input("Ingresá otra palabra")

if len(primeraPalabra) > len(segundaPalabra):
    print(primeraPalabra, "es más larga que" , segundaPalabra)

elif len(primeraPalabra) < len(segundaPalabra):
    print(segundaPalabra, "es más larga que", primeraPalabra)

else:
    print(primeraPalabra, "y", segundaPalabra, "son iguales.")


#🔹 Ejercicio 3: Pedir un número positivo

numero = input("Ingresá un número mayor a 0: ")

while numero == "" or (numero[0] == "-" or numero == "0"):  
    print("❌ Error: Debe ser un número mayor a 0.")  
    numero = input("Ingresá un número mayor a 0: ")  

print(f"✅ Número aceptado: {numero}")  
