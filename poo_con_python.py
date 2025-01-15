class Personaje:
    #Indica que no se va hacer nada por el momento
    #Atributos de la clase

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.__nombre = nombre
        self.__fuerza = fuerza
        self.__inteligencia = inteligencia
        self.__defensa = defensa
        self.__vida = vida
        
    def atributos(self):
        print(self.__nombre)
        print("-Fuerza-", self.__fuerza)
        print("-Inteligencia-", self.__inteligencia)
        print("-Defensa-", self.__defensa)
        print("-Vida-", self.__vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.__fuerza += fuerza
        self.__inteligencia += inteligencia
        self.__defensa += defensa
    def esta_vivo(self):
        return self.__vida > 0
    def morir(self):
        self.__vida = 0
        print(self.__nombre, "Has muerto")
    def dañar(self, enemigo):
        return self.__fuerza - enemigo.__defensa if self.__fuerza > enemigo.__defensa else 0
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.__vida = enemigo.__vida - daño
        print(self.__nombre, "Ha realizado", daño, "puntos de daño a", enemigo.__nombre)
        if not enemigo.esta_vivo():
            enemigo.__morir()
        print("Vida de", enemigo.__nombre, "es:", enemigo.__vida)

def get_fuerza(self):
    return self.__fuerza
def set_fuerza(self, fuerza):
    self.__fuerza = fuerza

#Variable del constructor vacío de la clase 
mi_personaje = Personaje ("Kanye", 8000, 90, 50, 100)
mi_enemigo = Personaje ("Ogro" , 60, 90, 40, 100)
#Prueba 4. Acceso o morir??
#mi_personaje.atacar(mi_enemigo)
#Prueba 7. Geyyers and setters
#print(mi_personaje.get_fuerza())
#mi_personaje.set_fuerza(-100)
#print(mi_personaje.get_fuerza())
mi_personaje._Personaje__fuerza = 10
mi_personaje.atributos()

#Prueba 1. Sin acceso el atributo fuerza
#print(mi_personaje.fuerza)




#print(mi_personaje.esta_vivo())
#print(mi_personaje.dañar(mi_enemigo))
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#mi_personaje.subir_nivel(10, 10, 0)
#mi_personaje.atributos()
#Modificando valores de los atributos
