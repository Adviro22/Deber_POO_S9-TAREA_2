#Función: Es un conjunto de instrucciónes que realizan un proceso
#su principal ventaja es que nos ayudan a evitar código repetio.

def saludar():
    print("Ortiz")
    print("Josue")
    print("Adviro22")
    return "Hola"

print(saludar())

def evaluarSueldoMinimo(sueldo):
    if sueldo >= 850:
        print("Cumples con el sueldo")
    else:
        print("Ganas menos que el sueldo mínimo")

evaluarSueldoMinimo(100)