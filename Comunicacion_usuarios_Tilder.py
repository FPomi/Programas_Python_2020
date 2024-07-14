import os

lista_matchs = ["Juan","Pedro","Alonzo","Rodrigo"]
nombre_usuario = "Pomi"

#-----------------------------------------------------------------------------------------------------------#

def lista_contactos (lista_matchs):
   
    print ("Lista de Matchs \n")
   
    for i in range(len(lista_matchs)):
        print (i+1, ")", lista_matchs[i], "-", "Pseudonimo", "\n")
       
    print ("0 ) Volver al menu. \n")

#-----------------------------------------------------------------------------------------------------------#

def entrar_chat (lista_matchs):
    
    ruta_archivo = "D:/Franco/Documents/Facultad/TXT_programacion/Tilder"
    
    chat_entrar = input ("Elige el nº del chat a entrar: ")
    
    while (chat_entrar != "0"):
        
        invalido = True
        
        while (invalido):
            
            invalido = False
            
            if (chat_entrar.isnumeric() == False ):
                invalido = True
            else:
                chat_entrar_int = int (chat_entrar)
                
                if (chat_entrar_int < 0) or (chat_entrar_int > len(lista_matchs)+1):
                    invalido = True
            
            if (invalido):
                chat_entrar = input ("\n Chat invalido, ingrese otro numero: ")
   
        ruta_lectura = ruta_archivo + "/" + nombre_usuario + lista_matchs [chat_entrar_int-1] + ".txt"
        ruta_escritura = ruta_archivo + "/" + lista_matchs [chat_entrar_int-1] + nombre_usuario + ".txt"

        mostrar_chat (ruta_lectura, lista_matchs [chat_entrar_int-1])
        mandar_mensajes (ruta_escritura, ruta_lectura, nombre_usuario, lista_matchs [chat_entrar_int-1])
        
        chat_entrar = input ("Elige el nº del chat a entrar: ")
    
    print ("Volves al inicio")
       

#-----------------------------------------------------------------------------------------------------------#

def limpiar_pantalla():
    #os.system('cls||clear')
    print("\n\n\n")

#-----------------------------------------------------------------------------------------------------------#

def mostrar_chat(ruta_lectura, match):
    limpiar_pantalla ()
    
    print ("Chat con", match, ": \n")
    
    try:
        chat = open(ruta_lectura, "x")
        chat.close()
    
    except:
        #print ("Ya existe el archivo")
        with open(ruta_lectura, "r") as chat:
           for linea in chat:
                print (linea)

            

#-----------------------------------------------------------------------------------------------------------#

def mandar_mensajes(ruta_escritura, ruta_lectura, pseudonimo, match):
    mensaje = input("Escribir mensaje (presione solo Enter para salir): ")
    
    while mensaje:
        with open(ruta_escritura, 'a') as chat:
            chat.write(f'{pseudonimo}: {mensaje}\n')
            
        with open(ruta_lectura, 'a') as chat:
            chat.write(f'{pseudonimo}: {mensaje}\n')
            
        mostrar_chat(ruta_escritura, match)
        mensaje = input("Escribir mensaje: ")
    
    limpiar_pantalla()
    lista_contactos (lista_matchs)

#-----------------------------------------------------------------------------------------------------------#
       
def main ():
    lista_contactos (lista_matchs)
    entrar_chat (lista_matchs)

#-----------------------------------------------------------------------------------------------------------#

main()