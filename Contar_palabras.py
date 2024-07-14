
def suma_de_numeros_primos(numero):
   
    cociente = 0.0
    contador_divisores = 0    
    
    for i in (1, numero):
        
        for a in i:

            cociente = i / a
            cociente_int = int(cociente)

            if cociente == cociente_int:
                contador_divisores = contador_divisores + 1

            if a == i and contador_divisores == 2:
                sumador = sumador + i
                contador_divisores = 0

    pass

def main():
    input (int(numero))
    sumador = 0
    suma_de_numeros_primos(numero)
    print ("suma_de_numeros_primos(",numero,") => ",sumador)

main()