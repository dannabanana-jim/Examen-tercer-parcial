#Ejercicio 4
#Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método __init__.
#Calcular después la suma, resta, multiplicación y división. Utilizar un método para cada una e imprimir los resultados obtenidos. 
#Llamar a la clase Calculadora.
print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")


class Calculadora:
    """
    Clase que representa una calculadora simple.
    Tiene métodos para realizar suma, resta, multiplicación y división.
    """
    def __init__(self, num1, num2):
        """
        Constructor de la clase. Inicializa los dos números con los cuales se realizará la operación.
        :param num1: float, primer número.
        :param num2: float, segundo número.
        """
        self.num1 = num1
        self.num2 = num2

    def suma(self):
        """
        Realiza la suma de los dos números.
        :return: La suma de los dos números.
        """
        return self.num1 + self.num2

    def resta(self):
        """
        Realiza la resta entre los dos números.
        :return: La resta de los dos números.
        """
        return self.num1 - self.num2

    def multiplicacion(self):
        """
        Realiza la multiplicación entre los dos números.
        :return: El resultado de la multiplicación.
        """
        return self.num1 * self.num2

    def division(self):
        """
        Realiza la división entre los dos números.
        Si el segundo número es 0, muestra un error.
        :return: El resultado de la división o un mensaje de error.
        """
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: No se puede dividir por 0"

calc = Calculadora(10, 5)
print("Suma:", calc.suma())          # Imprime la suma
print("Resta:", calc.resta())        # Imprime la resta
print("Multiplicación:", calc.multiplicacion())  # Imprime la multiplicación
print("División:", calc.division())  # Imprime la división
