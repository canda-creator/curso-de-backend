#Clase 3
#Ejercicio 1
# **Ejercicio 1:** Mayor o menor de edad
#Pedí al usuario su edad e imprimí si el usuario es mayor o menor de edad.

usuarioEdad = int(input("¿Cuántos años tenes?"))
if usuarioEdad >= 18:
    print("Sos mayor de edad.")
else:
    print("Sos menor de edad.")

#Ejercicio 2
#### **Ejercicio 2:** Número positivo, negativo o cero
#Pedí un número al usuario e imprimí **si SOLO es positivo, negativo o cero**.

usuarioNumero = int(input("Dime un número"))

if usuarioNumero > 0:
    print("Es un número positivo")
elif usuarioNumero == 0:
    print("Es cero")
else: 
    print("Es un número negativo")

#Ejercicio 3
### **Ejercicio 3:** Verificación de contraseña

#Definí una contraseña preestablecida (por ejemplo, "python123") y pedí al usuario que ingrese una. Si coincide, mostrale "Acceso concedido", de lo contrario, "Acceso denegado".

contraseñaPreestablecida = "Python123"
ingreseContraseña = input("Ingrese la contraseña")

if ingreseContraseña == contraseñaPreestablecida:
    print("Acceso concedido")
else:
    print("Acceso denegado")