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

foto_marco_superior = "╔═♥══════╗"
foto_marco_medio = '║'
foto_marco_inferior = "╚══════♥═╝"

foto1 = "( . ͜  .)"
foto2 =  " (´ ͜ʖ ´)"
foto3 = " (> ͜ʖ <)"
foto4 =  " (- ͜  -)"
foto5 = " (ᵔ ͜ʖ ᵔ)"
foto6 = " (♥ ͜ʖ ♥)"
foto7 =  " (* ͜ʖ *)"
foto8 = " ( `_´ )"
foto9 = "( * o *)"
foto10 = "( ► ͜ʖ ◄)"
foto11 = " (G ͜ʖ G)"
foto12 = "( ° ͜ʖ °)"
foto13 = "( e ͜ʖ e)"
foto14 = "( o ͜ʖ O)"
foto15 = "( ¬ ͜ʖ ¬)"
foto16 = " (U ͜ʖ U)"
foto17 = " (~ ͜ʖ ~)"
foto18 = "( ^ ͜ʖ ^)"
foto19 = "( ` ͜ʖ ´)"
foto20 = "( ~ ͜ʖ °)"


lista_fotos = [foto1, foto2, foto3, foto4, foto5, foto6, foto7, foto8, foto9, foto10, foto11, foto12, foto13, foto14, foto15, foto16, foto17, foto18, foto19, foto20]


def foto_usuarios(diccionario_usuarios, lista_fotos):

    # Función para mostrar una foto de perfil aleatoria para cada usuario durante la búsqueda de personas

    diccionario_fotos = {}
    fotos_no_disponibles = []
    contador = 0
    fotos_a_mostrar = []

    while contador != len(diccionario_usuarios):

        foto = random.choice(lista_fotos)

        if foto not in fotos_no_disponibles:

            fotos_a_mostrar.append(foto)
            fotos_no_disponibles.append(foto)
            contador += 1

    elemento = 0

    while elemento != len(fotos_a_mostrar) :

        for usuario in diccionario_usuarios:
        
            diccionario_fotos[usuario] = fotos_a_mostrar[elemento]
            elemento += 1


    return diccionario_fotos



"╔═♥══════╗"
"║( . ͜  .)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (´ ͜ʖ ´)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (> ͜ʖ <)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (- ͜  -)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (ᵔ ͜ʖ ᵔ)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (♥ ͜ʖ ♥)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (* ͜ʖ *)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ ( `_´ )║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( * o *)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ► ͜ʖ ◄)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (G ͜ʖ G)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ° ͜ʖ °)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( e ͜ʖ e)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( o ͜ʖ O)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ¬ ͜ʖ ¬)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (U ͜ʖ U)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║ (~ ͜ʖ ~)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ^ ͜ʖ ^)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ` ͜ʖ ´)║"
"╚══════♥═╝"
"╔═♥══════╗"
"║( ~ ͜ʖ °)║"
"╚══════♥═╝"