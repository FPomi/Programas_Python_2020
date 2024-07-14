import math
import random
import pickle
import os

import Menus_de_inicio
import Crear_nueva_sesion
import Diseño
import chat
import busqueda

from time import sleep


def Tilder ():
    
    #usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    
    pseudonimo_usuario = Menus_de_inicio.menu_principal ()
    
    while pseudonimo_usuario != "0":
    
        opcion = Menus_de_inicio.menu_usuario (pseudonimo_usuario)
    
        while opcion != "Cerrar sesion":
        
            if opcion == "Menu de chats":
                chat.menu_chats(pseudonimo_usuario)
    
            if opcion == "Menu de busqueda":
                busqueda.main_busqueda(pseudonimo_usuario)
            
            opcion = Menus_de_inicio.menu_usuario (pseudonimo_usuario)
        
        pseudonimo_usuario = Menus_de_inicio.menu_principál()
    
    
Tilder()