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

    #Perdirle al usurario escoger un arma
    '''def cambiar_arma(self):
        opcion = int(input("Elige un arma: (1) Espada de plata, daño 10. (2) Espada de bronce, daño 8"))
        if opcion == 1:
            self.espada = 10
        elif opcion == 2:
            self.espada = 8
        else:
            print("Opcion incorrecta")'''

    #Sobreescribir metodo      
    def atributos(self):
        super().atributos()
        print("-Espada-", self.espada)

    #Sobreescribir el calculo de daño 
    def dañar(self, enemigo):
        return self.fuerza * self.espada - enemigo.defensa
    
class Mago(Personaje):
    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        #Llamar a la clase padre
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro

    #Sobreescribir metodo      
    def atributos(self):
        super().atributos()
        print("-Libro-", self.libro)

    #Sobreescribir el calculo de daño 
    def dañar(self, enemigo):
        return self.inteligencia * self.libro - enemigo.defensa

trakalosa = Personaje("Trakalosa de Monterrey", 20, 15, 10, 100)
hercules = Guerrero("Hércules", 20, 15, 10, 100, 5)
diosito = Mago("Diosito", 20, 15, 10, 100, 5)
#Imprimir atributos antes del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()
#Ataques
trakalosa.atacar(hercules)
hercules.atacar(diosito)
diosito.atacar(trakalosa)
#Imprimir atributos antes del ataque
trakalosa.atributos()
hercules.atributos()
diosito.atributos()

#hercules.cambiar_arma()
#hercules.atributos()
#print(hercules.espada)

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
