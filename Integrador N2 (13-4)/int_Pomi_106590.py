"""
La fábrica de yogur en potes de vidrio Dahi se encuentra procesando los yogures recibidos de sus distintos centros
de producción y para eso tiene los siguientes archivos:

 

CORDOBA.CSV, SANTA_FE.CSV, ENTRE_RIOS.CSV, ordenados por lote

    lote: código alfanumérico, por ejemplo DXCO20210304

    gusto: string con posibles valores frutilla, vainilla, sin sabor

    calorías: string con posibles valores entero, light

    adicionales: string con posibles valores con frutas, con cereales o vacío.

    peso: valor numérico con decimales expresado en gramos, por ejemplo 125.22


Se pide escribir un programa en Python que procese los archivos y:


1.Genere un archivo único de salida STOCK.CSV unificando los datos de los 3 archivos y ordenado por lote,
descartando aquellos yogures con un peso menor a 90 gramos.

2.Imprimir la cantidad de kilos de yogur producido por cada uno de los 3 centros de producción

3.Guardar en un archivo PRODUCCION.TXT la descripción y el total de unidades de cada variedad de yogur en stock,
ordenado de mayor a menor por total de unidades. La variedad está determinada por el gusto, las calorías y los adicionales.
Por ejemplo “vainilla light con frutas”, “frutilla entero”, “sin sabor light con cereales”, etc.

"""

#----------------------------------------------------------------------------------------------------------------------------#

def leer_archivo (archivo, vacio):
    linea = archivo.readline()
    return linea.rstrip("\n").split(",") if linea else vacio

#----------------------------------------------------------------------------------------------------------------------------#

def analizar_stock (provincia):
    
    GRAMOS_MIN = 90
    
    lista_provincia = []
    
    kilos_producidos = 0.0
    
    vacio = ("","","","","")
    lote, gusto, calorias, adicionales, peso = leer_archivo(provincia, vacio)
    
    while lote:
        
        kilos_producidos += float(peso)/1000
        
        if float(peso) >= GRAMOS_MIN:
            lista_provincia.append([lote, gusto, calorias, adicionales, peso])
            
        lote, gusto, calorias, adicionales, peso = leer_archivo(provincia, vacio)
    
    #print(lista_provincia)
    return lista_provincia, kilos_producidos
        
#----------------------------------------------------------------------------------------------------------------------------#    
def analizar_produccion (produccion, stock_total):
    GRAMOS = 4
    
    for lista_in in range(len(stock_total)-2):
        #print(lista_in)
        for lista_comp in range(lista_in + 1, len(stock_total)-2):
            #print (stock_total[lista_in][0:-1])
            #print(stock_total[lista_in][GRAMOS])
            if (stock_total[lista_in][1:-1] == stock_total[lista_comp][1:-1]):
                
                stock_total[lista_in][GRAMOS] = float (stock_total[lista_in][GRAMOS]) + float(stock_total[lista_comp][GRAMOS])
                #print("se repite")
                #print(stock_total[lista_in][GRAMOS])
                del(stock_total[lista_comp][:])
        #print(lista)
    #print (stock_total)
    #print(stock_total)            
#----------------------------------------------------------------------------------------------------------------------------#    

def analizar_stocks (cordoba, santa_fe, entre_rios, stock, produccion):
    
    LOTE = 0
    
    stock_cordoba, kilos_producido_cordoba = analizar_stock (cordoba)
    stock_santa_fe, kilos_producido_santa_fe = analizar_stock (santa_fe)
    stock_entre_rios, kilos_producido_entre_rios = analizar_stock (entre_rios)
    
    stock_total = stock_cordoba + stock_entre_rios + stock_santa_fe
    stock_total.sort (key = lambda item:item[LOTE])
    
    #stock.write(stock_total)
    #print(stock_total)
    
    print (f"Se produjeron {kilos_producido_cordoba}kg de helado en Cordoba\n")
    print (f"Se produjeron {kilos_producido_santa_fe}kg de helado en Santa Fe\n")
    print (f"Se produjeron {kilos_producido_entre_rios}kg de helado en Entre Rios\n")

    analizar_produccion(produccion, stock_total)
    
#----------------------------------------------------------------------------------------------------------------------------#

def main():
    
    cordoba = open ("CORDOBA.CSV", "r")
    santa_fe = open ("SANTA_FE.CSV","r")
    entre_rios = open ("ENTRE_RIOS.CSV","r")
    
    stock = open ("STOCK.CSV","w")
    produccion = open ("PRODUCCION.TXT","w")
    
    analizar_stocks(cordoba, santa_fe, entre_rios, stock, produccion)
    
    cordoba.close()
    santa_fe.close()
    entre_rios.close()
    stock.close()
    produccion.close()
    
#----------------------------------------------------------------------------------------------------------------------------#    

main ()
