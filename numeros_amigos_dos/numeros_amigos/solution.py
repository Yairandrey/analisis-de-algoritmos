# Clase que contiene los dos métodos que resulven el problema de los números amigos
import pandas as pd
import timeit
class Solution :

    # Método que convierte la información a un excel
    def convertToExcel(data):
        df = pd.DataFrame(data)
        df.to_excel("reportes/ej_1.xlsx", index=False)
    
    # Método para la lógica
    def logica(n_amigos,data):
        # Matrices para hallar los divisores de los números
        matriz_a = []
        matriz_b = []

        # Itero sobre la cantidad de intentos y el promedio
        for m in range(6):

            # Itero sobre el total de parejas
            for i in range(len(n_amigos)):
                mayor = max(n_amigos[i])

                # Itero para hallar divisores
                for j in range(1,(int(mayor/2) + 1)):
                    if n_amigos[i][0] % j == 0:
                        matriz_a.append(j)
                    if n_amigos[i][1] % j == 0:
                        matriz_b.append(j)

                # Verifico si son números amigos.
                if sum(matriz_a) == n_amigos[i][1] and sum(matriz_b) == n_amigos[i][0]:

                # Guardo los tiempos de los 5 intentos
                    if m == 0: data['Attempt 1'][i] = f' {round(timeit.timeit(),5)}'
                    if m == 1: data['Attempt 2'][i] = f' {round(timeit.timeit(),5)}'
                    if m == 2: data['Attempt 3'][i] = f' {round(timeit.timeit(),5)}'
                    if m == 3: data['Attempt 4'][i] = f' {round(timeit.timeit(),5)}'
                    if m == 4: data['Attempt 5'][i] = f' {round(timeit.timeit(),5)}'

                # Calculo el promedio de cada pareja de números
                    if m == 5 : 
                        data['Average'][i] = ((float(data['Attempt 1'][i])+ float(data['Attempt 2'][i]) + float(data['Attempt 3'][i]) + float(data['Attempt 4'][i]) + float(data['Attempt 5'][i])) / 5)
        
            # Limpio matrices de divisores para cada número luego de comparar resultados
                matriz_a.clear()
                matriz_b.clear()
        return data
