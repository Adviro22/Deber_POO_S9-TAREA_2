# Break: Permite salir de un bucle cuando se cumple una condición

"""
for numero in range(1, 6):
    if numero == 3:
        break #Descanso o Interrumpir
    print("El numero es: {0}".format(numero))

print("Bucle terminado")
"""

# Continue: Omite una parte del bucle cuando se cumple una condición y
# continua con el resto.

"""
for numero in range(1, 6):
    if numero == 3:
        continue #Continua con el resto del bucle
    print("El numero es: {0}".format(numero))

print("Bucle terminado")
"""

# Pass: Permite continuar con una sentencia o función que ya no tiene
# o algún no tiene un bloque de código útil.

for numero in range(1, 6):
    if numero <= 3:
        #Aquí no pasa nada y el bucle sigue trabajando.
        pass
    else:
        print("El siguiente valor es mayor a 3:")
    print("El numero es: {0}".format(numero))

print("Bucle terminado")

def funcionSiImplementar():
    pass

