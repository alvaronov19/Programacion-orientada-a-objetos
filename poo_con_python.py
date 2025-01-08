class Personaje:
    #Indica que no se va hacer nada por el momento
    #Atributos de la clase
    nombre = 'default'
    fuerza = 0
    inteigencia = 0
    defensa = 0
    vida = 0

#Variable del constructor vacío de la clase 
mi_personaje = Personaje ()
#Modificando valores de los atributos
mi_personaje.nombre = "Gandalf"
mi_personaje.fuerza = 100
print ("El nombre del personaje es: ", mi_personaje.nombre)
print ("La fuerza del personaje es: ", mi_personaje.fuerza)
print ("La inteligencia del personaje es: ", mi_personaje.inteigencia)
print ("La defensa del personaje es: ", mi_personaje.defensa)
print ("La vida del personaje es: ", mi_personaje.vida)