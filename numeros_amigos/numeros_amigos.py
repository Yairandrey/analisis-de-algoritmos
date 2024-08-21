from timeit import timeit

a = int(input("Ingrese numero 1: "))
b = int(input("Ingrese numero 2: "))

matriz_divisores_a = []
matriz_divisores_b = []

#Divisores de a
for i in range(1,a-1):
    if a%i == 0:
        matriz_divisores_a.append(i)

#Divisores de b
for i in range(1,b-1):
    if b%i == 0:
        matriz_divisores_b.append(i)

print(matriz_divisores_a)
print(matriz_divisores_b)

suma_a = sum(matriz_divisores_a)
suma_b = sum(matriz_divisores_b)

if suma_a == b and suma_b == a:
    print(f'{a} y {b} son numeros amigos')
else:
     print(f'{a} y {b} no son numeros amigos')

print(f'{round(timeit(),5)} seconds of ejecution')