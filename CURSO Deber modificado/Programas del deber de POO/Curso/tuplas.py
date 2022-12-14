"""
Tupla: Es una estructura de datos propia de Python que permite almacenar disntintos
valores, son inmutables: no cambian una vez inicializadas
"""

tupla = (1, 2, 3)
print(tupla)
tupla2 = (7, "Oscar", True, 450.1, 16 + 7j)
print(tupla2)
tupla3 = (9, 3, (4, 5, 6))
print(tupla3)
print(tupla2[1])
# tupla2[1] = "Adviro22"
print(tupla2[-1]) #Se accede al último valor de la tupla.
print(tupla2[0:4])
print(tupla2[-2])

a, b, c = tupla
print(a)
print(b)
print(c)

tuplaFinal = tupla + tupla3
print(tuplaFinal)

print(tuplaFinal.count(21))
print(tuplaFinal.index(3))
