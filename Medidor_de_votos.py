def Medidor_votos ():
    
    NOMBRE = 0
    VOTOS = 1
    
    dicc_votos = {}
    dicc_ordenado = {}
    lista_votos = []
    
    seguir = "s"
    
    while seguir == "s":
        partido = input("Ingrese el partido a sumarle votos: ")
        cant_votos = int (input("Ingrese la cantidad de votos a sumarle: "))
        
        if partido in dicc_votos:
            dicc_votos[partido] += cant_votos
        else:
            dicc_votos[partido] = cant_votos
            
        seguir = input("Desea seguir ingresando?(s/n): ")

    dicc_ordenado = sorted(dicc_votos.items(), key = lambda item:item[1], reverse = True)
    
    for partido in dicc_ordenado:
        print (f"El partido {partido[NOMBRE]} obtuvo {partido[VOTOS]} votos.")
    
Medidor_votos()