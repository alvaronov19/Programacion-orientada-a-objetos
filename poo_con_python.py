class Personaje:
    #Indica que no se va hacer nada por el momento
    #Atributos de la clase

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida
        
    def atributos(self):
        print(self.nombre)
        print("-Fuerza-", self.fuerza)
        print("-Inteligencia-", self.inteligencia)
        print("-Defensa-", self.defensa)
        print("-Vida-", self.vida)
    def subir_nivel(self, fuerza, inteligencia, defensa):
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa
    def esta_vivo(self):
        return self.vida > 0
    def morir(self):
        self.vida = 0
        print(self.nombre, "Has muerto")
    def dañar(self, enemigo):
        return self.fuerza - enemigo.defensa
    def atacar(self, enemigo):
        daño = self.dañar(enemigo)
        enemigo.vida = enemigo.vida - daño
        print(self.nombre, "Ha realizado", daño, "puntos de daño a", enemigo.nombre)
        print("Vida de", enemigo.nombre, "es:", enemigo.vida)

#Creando clase Guerrero que herada de su clase padre "Personaje"
class Guerrero(Personaje):
    #Sobreescribir el constructor 
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        #Llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada
hercules = Guerrero("Hércules", 80, 50, 100, 100, 5)
hercules.atributos()
print(hercules.espada)

#Variable del constructor vacío de la clase 
#mi_personaje = Personaje ("Kanye", 90, 100, 80, 100)
#mi_enemigo = Personaje ("Ogro" , 90, 100, 80, 100)
#print(mi_personaje.esta_vivo())
#print(mi_personaje.dañar(mi_enemigo))
#mi_personaje.atributos()
#mi_personaje.atacar(mi_enemigo)
#mi_enemigo.atributos()
#mi_personaje.subir_nivel(10, 10, 0)
#mi_personaje.atributos()
#Modificando valores de los atributos
