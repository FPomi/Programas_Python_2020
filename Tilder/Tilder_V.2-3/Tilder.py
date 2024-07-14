import pickle

import Menus_de_inicio
import Crear_nueva_sesion
import Diseño
import Chats
import Busqueda
import Perfil

from time import sleep


def Tilder ():
    
    #usuarios = pickle.load(open("Datos_Usuarios_Final.pkl", "rb"))
    
    pseudonimo_usuario = Menus_de_inicio.menu_principal()
    
    while pseudonimo_usuario != "0":
    
        opcion = Menus_de_inicio.menu_usuario()
    
        while opcion != "Cerrar sesion":
        
            if opcion == "Menu de chats":
                Chats.menu_chats(pseudonimo_usuario)
    
            if opcion == "Menu de busqueda":
                Busqueda.main_busqueda(pseudonimo_usuario)
            
            if opcion == "Mi perfil":
                Perfil.mi_perfil(pseudonimo_usuario)
            
            opcion = Menus_de_inicio.menu_usuario()
        
        pseudonimo_usuario = Menus_de_inicio.menu_principal()
    
    
Tilder()
