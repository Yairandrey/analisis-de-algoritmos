from solution import Solution

# Matriz con las tuplas de los números amigos
n_amigos = [(220,284), 
            (1184,1210), 
            (2620,2924),
            (5020,5564),
            (6232,6368),
            (10744,10856),
            (12285,14595),
            (17296,18416),
            (63020,76084),
            (66928,66992)
            ]

# Diccionario para convertir a DataFrame
data = {
    'Couples': [f'{n_amigos[0]}',
                f'{n_amigos[1]}',
                f'{n_amigos[2]}',
                f'{n_amigos[3]}',
                f'{n_amigos[4]}',
                f'{n_amigos[5]}',
                f'{n_amigos[6]}',
                f'{n_amigos[7]}',
                f'{n_amigos[8]}',
                f'{n_amigos[9]}'
                ],
    'Attempt 1': ['','','','','','','','','',''], # Columna 1
    'Attempt 2': ['','','','','','','','','',''], # Columna 2
    'Attempt 3': ['','','','','','','','','',''], # Columna 3
    'Attempt 4': ['','','','','','','','','',''], # Columna 4
    'Attempt 5': ['','','','','','','','','',''], # Columna 5
    'Average':   ['','','','','','','','','',''], # Columna 6,
    'Time':      ['seg','seg','seg','seg','seg','seg','seg','seg','seg','seg',] # Columna 7
}

#Llamo al método que crea la tabla
data_to_convert = Solution.logica(n_amigos,data)


# Llamado al método que que convierte a excel
Solution.convertToExcel(data_to_convert)

# Muestro por concola la matriz obtenida
print(data_to_convert)


