#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random,os,time,string



# dibuixem les taules dels dos jugadors.
def inicialitzar_taulells():
    taulell_jugador = []
    taulell_maquina = []
    for i in range(12):
        taulell_fila_jugador = []
        taulell_fila_maquina =[]
        for j in range(12):
            taulell_fila_jugador.append(" ")
            taulell_fila_maquina.append(" ")
        taulell_jugador.append(taulell_fila_jugador)    
        taulell_maquina.append(taulell_fila_maquina)


    for i in range(12): ## dubuixem a les files no visibles a la taula jugador per a que la màquina faci la seva funcó.
        taulell_jugador[0][i] = "A"
        taulell_jugador[11][i] = "A"
        taulell_jugador[i][0] = "A"
        taulell_jugador[i][11] = "A"
        
        
    return  taulell_jugador, taulell_maquina



## mostrem les taules ordenadament.
def mostrar_taulells(taulell_jugador, taulell_maquina):
    print "  ", ("=")*141
    print "  ", (" ")*60, "ENFONZAR LA FLOTA"
    print "  ", ("=")*141
    print " ",
    for i in range(10):
        print "    " + str(i+1) + "",
    print "                  ",
    for i in range(10):
        if i != 9:
            print "    " + str(i+1) + "",
        else:
            print "    " + str(i+1) + ""
    print "   -------------------------------------------------------------                   -------------------------------------------------------------"
    for i in range(10):
        # mostrem els numeros verticals de la primera taula.
        if i != 9: 
            print str(i+1) + "  | ",
        else:
            print str(i+1) + " | ",

        # mostrem el taulell del jugador ordenadament.
        for j in range(10):

            if taulell_jugador[i+1][j+1] in range(10):
                print chr(27)+"[92m"+"B" +chr(27)+"[0m",
            elif taulell_jugador[i+1][j+1] == "T":
                print chr(27)+"[93m"+"X" +chr(27)+"[0m",
            elif taulell_jugador[i+1][j+1] == "E":
                print chr(27)+"[91m"+"X" +chr(27)+"[0m",
            elif taulell_jugador[i+1][j+1] == "A":
                print chr(27)+"[96m"+"A" +chr(27)+"[0m",                
            else:
                print " ",
            """
            print taulell_jugador[i+1][j+1],
            """
            print " | ",
        # mostrem els numeros verticals de la segona taula
        print "             ",
        if i != 9: 
            print str(i+1) + "  | ",
        else:
            print str(i+1) + " | ",
        
        # mostrem el taulell de la màquina ordenadament.
        
        for j in range(10):
            """
            if taulell_maquina[i+1][j+1] in range(10):
                print chr(27)+"[92m"+"B" +chr(27)+"[0m",
            """
            if taulell_maquina[i+1][j+1] == "T":
                print chr(27)+"[93m"+"X" +chr(27)+"[0m",
            elif taulell_maquina[i+1][j+1] == "E":
                print chr(27)+"[91m"+"X" +chr(27)+"[0m",
            elif taulell_maquina[i+1][j+1] == "A":
                print chr(27)+"[96m"+"A" +chr(27)+"[0m",                
            else:
                print " ",
            """
            print taulell_maquina[i+1][j+1],
            """
            print " | ",        
        print u""
        
        # afegim les linies horitzontals que separen les dues fileres.
        if i != 10:
            print u"   -------------------------------------------------------------                   -------------------------------------------------------------"



## funció per poder triar vaixell i protegir l'entrada de dades errònies.
def triar_vaixell():
    while True:
        vaixell_triat = ""
        tipus_vaixell = raw_input("   tria un vaixell: ")
        if tipus_vaixell.isdigit(): # comprovem si és un digit.
            tipus_vaixell = int(tipus_vaixell)
            if tipus_vaixell >= 1 and tipus_vaixell <=4: # guarda en la variable "tipus_vaixell" el tipus de vaixell triat.
                if tipus_vaixell == 1:
                    vaixell_triat = "submarins"
                elif tipus_vaixell == 2:
                    vaixell_triat = "fragates"
                elif tipus_vaixell == 3:
                    vaixell_triat = "portaavions"
                elif tipus_vaixell == 4:
                    vaixell_triat = "destructor"
                return vaixell_triat
            else:
                print u"   Entrada no permesa. Utilitza valors numèrics entre l'1 i el 4.\n "
        else:
            print u"   Entrada no permesa. Utilitza valors numèrics entre l'1 i el 4.\n "



## funció per afegir els vaixells a la taula, pot ser de forma automàtica o no. Aquesta funció es compartit amb l'usuari i la màquina.
def afegir_vaixells(taulell_primari, taulell_secundari, vaixells, auto):
    # en el diccionari "cuantitat" allotja el número de vaixells que disposem, i cada vegada que treim un vaixell doncs es esborrat de la llista.
    cuantitat = {"submarins":4, "fragates":3, "portaavions":2,"destructor":1}
    identificador = -1
    while cuantitat["submarins"]!= 0 or cuantitat["fragates"]!= 0 or cuantitat["portaavions"]!= 0 or cuantitat["destructor"]!= 0: # si la llista es buida (quan ja hem afegit tot els vaixells) no s'executará aquest bucle.

        
        if auto == "N": ## si triem posar els vaixells manualment cridadà les funciosn de triar_coordenades, validar_coordenades, validar_posicio
            print "   ---------------------------------------------------------------------------------------------------------------------------------------------"        
            print "   | 1) submarins    |",cuantitat["submarins"],"|", (" ")*34,"# #  ( )", (" ")*71, "|"
            print "   -----------------------", (" ")*36,"___#_#___|__", (" ")*65, "-\n   | 2) fragates     |",cuantitat["fragates"],"|", (" ")*32,"_  |____________|  _", (" ")*61, "|"
            print "   -----------------------", (" ")*25,"_=====| | |            | | |==== _", (" ")*54, 
            print "-\n   | 3) portaavions  |",cuantitat["portaavions"],u"|                     =====| |.---------------------------. | |====                         -═════>", (" ")*17, "|"
            print "   -----------------------       <--------------------'   .  .  .  .  .  .  .  .   '--------------/", (" ")*42, "-\n   | 4) destructor   |",cuantitat["destructor"],"|         \ ",
            print (" ")*57," /", (" ")*43, "|"
            print "   ---------------------------------------------------------------------------------------------------------------------------------------------"        
            while True:
                vaixell_triat = triar_vaixell() # cridem la funció triar_vaixell i la dada retornada s'emmagatzema a la corresponent vaiable.
                if cuantitat[vaixell_triat] > 0: # si la vairable es troba a la llista "cuantitat" doncs sortim del bucle.
                    break
                else:
                    print "   Ja no queden ", vaixell_triat # mostrem un missatge i tornem a triar.
            vaixell = vaixells[vaixell_triat] # en el main es troba una llista de diccionaris, on apareix el tipus de vaixell i la cuantitat de posicions que li correspon.
            validar = False 
            while not validar:
                
                x, y = triar_coordenades() # cridem aquesta funció i el que retorna seran les coordenades
                if vaixells[vaixell_triat] != 1:
                    ori = vertical_o_horitzontal() # triem en quina direcció serà col.locada.
                else:
                    ori = "h" # si el vaixell ocupa 1 casella no caldrà especificar la orientació
                validar = validar_posicio(taulell_primari,vaixell,x,y,ori) # cridem aquesta funció i comprovem si es pot afegir el vaixell a les coordenades i orientació establertes.
                if not validar:
                    print u"   No es pot posar un vaixell aquí. Si us plau, mireu la taula i intenta-ho de nou.\n"
                validar = validar_posicio(taulell_primari,vaixell,x,y,ori)  
        else: ## si tria l'usuari posar els vaixells aleatoriament doncs farà el mateix que la màquina
            while True:
                for vaixell_triat in vaixells.keys(): # agafa la clau i desprès comprova si es tova a la llista cuantitat, si es així doncs trenca el bucle.
                    if cuantitat[vaixell_triat] > 0:
                        break
                break       

            validar = False
            while not validar:
                vaixell = vaixells[vaixell_triat]
                x = random.randint(1,10)
                y = random.randint(1,10)
                z = random.randint(0,1)
                if z == 0: 
                    ori = "v"
                else:
                    ori = "h"
                validar = validar_posicio(taulell_primari,vaixell,x,y,ori)
        identificador += 1
        taulell_primari = posar_vaixell(taulell_primari,vaixell,ori,x,y, identificador) # una vegada sortit del bucle dibuixem el vaixell al taulell del jugador.
        cuantitat[vaixell_triat] -= 1 # una vegada dibuixat, eliminem el vaixell de la llista "cuantitat".
        if auto == "N":
            os.system("cls")
            mostrar_taulells(taulell_primari, taulell_secundari)
        

    return taulell_primari



## dibuixar vaixell.
def posar_vaixell(taulell_usuari,vaixell,ori,x,y, identificador):
    ## es dibuixa el vaixell horitzontalment o verticalment.
    if ori == "v":
        for i in range(vaixell):
            taulell_usuari[x+i][y] = identificador # cada vaixell tindrà el seu identificador en número (d'aqueta manera comprova si encara és enfonzat o no)
    elif ori == "h":
        for i in range(vaixell):
            taulell_usuari[x][y+i] = identificador

    return taulell_usuari



## comprova si la posició triada respecta el joc.
def validar_posicio(taulell_usuari,vaixell,x, y,ori):

    if ori == "v" and x+vaixell > 11: # si sobrepassa retorna False i tires de nou les coordenades
        return False
    elif ori == "h" and y+vaixell > 11:
        return False
    else:
        if ori == "h":
        
            for fil in range(x-1, x+2): # comprova si hi ha un digit al voltant (diferent de " " i A)
                for col in range(y-1, y+vaixell + 1 ):
                    if taulell_usuari[fil][col] != " " and taulell_usuari[fil][col] != "A":
                        return False

        else:
            for fil in range(x-1, x+vaixell +1):
                for col in range(y-1, y+2):
                    if taulell_usuari[fil][col] != " " and taulell_usuari[fil][col] != "A":
                        return False

    return True 




def triar_coordenades():
    while True:
        entrada_usuari = raw_input("   Introdueixi les coordenades (FILA.COLUMNA)? ")
        try:
            # comprovem si l'usuari ha afegit en 2 valors separats per un coma.
            coor = entrada_usuari.split(".")
            if len(coor) != 2:
                raise Exception("   Entrada no permesa. Introdueix correctament les coordenades.\n ");

            # convertim els números en enters.
            coor[0] = int(coor[0])
            coor[1] = int(coor[1])

            # comprovem si les coordenades es troben en un determinat rang.
            if coor[0] > 10 or coor[0] < 1 or coor[1] > 10 or coor[1] < 1:
                raise Exception("   Entrada no permesa. Utilitza valors entre l'1 i el 10.\n ")

            # retornem les coordenades.
            return coor
        
        except ValueError:
            print u"   Entrada no permesa. Introdueixi només valors numèrics per a les coordenades.\n "
        except Exception as missatge:
            print missatge




def vertical_o_horitzontal():

    # si l'usuari tria posar els vaixells manualment el joc demanarà la orientació.
    while True:
        entrada_usuari = raw_input("   vertical o horitzontal (V/H)? ")
        entrada_usuari = entrada_usuari.lower()
        if entrada_usuari == "v" or entrada_usuari == "h":
            return entrada_usuari
        else:
            print u"   Entrada no permesa. Introdueixi únicament v o h.\n "         




def comprovar_tirada(taulell_primari,x,y):
    
    # comprova si s'ha colpejat o no
    if taulell_primari[x][y] == " ":
        return "aigua"
    # triarà de nou perque ja han sigut colpejades aquestes posicions.
    elif taulell_primari[x][y] == 'A' or taulell_primari[x][y] == 'T' or taulell_primari[x][y] == 'E':
        return "errat"
    else:
        return "tocat"



def comprovar_enfonzament(taulell_primari, num_vaixell):
    # si troba un número més del identificador doncs encara no s'ha enfonsat
    for i in range(12):
        for j in range(12):
            if taulell_primari[i][j] == num_vaixell:
                return False
                
    return True



## funció on conté les funcions comprovar_tirada, aigua_recursiva i comprovar enfinsament, 
def tirada_usuari(taulell_primari,x,y, taulell_jugador):
    global vida_maquina, vida_jugador
    while True:

        res = comprovar_tirada(taulell_primari,x,y)
        if res == "tocat": # si al comprovar tirada es tocat doncs la coordenada es converteix en "T" i comprova si s'ha enfonsat.
            print("   El missil dirigit a la coordenada " + str(x) + "." + str(y) + " ha colpejat el vaixell.")
            num_vaixell = int(taulell_primari[x][y])
            taulell_primari[x][y] = 'T'
            if comprovar_enfonzament(taulell_primari, num_vaixell) == True:
                if taulell_primari == taulell_jugador: # si és així resta la vida del jugador enfonsat.
                    vida_jugador -= 1
                else:
                    vida_maquina -= 1
                print "   Felicitats, has enfonzat el vaixell!"
                aigua_recursiva(taulell_primari,x,y) # executa la funció on s'envolta d'aigua.
            taulell_primari[x-1][y+1] = 'A'
            taulell_primari[x+1][y-1] = 'A'
            taulell_primari[x+1][y+1] = 'A'
            taulell_primari[x-1][y-1] = 'A'
            raw_input("\n   Prem INTRO per visualitzar el resultat.")
            return True
        elif res == "aigua":
            raw_input("   El missil dirigit a la coordenada " + str(x) + "." + str(y) + " ha caigut a l'aigua.\n\n   Prem INTRO per visualitzar el resultat.")
            taulell_primari[x][y] = "A"
            return False
        elif res == "errat":
            print u"   Aquesta coordenada ja va ser colpejada. Torna a llençar el missil.\n "
            raw_input("   Prem INTRO per continuar.")

            return True



## funció recursiva per dibuxar la A d'aigua.
def aigua_recursiva(taulell_primari,x,y):
    if taulell_primari[x][y] == "T": ## si es confonsat doncs converteix la "T" en "E" i s'envolta d'aigua.
        taulell_primari[x][y] = "E"
        if taulell_primari[x-1][y] == " " or taulell_primari[x-1][y] == "A":
            taulell_primari[x-1][y] = "A"
        if taulell_primari[x-1][y]  == "T":
            aigua_recursiva(taulell_primari,x-1,y)
            
        if taulell_primari[x-1][y-1] ==  " " or taulell_primari[x-1][y-1] == "A":
            taulell_primari[x-1][y-1]= "A"
        if taulell_primari[x-1][y-1] == "T":
            aigua_recursiva(taulell_primari,x-1,y-1)
            
        if taulell_primari[x][y-1] ==  " " or taulell_primari[x][y-1] =="A":
            taulell_primari[x][y-1] = "A"
        if taulell_primari[x][y-1] == "T":
            aigua_recursiva(taulell_primari,x,y-1)
            
        if taulell_primari[x+1][y-1] ==  " " or taulell_primari[x+1][y-1] == "A":
            taulell_primari[x+1][y-1] ="A"
        if taulell_primari[x+1][y-1] == "T":
            aigua_recursiva(taulell_primari,x+1,y-1)
            
        if taulell_primari[x+1][y] ==  " " or taulell_primari[x+1][y] == "A":
            taulell_primari[x+1][y] ="A"
        if taulell_primari[x+1][y] == "T":
            aigua_recursiva(taulell_primari,x+1,y)
            
        if taulell_primari[x+1][y+1] ==  " " or taulell_primari[x+1][y+1] =="A":
            taulell_primari[x+1][y+1] ="A"
        if taulell_primari[x+1][y+1] == "T":
            aigua_recursiva(taulell_primari,x+1,y+1)
            
        if taulell_primari[x][y+1] ==  " " or taulell_primari[x][y+1] == "A":
            taulell_primari[x][y+1] ="A"
        if taulell_primari[x][y+1] == "T":
            aigua_recursiva(taulell_primari,x,y+1)
            
        if taulell_primari[x-1][y+1] ==  " " or taulell_primari[x][y+1] == "A":
            taulell_primari[x-1][y+1] ="A"
        if taulell_primari[x-1][y+1] == "T":
            aigua_recursiva(taulell_primari,x-1,y+1)    



## funció per comprovar el guanyador, és executat en la funció tirada usuari
def comprovar_guanyador(taulell_primari):
    ## si no conté nungun número doncs vol dir què s'ha enfonsat tots els vaixells.
    for i in range(12):
        for j in range(12):
            if taulell_primari[i][j] != " " and taulell_primari[i][j] != 'A' and taulell_primari[i][j] != 'E' and taulell_primari[i][j] != 'T':
                return False
    return True




def menu():
    os.system("cls")
    print "  ", ("=")*141
    print u"                                                                    MENÚ                                                                        "
    print "  ", ("=")*141
    print "   ---------------------------------------------------------------------------------------------------------------------------------------------"
    print "   | 1) Jugar una partida", (" ")*24, "|", (" ")*38, "# #  ( )", (" ")*41, "|"
    print "   -------------------------------------------------", (" ")*40, "___#_#___|__", (" ")*35, "-\n   | 2) Mostrar el Top-5 dels millors jugadors     |",
    print (" ")*36, "_  |____________|  _", (" ")*31, "|"
    print "   -------------------------------------------------", (" ")*29, "_=====| | |            | | |==== _", (" ")*24, "-\n   | 3) Com s'hi juga?", (" ")*27, "|", 
    print (" ")*25, "=====| |.---------------------------. | |====", (" ")*17, "|"
    print "   -------------------------------------------------           <--------------------'   .  .  .  .  .  .  .  .   '--------------/",
    print (" ")*12, "-\n   | 4) Sortir i guardar ranking en un fitxer.", (" ")*3, "|             \ ", (" ")*57, " /", (" ")*13, "|"
    print "   ---------------------------------------------------------------------------------------------------------------------------------------------"
    
    # demanem una opció i només acceptem valors entre 1 i 3.
    opcio = '5'
    while not opcio.isdigit() or int(opcio) < 1 or int(opcio) > 4:
        print u"   Què vols fer? ",
        opcio = raw_input()

    return opcio    


## funció que afegeix el guanyador en un diccionari.
def afegir_ranking(nom, num, ranking):
    if (nom in ranking and ranking[nom] < num): # si el jugador es troba en el diccionari ranking i té major puntuació, doncs canvía de valor.
        ranking[nom] = num
    elif nom not in ranking: # si no es troba comprova si hi ha menys de 5 guanyadors, si és així doncs s'afegeix.
        if len(ranking) < 5:
            ranking[nom] = num
        else: # sino, comprova si la puntuació es major al últim jugador del ranking. 
            minim = min(ranking.values()) # agafa el número minim.
            if minim < num: # si el número minim és menor al número del jugador doncs vol dir què té una major puntuació.
                claus = ranking.keys()
                for clau in claus:
                    if ranking[clau] == minim: # serà eliminat l'últim del ranking.
                        ranking.pop(clau)
                        ranking[nom] = num
                        break
    return ranking



## funció que mostra els guanyadors, es executat en el main.
def mostrar_ordenat(ranking):
    print "  ", ("=")*141
    # print "  ", (" ")*61, "RANKING"
    print "  ", ("=")*141
    j = 0
    missatge = "   Ets el primer jugador!!!"
    try:
        dades = ranking.items()
        if len(dades) > 0:
            dades.sort(key=lambda x: x[1]) # ordenem de menor a major.
            dades.reverse() # revertim els números.
            for clau in dades:
                j += 1
                print "\n", (" ")*48, u"█████████████ GUANYADOR Nº" + str(j) + u" █████████████\n"
                print (" ")*48, "NOM DEL JUGADOR:     " ,clau[0]
                print (" ")*48, "RONDES GUANYADES:    " ,clau[1]
                print 
        else:
            print missatge
    except:
        print missatge
        

## es executar cuan sortim del joc,
def desar_dades(ranking, fitxer):
    try:
        arxiu = open(fitxer, "w")
        claus = ranking.keys()
        for clau in claus: # escrivim els guanyadors a l'arxiu.
            arxiu.write(clau + '\t' + str(ranking[clau]) + '\n')
        arxiu.close()
    except:
        None



## es executat al principi del main. 
def carregar_ranking(arxiu):
    ranking = dict() ## el carrega en un diciconari 
    try:
        arxiu = open(arxiu, "r")
        for line in arxiu:
            nom, valor = line.split('\t')
            ranking[nom] = int(valor[:-1])
        arxiu.close()
        return ranking
    except IOError as e:
        return ranking




## mostra la vida dels jugadors, 
def mostrar_vida(vida_jugador, vida_maquina):

    print "   | flota del jugador",
    for i in range(10):

        if i < vida_jugador:
            print chr(27)+"[2;31;40m"+u"███" +chr(27)+"[0m",
        else:
            print "   ",
    print u"|                   | flota de l'enemic",

    for i in range(10):
        if i < vida_maquina:
            print chr(27)+"[1;33;40m"+u"███" +chr(27)+"[0m",
        else:
            print "   ",
    print u"|\n   -------------------------------------------------------------                   -------------------------------------------------------------"




def intel_maquina(x_maquina,y_maquina, taulell_jugador):
    
    global sw_inicial, dalt, baix, esquerra, dreta, aleatori, y_inicial, x_inicial
    if taulell_jugador[x_maquina][y_maquina] == "T" or aleatori == False: ## si es tocat un vaixell doncs la vaariable aleatori és tancat i sw_inicial guarda les coordenades inicials (1 vegada)
        aleatori = False
        if sw_inicial == 1:
            y_inicial = y_maquina
            x_inicial = x_maquina
            sw_inicial -= 1
        if dalt == 1: ## si la posició triada es aigua es aigua doncs executa el seguent if
            if taulell_jugador[x_maquina][y_maquina] == "A" or taulell_jugador[x_maquina -1][y_maquina] == "A" :
                dalt = 0
                baix = 1
                x_maquina = x_inicial
                y_maquina = y_inicial
            else:

                x_maquina -= 1
            
        if baix == 1:
            if taulell_jugador[x_maquina][y_maquina] == "A" or taulell_jugador[x_maquina +1][y_maquina] == "A" :
                baix = 0
                esquerra = 1
                x_maquina = x_inicial
                y_maquina = y_inicial
            else:

                x_maquina += 1

        if esquerra == 1:
            if taulell_jugador[x_maquina][y_maquina] == "A" or taulell_jugador[x_maquina][y_maquina -1] == "A" :
                esquerra = 0
                dreta = 1
                x_maquina = x_inicial
                y_maquina = y_inicial
            else:

                y_maquina -= 1
            
        if dreta == 1:
            if taulell_jugador[x_maquina][y_maquina] == "A" or taulell_jugador[x_maquina][y_maquina +1] == "A" :
                dreta = 0

            else:   
                y_maquina += 1
    if taulell_jugador[x_maquina][y_maquina] == "E" and aleatori == False: ## si es enfonsat el vaixell doncs acrivem el aleatori.
        aleatori = True # posem els variables en el seu estat incial.
        sw_inicial = 1
        dalt = 1
        baix = 0
        esquerra = 0
        dreta = 0
        
    if aleatori == True: ## si la posició tirada aleatoriament són els seguent seguirà del bucle fins que sigui un espai.
        while taulell_jugador[x_maquina][y_maquina] == "E" or taulell_jugador[x_maquina][y_maquina] == "A"  or taulell_jugador[x_maquina][y_maquina] == "T":
            x_maquina = random.randint(1,10)
            y_maquina = random.randint(1,10)
    return x_maquina, y_maquina



## variables globals,
vida_jugador = 10
vida_maquina = 10
sw_inicial = 1
dalt = 1
baix = 0
esquerra = 0
dreta = 0
y_inicial = 0
x_inicial = 0
aleatori = True

def main():
    global vida_maquina, vida_jugador, sw_inicial, dalt, baix, esquerra, dreta, aleatori, y_inicial, x_inicial ## variables globals 
    os.system("mode con cols=147 lines=50") ## amplada i allagada del terminal.
    os.system("title ENFONZAR LA FLOTA")

    rondes_ranking = 0 ## són les rondes del jugador (si el jugador es troba en el diccionari guanyadors doncs agafarà la dada de partides guanyades)
    cont = 1 ## contador per a que carregui una vegada el ranking.txt.

    while True: ## quest bucle infinit serveix per tornar al menú.
        opcio = '5'
        while opcio >= '4':
            if cont == 1:
                ranking = carregar_ranking("ranking.txt")
                cont -= 1

            # cridem a la funció menu i fem una cosa o altre en funció del valor retornat
            opcio = menu()
            if opcio == '1': ## si triem jugar.
                
                os.system("cls")
                print "  ", ("=")*141
                print "  ", (" ")*60, u"CONFIGURACIÓ INICIAL"
                print "  ", ("=")*141
                if rondes_ranking == 0: ## si rondes_ranking es 0 doncs:
                    nom_jugador = raw_input("   Introdueix el teu nom: ") ## comencem el joc escrivint el nom.
                    nom_jugador = nom_jugador.upper()
                    if nom_jugador in ranking: ## s el nom del jugador introduit es troba en el diccionari doncs agafarà la dada de rondes guanyades.
                        rondes_ranking = ranking[nom_jugador]
                else:
                    print u"   Utilitzaràs el mateix nom de la partida anterior.\n"
                auto = "R"
                while auto != "S" and auto != "N": ## triem si posar els vaixells aleatoriament o no.
                    auto = raw_input("   Vols posar els vaixells aleatoriament (s/n)? ")
                    auto = auto.upper()
                os.system("cls")
                nom_maquina = "MR.ROBOT" 

                vaixells = {"destructor":4, "portaavions":3, "fragates":2, "submarins":1} ## cuantitat de vaixells.
                taulell_jugador, taulell_maquina = inicialitzar_taulells()
                if auto == "N": ## es visualitzarà els taulells buits per colocar els vaixells.
                    mostrar_taulells(taulell_jugador, taulell_maquina)


                for i in range(1):
                    taulell_jugador = afegir_vaixells(taulell_jugador, taulell_maquina, vaixells, auto) ## esecutem una vegada el colocament dels vaixells.

                for i in range(1): ## la màquina sempre ha de posar els vaixells aleatoriament.
                    auto = "S"
                    taulell_maquina = afegir_vaixells(taulell_maquina ,taulell_jugador , vaixells, auto)

                os.system("cls")
                mostrar_taulells(taulell_jugador, taulell_maquina)
                mostrar_vida(vida_jugador, vida_maquina)

                ## vairables globals.
                x_maquina = random.randint(1,10)
                y_maquina = random.randint(1,10)
                torn = 1
                sw_inicial = 1
                dalt = 1
                baix = 0
                esquerra = 0
                dreta = 0
                aleatori = True
            
                while True:
                    if torn % 2: # comença el jugador
                        print "   TORN DE ",nom_jugador
                        x,y = triar_coordenades()
                        if tirada_usuari(taulell_maquina,x,y, taulell_jugador) == False: ## si perd doncs el seguent torn serà del contrincant.
                            torn += 1

                    else:
                        print "   TORN DE ",nom_maquina

                        if tirada_usuari(taulell_jugador,x_maquina,y_maquina, taulell_jugador) == False:
                            torn += 1
                        x_maquina, y_maquina = intel_maquina(x_maquina,y_maquina, taulell_jugador)
  
                    os.system("cls")
                    mostrar_taulells(taulell_jugador, taulell_maquina)
                    mostrar_vida(vida_jugador, vida_maquina)



                    if comprovar_guanyador(taulell_jugador): ## comprova guanyador i posa les vides a 10.
                        print u"   Accepta-ho, que ha perdut!\n\n   Prem INTRO per tornar al menú."
                        raw_input("   ")
                        vida_jugador = 10
                        vida_maquina = 10
                        break
                    elif comprovar_guanyador(taulell_maquina):
                        print "   Has guanyat!\n "
                        rondes_ranking += 1 ## si guanyem sumem el ranking i l'afegim al diccionari.
                        ranking = afegir_ranking(nom_jugador,rondes_ranking, ranking)
                        if nom_jugador  in ranking:
                            print "   Guanyador afegit al Top-5.\n"
                            print "   Recorda, has de premar 4 (sortir) per actualitzar el fitxer ranking.txt"
                        else:
                            minim = min(ranking.values())
                            print u"   Necesites", (minim - rondes_ranking + 1), "rondes per accedir al Top-5."
                        print u"\n   Prem INTRO per tornar al menú."
                        raw_input("   ")
                        vida_jugador = 10
                        vida_maquina = 10                               
                        break

            elif opcio == '2': ## si l'opció triada es mostrar el ranking, doncs cridem la funció mostrar_ranking.
                os.system("cls")
                mostrar_ordenat(ranking)
                print u"\n   Prem INTRO per tornar al menú."
                raw_input("   ")
            elif opcio == "3":
                os.system("cls")
                print "  ", ("=")*141
                print "  ", (" ")*61, "COM S'HI JUGA?"
                print "  ", ("=")*141

                print u"\n     Cada jugador té un taulell 10x10 on col·loca els seus vaixells sense que es toquin entre elles. Al seu torn, indica una coordenada,"
                print u"     que es refereix a l'eix de les coordenades 'x,y'. Si ha encertat una posició on hi ha un vaixell, s'indicarà 'tocat' s'envoltarà"
                print u"     d'aigua les cantonades i si no és així, 'aigua'. Quan s'enfonsa un vaixell concret, s'indica amb la paraula 'enfonsat' i s'envoltarà"
                print u"     d'aigua tot el vaixell. Tenint en compte les distribucions possibles cal enfonsar tots els vaixells abans de perdre els propis."
                print u"     Si has tocat o enfonsat un vaixell tindràs una tirada més fins que fallis.  "

                print u"\n     Els vaixells que disposen els jugadors són els següents:"
                print u"""
                -----------------------------------
                | submarins    |    de 4 peces    |
                -----------------------------------
                | fragates     |    de 3 peces    |
                -----------------------------------
                | portaavions  |    de 2 peces    |
                -----------------------------------
                | destructor   |    d'1 peça      |
                -----------------------------------
                """
                print u"\n   Prem INTRO per tornar al menú."
                raw_input("   ")
            elif opcio == '4':
                desar_dades(ranking, "ranking.txt")
                print "   A reveure!"
                exit()


                
if __name__ == "__main__":
    main()
    raw_input("\nPrem INTRO per sortir!")