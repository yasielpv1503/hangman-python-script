import random

MAX_LIFE = 9


# LISTA DE COLORES PARA LA CONSOLA
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# TOMA UNA PELICULA ALEATORIA DEL FICHERO pelis.txt
def GET_PELI_RAMDON():
    f = open("pelis.txt", "r")
    array_pelis = f.readlines()
    n = random.randint(0, len(array_pelis) - 1)
    return array_pelis[n].rstrip().lower().lstrip()


# MESSAGE
def PRINT_TEXT(color, text):
    print(color + text + bcolors.ENDC)


# IMPRIME MENSAJES DE ADVERTENCIA
def NOOPTION(TEXT):
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.WARNING, "                " + TEXT + "                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")


# IMPRIME MENSAJES DE ERROR
def ERROR(TEXT):
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.FAIL, "                " + TEXT + "                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")


# IMPRIME MENSAJES DE FIN DE JUEGO, REINICIA EL JUEGO
def GAME_OVER():
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.FAIL, "                HAS PERDIDO!!!!!!!                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    MENU_PLAY()


# IMPRIME MENSAJES DE GANADO
def WINNER():
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.OKGREEN, "                FELICIDADES, HAS GANADO!!!!!!!                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    PRINT_TEXT(bcolors.OKBLUE, "                                                           ")
    MENU_PLAY()


# IMPRIME MENSAJES DE PRESENTACION
def WELCOME():
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.OKBLUE, "|              BIENBENIDO A AHORCADO-PELICULAS              |")
    PRINT_TEXT(bcolors.FAIL, "|                  por yasielpv1503@gmail.com                  |")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")


# IMPRIME MENSAJES DE DESPEDIDA
def BYE():
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.FAIL, "|                  GRACIAS POR JUGAR CONMIGO!              |")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")


# IMPRIME LAS REGLAS DEL JUEGO
def PLAY_RULES():
    PRINT_TEXT(bcolors.OKBLUE, "----------------------------------------------------------------------")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                                     |")
    PRINT_TEXT(bcolors.OKBLUE, "|                 EL JUEGO HA COMENZADO                               |")
    PRINT_TEXT(bcolors.OKBLUE, "|A continuacion te presentaremos el nombre de una pelicula,           |")
    PRINT_TEXT(bcolors.OKBLUE, "|usted dispone de 10 oportunidades para adivinar de que pelicula      |")
    PRINT_TEXT(bcolors.OKBLUE, "|se trata, debe ir entrando letra a letra, por cada letra aceptada    |")
    PRINT_TEXT(bcolors.OKBLUE, "|se ira completando la frase, si no acepta pierdes una oportunidad    |")
    PRINT_TEXT(bcolors.OKBLUE, "|si completa el nombre, usted gana, si se le agotan las oportunidades |")
    PRINT_TEXT(bcolors.OKBLUE, "|usted pierde                                                         |")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                                     |")
    PRINT_TEXT(bcolors.OKBLUE, "----------------------------------------------------------------------")


# IMPRIME MENU INICIAL DEL JUEGO
# 1 PARA INICIAR EL JUEGO
# 0 PARA SALIR
def MENU_PLAY():
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.OKBLUE, "|              - PARA INICIAR UN NUEVO JUEGO OPRIMA (1)    |")
    PRINT_TEXT(bcolors.OKBLUE, "|              - PARA SALIR (0)                            |")
    PRINT_TEXT(bcolors.OKBLUE, "|                                                          |")
    PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")

    OPT = str(raw_input("ENTRE UNA OPCION 0 o 1: "))
    if (OPT == "0"):
        BYE()
        exit(0)
    else:
        if (OPT == "1"):
            PLAY()
        else:
            NOOPTION("OPCION NO VALIDA")
            MENU_PLAY()


# FUNCION PARA ADICIONAR UN CHAR EN UNA POSICION EN LA PALABRA FANTASMA
def addChar(FILM, GOST, CHAR):
    F = ""
    for LETTER in FILM:
        F = F + LETTER + " "
    for index, value in enumerate(list(F)):
        if value == CHAR:
            GOST = GOST[:index] + CHAR + GOST[index + 1:]
    return GOST.upper()


# FUNCION PARA SUSTITUIR LOS CARACTERES ENTRADOS DEL NOMBRE DE LA PELICULA EN LA PALABRA FANTASMA
def COMPLETE_GHOST(FILM, LETTER_USED):
    GOST = ""
    for LETTER in FILM:
        if (LETTER == " "):
            GOST = GOST + "  "
        else:
            GOST = GOST + "_ "
    for CHAR in LETTER_USED:
        if CHAR in FILM:
            GOST = addChar(FILM, GOST, CHAR)

    if ("_" not in GOST):
        WINNER()
    return GOST


def CHECK_WINNER(FILM, LETTER_USED):
    GOST = ""
    for LETTER in FILM:
        if (LETTER == " "):
            GOST = GOST + "  "
        else:
            GOST = GOST + "_ "
    for CHAR in LETTER_USED:
        if CHAR in FILM:
            GOST = addChar(FILM, GOST, CHAR)
    if ("_" not in GOST):
        WINNER()
        return True
    return False


# FUNCION INICIA EL JUEGO
def PLAY():
    film = GET_PELI_RAMDON()
    PLAY_RULES()
    LETTER_USED = []
    LIFE = MAX_LIFE

    RUN(film, LETTER_USED, LIFE)


# FUNCION INICIA LA ENTRADA DE CARACTERES Y VA MOSTRANDO PROGRESO DEL JUEGO
def RUN(film, LETTER_USED, LIFE):
    if not CHECK_WINNER(film, LETTER_USED):
        PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")
        PRINT_TEXT(bcolors.OKCYAN, "| ")
        PRINT_TEXT(bcolors.WARNING, "|  PELICULA: " + COMPLETE_GHOST(film, LETTER_USED))
        PRINT_TEXT(bcolors.OKCYAN, "| ")
        PRINT_TEXT(bcolors.FAIL, "|  OPORTUNIDADES: " + str(LIFE))
        PRINT_TEXT(bcolors.FAIL, "|  LETRAS USADAS:" + ",".join(LETTER_USED))
        PRINT_TEXT(bcolors.OKCYAN, "| ")
        PRINT_TEXT(bcolors.OKBLUE, "-----------------------------------------------------------")
        OPT = str(raw_input("ENTRE UNA LETRA: "))

        if (len(OPT) != 1):
            NOOPTION("DEBE INSERTAR UN SOLO CARACTER!!!!!")
            RUN(film, LETTER_USED, LIFE)

        if (not OPT.isalnum()):
            NOOPTION("CARACTER NO VALIDA")
            RUN(film, LETTER_USED, LIFE)

        if OPT in LETTER_USED:
            NOOPTION("YA USO ESTE CARACTER, INTENTE CON OTRO!!!!!")
            RUN(film, LETTER_USED, LIFE)

        if OPT not in LETTER_USED:
            LETTER_USED.append(OPT)

        if OPT not in film:
            LIFE = LIFE - 1
            if LIFE == 0:
                GAME_OVER()
            else:
                ERROR("PERDISTES UNA OPORTUNIDAD!!!!!")
                RUN(film, LETTER_USED, LIFE)

        if (OPT == "0"):
            BYE()
            exit(0)
        else:
            if (OPT == "1"):
                PLAY()
            else:
                RUN(film, LETTER_USED, LIFE)


# INICIO AQUI!!!!!!!!!!
# TODO UN RETO @Joaquin!!!

WELCOME()
MENU_PLAY()
