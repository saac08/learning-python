"""
Operaciones básicas: Pide dos números al usuario e imprime 
la suma, resta, multiplicación y división.
"""

print("Ingrese el primer numero: ", end="")
numero_uno = int(input()) 
print("Ingrese el segundo dos: ", end="")
numero_dos = int(input())

def Suma(num_uno, num_dos):
    return print(num_uno + num_dos)

def Resta(num_uno, num_dos):
    if(num_uno - num_dos < 0):
        return print("El resultado es negativo")
    return print(num_uno - num_dos)

def Division(num_uno, num_dos):
    return print(num_uno / num_dos)

def Producto(num_uno, num_dos):
    return print(num_uno * num_dos)

print("Los resultados serían:")
print("-----------------------------------")
Suma(numero_uno, numero_dos)
Resta(numero_uno, numero_dos)
Division(numero_uno, numero_dos)
Producto(numero_uno, numero_dos)