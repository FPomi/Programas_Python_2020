def es_primo(num_max):
    
    contador_divisores = 0
    
    for i in range (1, num_max+1):
        cociente = num_max / i
        cociente_int = int(cociente)

        if cociente == cociente_int:
            contador_divisores = contador_divisores + 1
        
    if contador_divisores == 2:            
        contador_divisores = 0
        return True
    else:            
        contador_divisores = 0
        return False

"""-------------------------------------------------------------------------------------------------------------------------"""

def suma_de_numeros_primos(numero):
    
    sumador = 0
    
    for i in range (1, numero+1):
        
        if es_primo(i) == True:
            sumador = sumador + i

    return sumador
    pass

"""-------------------------------------------------------------------------------------------------------------------------"""

def main():
    numero = int (input ("ingrese un valor: "))
    sumatoria = suma_de_numeros_primos(numero)
    
    print ("suma_de_numeros_primos(", numero,") => ", sumatoria)

main()