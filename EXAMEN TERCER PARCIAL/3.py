#Ejercicio 3
#Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con los métodos para inicializar
#los atributos, imprimir el valor del lado con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")

class Triangulo:
    """
    Clase que representa un triángulo con tres lados.
    Tiene métodos para imprimir el lado mayor y determinar el tipo de triángulo.
    """
    def __init__(self, lado1, lado2, lado3):
        """
        Constructor de la clase. Inicializa los tres lados del triángulo.
        :param lado1: float, longitud del primer lado.
        :param lado2: float, longitud del segundo lado.
        :param lado3: float, longitud del tercer lado.
        """
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def imprimir_lado_mayor(self):
        """
        Imprime el valor del lado mayor del triángulo.
        """
        mayor = max(self.lado1, self.lado2, self.lado3)
        print(f"El lado mayor es: {mayor}")

    def tipo_triangulo(self):
        """
        Determina el tipo de triángulo:
        - Equilátero: todos los lados son iguales.
        - Isósceles: al menos dos lados son iguales.
        - Escaleno: los tres lados son diferentes.
        """
        if self.lado1 == self.lado2 == self.lado3:
            print("El triángulo es equilátero.")
        elif self.lado1 == self.lado2 or self.lado2 == self.lado3 or self.lado1 == self.lado3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno.")


triangulo1 = Triangulo(5, 5, 8)
triangulo1.imprimir_lado_mayor()  # Imprime el lado mayor
triangulo1.tipo_triangulo()       # Determina el tipo de triángulo

