import os
import pickle

grupo_prueba = {}
grupo_prueba["pabloguarna"] = ["Pablo", "Guarna", "Pablo1", "H", 38, [-34.6882 ,-58.5620], [ "ingenieria", "informatica", "racing", "rock", "programacion", "yoga"],[], {}, "( . ᴗ .)"]
grupo_prueba["marcosrodriguez"] = ["Marcos", "Rodriguez", "Marcos1", "H", 26, [-34.7683,-58.4068], ["cerveza-artesanal", "yoga", "boca juniors", "politica", "programacion", "escritura"], [],{}, "(´ ᴗ ´)"]    
grupo_prueba["anastacio_f"] = ["Anastacio", "Fernandez", "Anastacio1", "h", 48, [-34.6041,-58.9457], ["river-plate", "ciclismo", "viajes", "moda", "cocinar", "yoga"], [],{}, "(> ᴗ <)"]
grupo_prueba["inesines"] = ["Inés", "Hernandez", "Ines1", "M", 18, [-34.4346,-58.5815], ["pizza", "deportes", "yoga", "league-of-legends", "rap", "bailar"],[],{}, "(- ᴗ -)"]
grupo_prueba["tincho123"] = ["Martin", "Dos Santos", "Martin1", "H", 21, [-34.3426,-58.8250], ["rugby", "deportes", "cerveza-artesanal", "fiesta", "ciclismo", "yoga"],[],{}, "(ᵔ ᴗ ᵔ)"]
grupo_prueba["marialopezzz"] = ["Maria", "Lopez", "Maria1", "M", 20, [-34.1081,-59.0269], ["anime", "videojuegos", "musica", "bailar", "netflip", "yoga"],[],{}, "(♥ ᴗ ♥)"]
grupo_prueba["fernandaf"] = ["Fernanda", "Fernandez", "Fernanda1", "M", 30, [-34.9379,-57.9573], ["yoga", "parque", "ingenieria", "informatica", "racing", "rock", "programacion", "netflip"],[],{}, "(* ᴗ *)"]
grupo_prueba["fede"] = ["Federique", "Lopez", "Federique1", "I", 55, [-34.5819,-58.4218], ["charlas", "debate", "yoga", "boca-juniors", "perros"],[],{}, "( `_´ )"]
grupo_prueba["ramone"] = ["Ramone", "Arias", "Ramone1", "I", 18, [-34.7719,-58.3832], ["charlas", "debate", "yoga", "boca-juniors","perros"],[],{}, "( * o *)"]
grupo_prueba["carolinah"]= ["Carolina", "Herrera", "Carolina1", "M", 60, [-34.6394,-58.460017], ["viajes", "moda", "cocinar", "yoga", "escritura"],[],{}, "( ► ᴗ ◄)"]

diccionario = grupo_prueba
pickle.dump(diccionario, open("Datos_Usuarios_Final.pkl", "wb"))

