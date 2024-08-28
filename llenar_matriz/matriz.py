import random,time
inicio = time.time()

# Código a medir
time.sleep(1)

a = int(input('Ingresa valor: '))
# Creo la matriz que va a guardar la informacion.
matriz = []
# Creo el vector o las filas de la matriz
vector= []
for i in range(a):
    for j in range(a): 
        vector.append(random.randint(0,100))
    matriz.append(vector)
    vector = []
fin = time.time()
print(f'Time of ejecution: {round(fin-inicio,5)} seconds')

# Imprimo los vectores o filas de la matriz
#for i in matriz:
    #print(i)