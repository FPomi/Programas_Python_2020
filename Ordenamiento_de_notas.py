"""
Se tienen 4 archivos con las notas del parcial de Algoritmos I:
andres.csv
ezequiel.csv
gustavo.csv
uriel.csv.
Los archivos están ordenados por padrón y su formato es:
<padrón>, <nota ej1>, <nota ej2>, <nota ej3>, <nota ej4>
Generar un archivo correctores.csv que contenga la información de los 4 archivos, ordenado
por padrón.
"""

with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\andres.csv", "w") as archivo:
    archivo.write ("123456, 4, 6, 3, 10") 

with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\ezequiel.csv", "w") as archivo:
    archivo.write ("654321, 5, 7, 1, 1")
    
with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\gustavo.csv", "w") as archivo:
    archivo.write ("456123, 8, 2, 1, 9")
    
with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\uriel.csv", "w") as archivo:
    archivo.write ("125634, 7, 3, 6, 6")
    

with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\correctores.csv", "w") as corrector:
    lista_corrector = []
    
    with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\andres.csv", "r") as archivo:
        lista_corrector.append(archivo.readlines())
    with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\ezequiel.csv", "r") as archivo:
        lista_corrector.append(archivo.readlines())
    with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\gustavo.csv", "r") as archivo:
        lista_corrector.append(archivo.readlines())
    with open ("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\uriel.csv", "r") as archivo:
        lista_corrector.append(archivo.readlines())
        
    lista_corrector.sort( key = lambda item:item[0])
    
    for lista in lista_corrector:
        for variable in lista:
            corrector.write(variable)
        corrector.write("\n")
        
    