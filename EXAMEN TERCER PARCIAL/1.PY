#Ejercicio 1
#Realizar un programa que conste de una clase llamada Alumno que tenga como atributos el nombre
# y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y
#mostrar un mensaje con el resultado de la nota y si ha aprobado o no.´

print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")

class Alumno:
    """
    Clase que representa a un alumno, con su nombre y nota.
    Tiene métodos para imprimir los atributos y determinar si el alumno ha aprobado o no.
    """
    def __init__(self, nombre, nota):
        """
        Constructor de la clase. Inicializa los atributos nombre y nota del alumno.
        :param nombre: str, nombre del alumno.
        :param nota: float, nota obtenida por el alumno.
        """
        self.nombre = nombre
        self.nota = nota

    def imprimir(self):
        """
        Imprime el nombre y la nota del alumno.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")

    def resultado(self):
        """
        Muestra si el alumno ha aprobado o no basado en su nota.
        Se considera aprobado con una nota mayor o igual a 6.
        """
        if self.nota >= 6:
            print(f"{self.nombre} ha aprobado.")
        else:
            print(f"{self.nombre} no ha aprobado.")


alumno1 = Alumno("Danna", 9)
alumno1.imprimir()   # Imprime el nombre y la nota
alumno1.resultado()  # Indica si aprobó o no




