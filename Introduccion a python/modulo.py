
# Los modulos son simple archivos con
# clases, de estos podemos  sacar codigo
# para utilizarlos en diversas operaciones
# y llevar un orden de nuestro codigo
from clase import Calculadora

# creamos una calculadora, usando
# los numeros 50 y 25 como entrada
calc = Calculadora(50,25)

# Llamamos al metodo sumar de la 
# calculadora 50+25 = 75
calc.sumar()

# Llamamos al metodo restar de la 
# calculadora 50-25 = 25
calc.restar()

# Llamamos al metodo multiplicar de la 
# calculadora 50*25 = 1250
calc.multiplicar()

# Llamamos al metodo dividir de la 
# calculadora 50 / 25 = 2
calc.dividir()