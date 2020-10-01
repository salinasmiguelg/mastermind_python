#IMPORTACIÓN
#Se importan las funciones requeridas de random para
#generar las combinaciones aleatorias 
from random import *
from time import sleep
#Se importa sleep() para que no se cierre el programa de forma abrupta al final


#DEFINICIÓN DE FUNCIONES

#Se define la función para crear una respuesta aleatoria
def celTab():
    tab = []
    colores = "R,A,V,M,N"
    colores = colores.split(",")
    for e in list(range(0,4)): #se itera sobre una lista con los índices de 0 a 4 
        tab.append(colores[randint(0,4)]) #randint() da un entero entre 0 y 4
    return tab

#Función que crea el tablero para jugar        
def tablero():
    juego = list(range(0,4))
    return juego

#Función que permite al jugador (sea uno o dos) hacer un movimiento
def movimiento(tablero):
    tableroMod = list() #aquí se crea una lista que contendrá los movimientos
    for e in tablero: #se itera sobre el tablero original
        #pero se usa append() en el nuevo tablero con la respuesta
        mov = input("¿Qué ficha pondrá en la posición " + str(e+1) + ": ")
        tableroMod.append(mov)
    return tableroMod

#Función que verifica la jugada realizada
#esta compara la lista objetivo generada aleatoriamente
#con la ingresada en cada movimiento del jugador
def verificar(objetivo, tablero):
    CopOb = list() #se utiliza como copia del objetivo para modificarlo
    #con esta lista se evitan las repeticiones
    for ele in objetivo:
        CopOb.append(ele)
    Egal = list(range(0,4)) #En esta lista se almacenarán los resultados
    #de comprobar si las opciones ingresadas son válidas
    #Dentro de este for se comprueban las fichas negras
    #Dígase, las fichas en la posición correcta y con el color correcto
    for n in list(range(0,4)):
        if CopOb[n] == tablero[n]:
            Egal[n] = "Ne"
            tablero[n] = "_"
            CopOb[n] = "Us" #Cuando se encuentra una ficha negra, a fin de que
            #no se repitan en la siguiente revisión, se reemplaza con "US"
            #O sea, "usado"
    #El siguiente for busca las fichas blancas
    #Dígase, fichas que están en la lista objetivo, pero en posición incorrecta
    for n in list(range(0,4)):
        if tablero[n] in CopOb:
            for d in list(range(0,4)):
                if CopOb[d] == tablero[n]:
                    CopOb[d] = "Us" #como anteriormente, se reemplaza por "US"
                    break
            Egal[n] = "Bla"
    #En este for se comprueban los resultados restantes
    #Dígáse, los incorrectos, que se guardan como un espacio vacío
    #Se representa con "___"
    for n in list(range(0,4)):
        if type(Egal[n]) == type(1): #se compara el tipo de resultado
            #si es un número, como 1, se cambia a nulo, o "__"
            Egal[n] = "__"
    return Egal              
    #Se retorna la lista revisada

#Función que verifica la victoria de la jugada
#esta función cuenta el número de fichas negras 
def victoria(resul):
    ver = False #se asume la derrocha con verificador False
    canNer = 0
    for r in resul:
        if r == "Ne":
            canNer = canNer + 1
    if canNer == 4: #si se llega al resultado de 4 fichas negras, se gana
        #y por tango el verificador se cambia a True
        ver = True
    return ver

#Función que marca los movimientos del jugador dentro del juego
#En esta función entra el número del jugador (puede ser 1 o 2)
#Y la combinación a la que hay que llegar
def jugador(num, tab):
    ver = False #se asume que la jugada será errónea
    t = tablero() #se crea el tablero de juego
    mov = movimiento(t) #se llama al movimiento
    venk = verificar(tab,mov) #dada la respuesta, se verifica la victoria
    print(venk[3] + " " + venk[0] + "\n" + venk[2] + " " + venk[1])
    #en el print anterior se muestra por pantalla (desordenado) los resultados
    #de los movimientos del jugador
    b = victoria(venk) #se verifica el True o False de la función victoria
    if b == True: #de ser True, se da el mensaje por pantalla
        #dando la victoria al jugadoor [num] y cambiando el verificador a True
        print("¡Usted ha ganado, jugador " + str(num) + "!")
        ver = True
    else: #se lo contrario, se imprime un "siga intentándolo"
        print("¡Ups! Siga intentándolo\n")
    return ver #se devuelve o un verificador ganador o continuador (se sigue jugando)

#Función que corre el juego completo
#esta función es la encargada de llevar el loop principal del juego
#aquí entra la combinación aleatoria
def juego(tab):
    #Se pregunta por pantalla cuánto jugadores intentarán adivinar la combinación
    can = int(input("¿Cuántos jugadores se presentan?: "))
    if can == 1:
        for e in list(range(0,16)):
            tabGam = tab #tabGam es la combinación secreta
            gem = jugador(can,tabGam) #Se da a correr la jugada del jugador
            if gem == True:
              #de devolverse una victoria, se corta el loop con break
                break
    if can == 2: #De ser dos jugadores, se hace correr el for cambiando
        #de forma alternativa de jugador 1 a 2. Comienza el 1
        turno = 1
        tuVer = False #se usa un verificador para ir cambiando de jugador
        #1 a 2 sin que la comprobación solo sea numérica
        for e in list(range(0,16)):
            if turno == 1: #El estilo de juego es el mismo
                print("Turno del jugador " + str(turno) + "\n")
                tabGam = tab
                gem = jugador(turno,tabGam)
                if gem == True:
                    break
                tuVer = False #se mantiene en falso el verificador
                turno = turno + 1 #dado que sigue el jugador 2, se suma 1
            if turno == 2:
                print("Turno del jugador " + str(turno) + "\n")
                tabGam = tab
                gem = jugador(turno,tabGam)
                if gem == True:
                    break
                tuVer = True #en este caso, para indicar que el jugador 2
                #ya movió, se utiliza el verificador en True
            if turno == 2 and tuVer == True: #Si el turno 2 ya pasó y el jugador 2 ya movió
                turno = turno - 1 #se devuelve el turno al jugador 1

#BLOQUE PRINCIPAL
#Se imprimen las instrucciones por pantalla
print("¡Bienvenido a Mastermind!\nColores disponibles: R,A,V,M,N\n")
print("INSTRUCCIONES:\n")
print("El número de intentos es 15")
print("Los datos se ingresan uno a uno en mayúscula")
print("De no usarse mayúscula o las letras permitidas, no se recibirá el intento")
print("Esto es, el sistema lo asumirá como nulo")
print("Se pedirán los colores en el siguiente formato:\n")
print("[POSICIÓN 1, POSICIÓN 2, POSICIÓN 3, POSICIÓN 4] \n")
print("¿Qué ficha pondrá en la posición n?: [Color que usted elija] \n")
print("Su objetivo es adivinar una combinación secreta del tipo:\n")
print("[V,N,N,A]")
print("\n Tome en cuenta: los colores pueden repetirse\n")
ver = True
#Se utiliza un loop para poder reiniciar el juego una vez acabados los intentos
#Mientras ver sea True, se seguirá jugando
while ver == True:
    tab = celTab() #se crea la combinación aleatoria
    da = juego(tab) #se corre el juego
    #al finalizar los intentos se muestra la respuesta correcta
    print("La respuesta correcta era: ")
    print(tab)
    print("¡Gracias por jugar! \n")
    print("¿Desea jugar de nuevo?\n")
    #se pregunta si se quiere seguir jugando
    seguir = input("Para seguir, ingrese 1. Para cerrar, ingrese 0: ")
    #de ser afirmativo, se reinicia el loop
    #de cerrar el programa, se pone sleep() a fin de que el final no sea abrupto
    sleep(2)
    if seguir == "0":
        ver = False #y se cambia ver a False para cerrar el loop del juego total
#SALIDA
#se imprime el aviso de que se cerrará el juego
print("¡Ha finalizado Mastermind!")
#se esperan 5 segundos y se cierra el juego
sleep(5)

    




            

        

        
    






