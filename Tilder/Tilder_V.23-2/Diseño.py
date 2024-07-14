import random


tilder = ("........................................................................\n"
"................................OOO.....................................\n"
"..........II...............ZOOO.OOO..........OOO........................\n"
"..........IIII.......OOO....OO~.OOO..........OOO........................\n"
"....I....IIIIII......OOO........OOO..........OOO.....==............,....\n"
"...??I..IIIIIIII...8OOOOOO8.OOO.OOO..88OOOOO?OOO..O8OOOOOO,..OOOOOOO....\n"
"..??????I?IIIIII,...8OO....OOO.OOO.OOOO...8OOOO.OOO8..OOO8.OOOO8........\n"
"..???????????IIII....8OO....OOO.OOO.OOO.....?OOO+OO8.....OOO.OOO........\n"
".???????????II?I....8OO....OOO.OOO.OOO.....?OOO8OOOOOOOOOOO.OOO.........\n"
"..?????????????I.....8OO....OOO.OOO.OOO.....?OOOOOO?.........OOO........\n"
"...????????????+.....8OO....OOO.OOO.OOO8....OOOO.OOO?....?8..OOO........\n"
"....??????????........OOOOO.OOO.OOO..OOOOOOOOOOO..OOOOOOOOOO.OOO........\n"
"......,I???:...........8O8............8OOO..$$$.....O88O................\n"
"........................................................................\n"
"............................................................v1.0........\n"
"........................................................................\n")


perfil_horizontal = "═"
perfil_vertical = "║"
perfil_costado_derecha_superior = "╔"
perfil_costado_derecha_inferior = "╚"
perfil_costado_izquierda_superior = "╗"
perfil_costado_izquierda_inferior = "╝"

foto1 = "( . ᴗ .)"
foto2 =  "(´ ᴗ ´)"
foto3 = "(> ᴗ <)"
foto4 =  "(- ᴗ -)"
foto5 = "(ᵔ ᴗ ᵔ)"
foto6 = "(♥ ᴗ ♥)"
foto7 =  "(* ᴗ *)"
foto8 = "( `_´ )"
foto9 = "( * o *)"
foto10 = "( ► ᴗ ◄)"
foto11 = "( G ᴗ G)"
foto12 = "(° ᴗ °)"
foto13 = "( e ᴗ e)"
foto14 = "( o ᴗ O)"
foto15 = "( ¬ ᴗ ¬)"
foto16 = "(U ᴗ U)"
foto17 = "(~ ᴗ ~)"
foto18 = "(^ ᴗ ^)"
foto19 = "(` ᴗ ´)"
foto20 = "(~ ᴗ °)"


lista_fotos = [foto1, foto2, foto3, foto4, foto5, foto6, foto7, foto8, foto9, foto10, foto11, foto12, foto13, foto14, foto15, foto16, foto17, foto18, foto19, foto20]


foto_derecha_superior = "╔═♥"
foto_izquierda_superior = "╗"
foto_derecha_inferior = "╚"
foto_izquierda_inferior = "♥═╝"
marco_vertical = "║"
marco_horizontal = "═"


def galeria(diccionario_usuarios):
    
    fotos_no_disponibles = []

    for usuario in diccionario_usuarios:

        fotos_no_disponibles.append(diccionario_usuarios[usuario][9])


    fotos_a_mostrar = []

    if len(fotos_no_disponibles) < 19:

        for foto in lista_fotos:

            if foto not in fotos_no_disponibles:

                fotos_a_mostrar.append(foto)
                fotos_a_mostrar = fotos_a_mostrar[0:2]

    else:

        while len(fotos_a_mostrar) < 2:

            foto = random.choice(lista_fotos)

            if foto not in fotos_a_mostrar:

                fotos_a_mostrar.append(foto)
    
    fotos_no_disponibles.clear()

    return fotos_a_mostrar







"╔═♥══════╗"
"║( . ᴗ .)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (´ ᴗ ´)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (> ᴗ <)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (- ᴗ -)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (ᵔ ᴗ ᵔ)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (♥ ᴗ ♥)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (* ᴗ *)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ ( `_´ )║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( * o *)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ► ᴗ ◄)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( G ᴗ G)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (° ᴗ °)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( e ᴗ e)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( o ᴗ O)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ¬ ᴗ ¬)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (U ᴗ U)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (~ ᴗ ~)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (^ ᴗ ^)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (` ᴗ ´)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (~ ᴗ °)║"
"╚══════♥═╝"