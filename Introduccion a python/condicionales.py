# Importamos del archivo retornar_valores
# la clase Calculadora
from retornar_valores import Calculadora

# Le pedimos al usuario que ingrese numeros
n1 = input("Ingrese primer numero: ")
n2 = input("Ingrese segundo numero: ")


# Creamos un objeto de la clase calculadora
calc = Calculadora(int(n1), int(n2))

# Si el resultado de la suma de ambos numeros es
# mayor a 50 , tomamos ese valor , lo convertimos
# a letra y luego  imprimimos un mensaje en pantalla
if( calc.sumar() > 50):
    print("el numero: " + str(calc.sumar()) + " es mayor a 50")
# Si no, si el valor es menor, hacemos lo mismo
elif(calc.sumar() < 50):
    print("el numero: "  + str(calc.sumar()) + " es menor a 50")

# Si el resultado de la division de ambos numeros es igual
# o menor a 13 y mayor a 10 imprimimos un mensaje
if(calc.dividir() <= 13  and calc.dividir() < 10):
    print("el numero: " + str(calc.dividir()) + " es 25 o menos")
# Si no, si el resultado de la division de ambos numeros es mayor o igual
# a 13 y sea mayor a 10 imprimimos un mensaje
elif(calc.dividir() >= 13  and calc.dividir() > 10):
    print("el numero: " + str(calc.dividir()) + " es 25 o mas")
# Si el resultado es mayor a 10 o  menor a 20
if(calc.dividir() > 10 or calc.dividir() < 20):
    print("el numero es mayor a 10")

# Mientras el resultado de la division sea
# mayor a 11 imprimiremos un mensaje
while(calc.dividir() > 11):
    print("si es")