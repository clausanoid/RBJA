from retornar_valores import Calculadora

calc = Calculadora(25, 2)

if( calc.sumar() > 50):
    print("el numero: " + str(calc.sumar()) + " es mayor a 50")
elif(calc.sumar() < 50):
    print("el numero: "  + str(calc.sumar()) + " es menor a 50")
    
if(calc.dividir() <= 13  and calc.dividir() > 10):
    print("el numero: " + str(calc.dividir()) + " es 25 o menos")
elif(calc.dividir() >= 13  and calc.dividir() > 10):
    print("el numero: " + str(calc.dividir()) + " es 25 o mas")
    
if(calc.dividir() > 10 or calc.dividir() > 10):
    print("el numero es mayor a 10")

while(calc.dividir() > 11):
    print("si es")