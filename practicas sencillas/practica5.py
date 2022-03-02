# Creamos la clase
class Persona:
    # creamos la primera funcion
    # para inicializar el atributo nombre
    def inicializar(self,nom):
        self.nombre=nom

    # creamos el segundo metodo
    # para mostrar el nombre
    def mostrar(self):
        print("Nombre: ",self.nombre)
#bloque principal
# creamos una instancia de la clase persona
persona1=Persona()
persona1.inicializar("Hilda")
persona1.mostrar()

# creamos un objeto de la clase persona
persona2=Persona()
persona2.inicializar("Araceli")
persona2.mostrar()
