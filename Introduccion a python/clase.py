# La clase calculadora representa un objeto de la vida real
# con sus propiedades (Botones) y metodos (Acciones que puede realizar
# como lo son sumas , restas , multiplicaciones, etc) 
class Calculadora:
    # La funcion __init__ es una funcion de python
    # que nos permite definir las propiedades iniciales
    # del objeto, self , siendo la clase, y n1 y n2 numeros
    # a ingresar para realizar operaciones
    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    # La funcion sumar toma los valores de el
    # el objeto de la clase e imprime en pantalla
    # el resultado de la suma de estos    
    def sumar(self):
        print(str(self.n1 + self.n2))
    # La funcion sumar toma los valores de el
    # el objeto de la clase e imprime en pantalla
    # el resultado de la resta de estos    
    def restar(self):
        print(str(self.n1 - self.n2))
        
    # La funcion sumar toma los valores de el
    # el objeto de la clase e imprime en pantalla
    # el resultado de la multiplicacion de estos    
    def multiplicar(self):
        print(str(self.n1 * self.n2))
    
    
    # La funcion sumar toma los valores de el
    # el objeto de la clase e imprime en pantalla
    # el resultado de la division de estos    
    def dividir(self):
        print(str(self.n1 / self.n2))
        
        
