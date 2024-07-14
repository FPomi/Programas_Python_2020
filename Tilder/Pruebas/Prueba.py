def listar_archivo():
    
    with open("D:\\Franco\\Facultad\\Algoritmos\\Programas _pyton_2020\\Thonnys\\Archivos de programas\\ventas.csv","r") as arVentas:
        cant_total_gral = imp_total_gral = 0
        
        for linea in arVentas:
            cod_suc, cod_art, cant, imp = linea.rstrip("\n").split(",")
            
            print(cod_suc, cod_art, cant, imp)
            
            cant_total_gral += int(cant)
            imp_total_gral += float(imp)
        
        print("Total General: ", cant_total_gral, imp_total_gral)
    
    return

listar_archivo()