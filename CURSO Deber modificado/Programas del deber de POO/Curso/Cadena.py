texto = ("bienveNIdos al canal de Josue :v")

print(texto)
print(texto.lower())
print(texto.title())
print(texto.find("al"))
print(texto.count("e"))

textoFinal = texto.replace("e", "3")
print(textoFinal)

valor = texto.isnumeric()
print(valor)

cadenaSeparada = texto.split(" ")
print(cadenaSeparada)