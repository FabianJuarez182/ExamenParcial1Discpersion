
ArrayInicial = []
ArrayFinal = []
m = input ("Ingrese el modulo: ")

Lista = input("Ingrese la lista a utilizar separada por (,): ")

ArrayInicial = Lista.split(",")
print(ArrayInicial)
for i in range(int(m)):
    ArrayFinal.append("null")

for i in range(len(ArrayInicial)):
    modu = int(ArrayInicial[i]) % int(m)
    posModu = modu
    datoObtenido = ArrayFinal[modu]
    if datoObtenido == "null":
        ArrayFinal[modu] = int(ArrayInicial[i])
    else:
        for j in range(len(ArrayFinal)):
            if (posModu != len(ArrayFinal)-1):
                posModu = posModu + 1
                datoObtenido = ArrayFinal[posModu]
                if datoObtenido == "null":
                    ArrayFinal[posModu] = int(ArrayInicial[i])
                    break
            else:
                posModu = 0
                if ArrayFinal[posModu] == "null":
                    ArrayFinal[posModu] = int(ArrayInicial[i])
                    break
print("\n\nLa lista final de la dispersión es:")
print(ArrayFinal)