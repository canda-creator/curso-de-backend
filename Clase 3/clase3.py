#Clase 3

#Ejercicio 1
usuarioEdad = int(input("¿Cuántos años tenes?"))
if usuarioEdad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

#Ejercicio 2
usuarioNumero = int(input("Dime un número"))

if usuarioNumero > 0:
    print("Es un número positivo")
elif usuarioNumero == 0:
    print("Es cero")
else: 
    print("Es un número negativo")

#Ejercicio 3
contraseñaPreestablecida = "Python123"
ingreseContraseña = input("Ingrese la contraseña")

if ingreseContraseña == contraseñaPreestablecida:
    print("Acceso concedido")
else:
    print("Acceso denegado")