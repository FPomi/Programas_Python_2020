import os
import pickle

#-----------------------------------------------------------------------------------------------------------------------------#

def limpiar_pantalla():
    os.system('cls||clear')

#-----------------------------------------------------------------------------------------------------------------------------#

def imprimir_menu(datos, usuarios, pseudonimo_usuario):
    '''muestra los chats del usuario'''
    limpiar_pantalla()
    _,_,_,_,_,_,_,likes,_,_ = datos
    print ("CHATS")
    n = 1
    for pseudonimo_likeado in likes:
        if pseudonimo_usuario in usuarios[pseudonimo_likeado][7]:
            nombre = usuarios[pseudonimo_likeado][0]
            print (f"{n}) {nombre} - {pseudonimo_likeado}")
            n += 1
    if n == 1:
        print ("Nada por acá!")
        return 0
    else:
        return 1
 
#-----------------------------------------------------------------------------------------------------------------------------#

def buscar_pseudonimo(usuarios, datos, pseudonimo_usuario, vacio):
    '''devuelve el pseudonimo de la persona con quien el usuario quiere hablar o None si quiere volver al menu'''
    _,_,_,_,_,_,_,likes,chats,_ = datos

    if vacio == 0:
        chat_entrar = input("Presione '<' para volver atrás: ")
    else:
        chat_entrar = input("Eliga el nº del chat a entrar, o < para volver atrás: ")    

    invalido = True

    while (invalido):
        invalido = False
        
        if (chat_entrar.isnumeric() == False):
            invalido = True

        elif (int(chat_entrar) <= 0) or (int(chat_entrar) > len(chats)):
            invalido = True
        
        if chat_entrar == "<":
            invalido = False
            
        if invalido:
            chat_entrar = input ("Elección invalida, vuelva a intentar: ")
        
    resultado = None

    if chat_entrar != "<":
        n = 0
        m = 0
        while n < int(chat_entrar):
            if pseudonimo_usuario in usuarios[likes[m]][7]:
                resultado = likes[m]
                n += 1
            m += 1

    return resultado

#-----------------------------------------------------------------------------------------------------------------------------#

def mostrar_chat(usuarios, pseudonimo_usuario, pseudonimo_match):
    '''crea el archivo de texto del chat si es que todavia no existe, y muestra la conversacion existente'''

    limpiar_pantalla()
    print (f"Chat con {pseudonimo_match}\n")

    if usuarios[pseudonimo_usuario][-2][pseudonimo_match] == " ":
        usuarios[pseudonimo_usuario][-2][pseudonimo_match] = pseudonimo_usuario + "_" + pseudonimo_match + ".txt"
        usuarios[pseudonimo_match][-2][pseudonimo_usuario] = pseudonimo_usuario + "_" + pseudonimo_match + ".txt"

        ruta_archivo = pseudonimo_usuario + "_" + pseudonimo_match + ".txt"
    else:
        ruta_archivo = usuarios[pseudonimo_usuario][-2][pseudonimo_match]

    try:
        chat = open(ruta_archivo, "x")
        chat.close()

    except:
        #ya existe el archivo
        with open(ruta_archivo, "r") as chat:
            for linea in chat:
                print (linea)

#-----------------------------------------------------------------------------------------------------------------------------#

def mandar_mensajes(usuarios, ruta_archivo, pseudonimo_usuario, pseudonimo_match):
    '''manda mesnajes :)'''
    mensaje = input("Escribir mensaje, o < para volver atrás: ")
    while mensaje != "<":
        with open(ruta_archivo, 'a') as chat:
            if mensaje != "":
                chat.write(f'{pseudonimo_usuario}: {mensaje}\n')
        mostrar_chat(usuarios, pseudonimo_usuario, pseudonimo_match)
        mensaje = input("Escribir mensaje, o < para volver atrás: ")
    

#-----------------------------------------------------------------------------------------------------------------------------#

def chat(usuarios, pseudonimo_usuario, pseudonimo_match):
    #primero abro el chat y cargo los mensajes anteriores
    mostrar_chat(usuarios, pseudonimo_usuario, pseudonimo_match)

    #ahora permito que el usuario mande mensajes
    ruta_archivo = usuarios[pseudonimo_usuario][-2][pseudonimo_match]
    mandar_mensajes(usuarios, ruta_archivo, pseudonimo_usuario, pseudonimo_match)

#-----------------------------------------------------------------------------------------------------------------------------#

def menu_chats(pseudonimo_usuario):
    ''' menu de chats:   
        --------------------------------------------------------------------------
        CHATS
        1) nombre1 - pseudonimo1
        2) nombre2 - pseudonimo2
        3) nombre3 - pseudonimo3

        Ingrese numero de chat, o 0 para volver al menu principal: 
        --------------------------------------------------------------------------
    '''
    usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    
    seguir_chat = True
    
    while seguir_chat:
        datos = usuarios[pseudonimo_usuario]

        #imprimo el menu
        vacio = imprimir_menu(datos, usuarios, pseudonimo_usuario)

        #me fijo a que chat quiere entrar el usuario, o si quiere vovler al menu principal
        resultado = buscar_pseudonimo(usuarios, datos, pseudonimo_usuario, vacio)

        if resultado:
            pseudonimo_match = resultado

           #entro al chat
            chat(usuarios, pseudonimo_usuario, pseudonimo_match)
            seguir_chat = True

        else:
            seguir_chat = False
            
    pickle.dump(usuarios, open("Datos_Usuarios_Final.pkl", "wb"))

#-----------------------------------------------------------------------------------------------------------------------------#
