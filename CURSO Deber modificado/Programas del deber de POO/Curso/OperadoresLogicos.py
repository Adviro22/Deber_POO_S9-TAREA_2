#AND: Equivalente a "Y si además..."
#OR: "Osino.."
#not -> negación

distancia = 400
numeroHermanos = 3
salarioPadres = 3000

tieneBeneficios = False

if (distancia > 1000 and numeroHermanos > 2) or salarioPadres < 2000:
    tieneBeneficios = True

print(not tieneBeneficios)

if (5 > 3) or (8 < 6):
    print("Verdad")
else:
    print("Es mentira...")