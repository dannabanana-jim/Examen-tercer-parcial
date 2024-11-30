#Ejercicio 5
#Realizar una clase que administre una agenda. Se debe almacenar para cada contacto el nombre, el teléfono y el email. 
#Además deberá mostrar un menú con las siguientes opciones
#Añadir contacto
#Lista de contactos
#Buscar contacto
#Editar contacto
#Cerrar agenda

print(" ")
print("Danna Paola Martinez Jimenez 3-W No. 1195")
print(" ")

class Agenda:
    """
    Clase que representa una agenda donde se pueden gestionar contactos.
    Tiene métodos para añadir, listar, buscar, editar y cerrar la agenda.
    """
    def __init__(self):
        """
        Constructor de la clase. Inicializa una lista vacía de contactos.
        """
        self.contactos = []

    def añadir_contacto(self, nombre, telefono, email):
        """
        Añade un nuevo contacto a la agenda.
        :para nombre: str, nombre del contacto.
        :para telefono: str, número de teléfono del contacto.
        :para email: str, correo electrónico del contacto.
        """
        self.contactos.append({"nombre": nombre, "telefono": telefono, "email": email})

    def listar_contactos(self):
        """
        Lista todos los contactos almacenados en la agenda.
        """
        for contacto in self.contactos:
            print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    def buscar_contacto(self, nombre):
        """
        Busca un contacto por nombre y muestra los datos si lo encuentra.
        :para nombre: str, nombre del contacto a buscar.
        """
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                print(f"Contacto encontrado: {contacto}")
                return
        print("Contacto no encontrado.")

    def editar_contacto(self, nombre, nuevo_telefono, nuevo_email):
        """
        Edita los datos de un contacto.
        :param nombre: str, nombre del contacto a editar.
        :param nuevo_telefono: str, nuevo número de teléfono.
        :param nuevo_email: str, nuevo correo electrónico.
        """
        for contacto in self.contactos:
            if contacto["nombre"] == nombre:
                contacto["telefono"] = nuevo_telefono
                contacto["email"] = nuevo_email
                print(f"Contacto {nombre} editado.")
                return
        print("Contacto no encontrado.")

    def cerrar_agenda(self):
        """
        Cierra la agenda (muestra un mensaje de cierre).
        """
        print("Agenda cerrada.")


agenda = Agenda()
agenda.añadir_contacto("Caslos", "123456789", "caslos@mail.com")
agenda.añadir_contacto("Teresa", "987654321", "Teresa@mail.com")
agenda.listar_contactos()   # Muestra todos los contactos
agenda.buscar_contacto("Caslos")  # Busca a Caslos
agenda.editar_contacto("Caslos", "111222333", "nuevo@mail.com")  # Edita los datos de Carlos
agenda.listar_contactos()   # Muestra todos los contactos actualizados
agenda.cerrar_agenda()      # Cierra la agenda
