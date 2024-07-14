import pickle

def Pseudonimo(dicc_usuarios):
    
    pseudo = input("Primero ingrese un Pseudonimo unico para poder identificarlo.\n(Este debe ser unico, solo minúsculas, números y guión bajo):\n ")
        
    while (pseudo in dicc_usuarios):
        pseudo = input("Parece que el Pseudonimo esta en uso.\n Intente otro, por favor.\n(Este debe ser unico, solo minúsculas, números y guión bajo):")
            
    caracter = 0
    while caracter != len(pseudo):
        if ( not pseudo[caracter].isalnum() ) or ( pseudo[caracter].isupper() ):
            if pseudo[caracter] != "_":
                print("EROR. :C Pseudonimo invalido")
                pseudo=input("Ingrese otro Pseudonimo.\n Este debe ser unico, solo minúsculas, números y guión bajo:\n")
                caracter = 0
            else:
                caracter += 1
        else:
            caracter +=1 
        
    return pseudo

#-----------------------------------------------------------------------------------------------------------------------------#

def verf_contraseña(contraseña):
    
    tien_May = False
    tien_Min = False
    tien_Num = False
        
    for caracter in contraseña:
        if caracter.isnumeric():
            tien_Num = True
        elif caracter.isupper():
            tien_May = True
        elif caracter.islower():
            tien_Min = True
    
    return tien_Num and tien_May and tien_Min

#-----------------------------------------------------------------------------------------------------------------------------#

def contraseña():
    contraseña = input("Ingrese su contraseña.\n(Esta requiere al menos una mayúscula, una minúscula, un dígito decimal, y un largo mínimo de 5 caracteres):")
    return contraseña

#-----------------------------------------------------------------------------------------------------------------------------#

def contraseña_incorrecta():
    cntr = input("ERROR. :C\nLa contraseña no cumple con los requisitos. Por favor ingrese una contraseña valida: ")
    return cntr

#-----------------------------------------------------------------------------------------------------------------------------#

def sexualidad():
    
    sex = input("Ingrese su sexo entre:\n*Mujer (M)\n*Hombre (H)\n*o\n*Indefinido (I)\n")
    sexo_valido = ["m","h","i"]
    
    while sex and sex.lower() not in sexo_valido:
        sex = input("ERROR. >:C\nPorfavor Ingrese su sexo entre:\n*Mujer (M)\n*Hombre (H)\n*o\n*Indefinido (I)\n ")    
    
    return sex.lower()

#-----------------------------------------------------------------------------------------------------------------------------#

def ingre_edad():
    ed = int(input("Ingrese su edad\n(Debe tener 18 años como minimo para poder ingresar):\n"))
    return ed

#-----------------------------------------------------------------------------------------------------------------------------#

def ubicacion():
    
    coord = []
    
    latitud = float(input("Primero ingrese su latitud en grados decimales\n(Consulte en Go*gle M*ps si no conoce su posicion en grados decimales):\n"))
    coord.append(latitud)
    
    longitud = float(input("Ahora su longitud en grados decimales\n(Consulte en Go*gle M*ps si no conoce su posicion en grados decimales):\n"))
    coord.append(longitud)
    
    return coord

#-----------------------------------------------------------------------------------------------------------------------------#

def etiqueta_valida(interes):
    
    valido = True
    tildes = ["á","é","í","ó","ú","Á","É","Í","Ó","Ú"] 
    guion="-"
    
    
    if len(interes) == 0 :
        valido = False
    else:
        indice = 0
        while indice < len(interes) and valido:
            if interes[indice] == " " or ( interes[indice] in tildes ):
                valido = False
           
            indice += 1
    
        indice = 0
        while indice < len(interes) and valido:
            if interes[indice].isalpha()==False and (interes[indice] != guion):
                valido = False
            indice += 1
    
    return valido

#-----------------------------------------------------------------------------------------------------------------------------#

def etiquetas_de_interes():
    
    lista_intereses = []
    print("Muy Bien!\n Hemos llegado a una parte importante en la creacion de su perfil :D")
    
    interes = input("Por favor ingrese sus intereses.\n Los intereses son etiquetas, palabras sin espacio ni acentos, unidas con guiones medios unicamente.\n(Para dejar de ingresar solo debe dejar en blanco):")
    
    val = etiqueta_valida(interes)
        
    while val and len(interes) != 0:
        lista_intereses.append(interes)
        interes = input("Ingrese más de sus intereses.\n Los intereses son etiquetas, palabras sin espacio ni acentos, unidas con guiones medios unicamente.\n(Para dejar de ingresar solo debe dejar en blanco):")
        val = etiqueta_valida(interes)
        
    return lista_intereses

#-----------------------------------------------------------------------------------------------------------------------------#

def nueva_persona():
    
    usuarios = pickle.load(open("Datos_Usuarios_Final.pkl" , "rb"))
    
    print("\t\tGracias por decidir ser un usuario nuevo!")
    print("Vamos a crear un perfil inigualable!")
    
    pseudo = Pseudonimo(usuarios)
    
    nombre = input("\nIngrese su nombre:")
    apellido = input("Ingrese su apellido:")
    
    contra = contraseña()
    while len(contra) < 5  or not verf_contraseña(contra):
        contra = contraseña_incorrecta()
        
    sexo = sexualidad()
    
    edad = ingre_edad()
    while edad < 18 or edad > 99:
        edad = ingre_edad()
   
    print("Su siguiente paso es indicar su ubicacion actual.")

    coord = ubicacion()
     
    intereses = etiquetas_de_interes() 
    
    matcheos = []

    chats = {}

    usuarios[pseudo] = [nombre, apellido, contra, sexo, edad, coord, intereses, matcheos, chats]
    
    pickle.dump(usuarios, open("Datos_Usuarios_Final.pkl", "wb"))
    
    return pseudo    
    
