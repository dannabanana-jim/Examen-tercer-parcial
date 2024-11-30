#Ejercicio 2
#Realizar un programa que tenga una clase Persona con las siguientes características.
#La clase tendrá como atributos el nombre y la edad de una persona. Implementar los métodos necesarios para
# inicializar los atributos, mostrar los datos e indicar si la persona es mayor de edad o no.

print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")

class Persona:
    """
    Clase que representa una persona, con su nombre y edad.
    Tiene métodos para mostrar los datos y verificar si la persona es mayor de edad.
    """
    def __init__(self, nombre, edad):
        """
        Constructor de la clase. Inicializa los atributos nombre y edad de la persona.
        :param nombre: str, nombre de la persona.
        :param edad: int, edad de la persona.
        """
        self.nombre = nombre
        self.edad = edad

    def mostrar_datos(self):
        """
        Muestra el nombre y la edad de la persona.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")

    def es_mayor_de_edad(self):
        """
        Verifica si la persona es mayor de edad.
        Se considera mayor de edad a partir de los 18 años.
        """
        if self.edad >= 18:
            print(f"{self.nombre} es mayor de edad.")
        else:
            print(f"{self.nombre} no es mayor de edad.")


persona1 = Persona("Celia", 20)
persona1.mostrar_datos()       # Muestra nombre y edad
persona1.es_mayor_de_edad()    # Verifica si es mayor de edad

