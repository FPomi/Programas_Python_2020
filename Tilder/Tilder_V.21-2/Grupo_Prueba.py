import os
import pickle

"""
grupo_prueba = {}
#  clave: Pseudónimo   Nombre    Apellido  Contraseña  Sexo    Edad  Direccion(Latitud y longitud)
grupo_prueba["elenitaaa"] = ["Elena", "Vasquez", "48lopiaSd", "M", 38, [75.15648,25.45973], [ "gatos", "perros", "charlas", "rock", "programacion"],["a","z","anastacio_f"], {}]
grupo_prueba["marcosrodriguez"] = ["Marcos", "Rodriguez", "Qwer15", "H", 26, [27.12452,32.15475], ["cerveza-artesanal", "boca juniors", "politica", "programacion", "escritura"], ["tincho123","elenitaaa"],{}]    
grupo_prueba["anastacio_f"] = ["Anastacio", "Fernandez", "AAAaahh78", "h", 48, [95.12548,86.26548], ["river-plate", "ciclismo", "gatos", "comida", "videojuegos"], ["elenitaaa"],{}]
grupo_prueba["xlolx"] = ["Lucio", "Hernandez", "rutidjk34K", "H", 18, [43.453435,68.232324], ["pizza", "deportes", "league-of-legends", "rap", "bailar"],["tincho123"],{}]
grupo_prueba["tincho123"] = ["Martin", "Dos Santos", "36tengoHambre", "H", 21, [12.453435,68.232324], ["rugby", "deportes", "cerveza-artesanal", "fiesta", "ciclismo"],["xlolx"],{}]
grupo_prueba["marialopezzz"] = ["Maria", "Lopez", "reiroX78", "M", 20, [105.1254218,96.456452], ["anime", "videojuegos", "musica", "bailar", "netflip"],["ff"],{}]
grupo_prueba["ff"] = ["Fernanda", "Fernandez", "Contasena123223", "M", 30, [54.697835,79.95695], ["parque", "yoga", "naturaleza", "rock", "netflip"],["marialopezzz"],{}]
grupo_prueba["a"] = ["Aaaa", "Zzzz", "dkfjkdjT24", "I", 99, [26.85228,120.532323], ["charlas", "debate", "yoga", "boca-juniors", "perros"],["z"],{}]
grupo_prueba["z"] = ["Zzzz", "Aaaaa", "24dkfjkdjT", "I", 18, [120.85228,26.532323], ["charlas", "debate", "yoga", "boca-juniors","perros"],["a"],{}]
grupo_prueba["ch1512"]= ["Carolina", "Herrera", "carolinaHerrera1653", "M", 60, [50.5656565,80.454654], ["viajes", "moda", "cocinar", "yoga", "escritura"],["x"],{}]
grupo_prueba["x"] = ["x", "x", "y", "M", 20, [50.100000,80.100000], ["viajes", "moda", "cocinar", "gatos", "parque"],["ch1512","ff"], {}]

pickle.dump(grupo_prueba, open("Datos_Usuarios_Final.pkl", "wb"))
"""

# El usuario "x" es el que estuve usando de prueba de pseudonimo ingreso en Arranca_el_programa hasta ahora

def main():

### Creación del archivo csv en base a los primeros 10 usuarios de prueba, 
### después va a ser un archivo para todos en general agregando nuevos usuarios

    no_iniciado = 0
    ya_iniciado = 1 
    
    """ Si en el archivo "inicio.txt" hay un 1 significa que el archivo datos usuarios ya fue creado anteriormente
    Esto es para evitar que se sobreescriba una vez que ya fue iniciada. Si hay un 0 se crea por primera vez"""

    iniciado = 5
    lista_usuarios=[]

    with open("inicio.txt") as archivo_txt:

        ruta_archivo = os.getcwd()
        os.chdir(ruta_archivo) 
        archivo_txt = "inicio.txt"
        lectura = open(archivo_txt)

        for dato in lectura:
            iniciado = int(dato)

    if iniciado == no_iniciado:

        for pseudonimo in grupo_prueba:

            datos_usuarios = grupo_prueba[pseudonimo]
            usuarios = pseudonimo
            lista_usuarios.append(datos_usuarios)
            datos_usuarios.insert(0,usuarios)


        with open('datos_usuarios.csv', 'w', newline='') as archivo_csv:
            
            escritura = csv.writer(archivo_csv, delimiter="/")
            datos=[["Pseudonimo","Nombre","Apellido","Contraseña","Sexo","Edad","Direccion","Intereses"]]
            escritura.writerows(datos)
            escritura.writerows(lista_usuarios)

        archivo_csv.close()
        datos.clear()
        lista_usuarios.clear()

        with open('inicio.txt', 'w', newline='') as archivo:
                
            escritura = csv.writer(archivo)
            escritura.writerows(str(ya_iniciado))
        
        archivo.close()

        

main()