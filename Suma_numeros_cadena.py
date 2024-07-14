def sumar_caracteres_numericos(cadena):
    
    sumador = 0
    
    for i in range (len(cadena)):
        
        print (cadena[i])

        if cadena[i].isnumeric():
            sumador = sumador + int(cadena[i])
            #print(sumador)
            
    print("suma =",sumador)            
    
def main():
    cadena = input()
    sumar_caracteres_numericos(cadena)
    
    
main()