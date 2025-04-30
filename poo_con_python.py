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

<<<<<<< HEAD
    def personajeMasVida(personajes):
    max_vida = max(personajes, key=lambda p: p.vida)
    print(f"El personaje con más vida es {max_vida.nombre} con {max_vida.vida} puntos de vida.")

    def sumaInteligencia(personajes):
        total_inteligencia = sum(p.inteligencia for p in personajes)
        print(f"La inteligencia total de los personajes es: {total_inteligencia}")

    def personajesVidaMayorA(personajes, valor_vida):
        filtrados = [p for p in personajes if p.vida > valor_vida]
        if filtrados:
            print(f"Los personajes con vida mayor a {valor_vida} son:")
            for p in filtrados:
                print(f"- {p.nombre}: {p.vida} puntos de vida")
        else:
            print(f"No hay personajes con vida mayor a {valor_vida}.")

    
=======
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

>>>>>>> 50a1277ccdd8a23f77635bbe7469bd7e47f9a9a8
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
