
def combinaciones_6(lista_combinaciones:list):
    combi_ganadoras =[[1,2,3],[3,2,1],[5,1],[1,5],[2,1,3],[3,1,2],[2,3,1]]
    combi_objetivo = []
    respuesta = 6
    suma = 0
    if isinstance(lista_combinaciones,list):
        
        lista_combinaciones.sort()
        for i,numero in enumerate(lista_combinaciones):
            suma += numero
            print("suma: ",suma)
            
            numeros_usados = []
            numeros_usados.append(numero)
            print(numeros_usados)
            
            lista_combinaciones.pop(i-1)
            print(lista_combinaciones)
            
            if suma == 6:
                if numeros_usados in combi_ganadoras:
                    combi_objetivo.append()
                    
        return combi_objetivo
    else:
        return combi_objetivo
        
        
        
mi_lista = [1,2,3,4,5,6,1,2]
combinaciones_utiles = combinaciones_6(mi_lista)

print("Mis combinaciones ganadoras: ", combinaciones_utiles)