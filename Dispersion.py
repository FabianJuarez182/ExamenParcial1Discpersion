# Universidad del Valle de Guatemala
# Departamento de Ingeniería
# Matematica Discreta seccion 10
# Fabián Estuardo Juárez Tello 21440
# Catedrático: Mario Castillo

#Crear las variables y listas para utilizar las variables
ArrayInicial = []
ArrayFinal = []

# Pedir la variable del modulo para utilizar en las listas
m = input ("Ingrese el modulo: ")

# Pedir la lista de numeros
Lista = input("Ingrese la lista a utilizar separada por (,): ")

# separar la lista por comas para cada elemento
ArrayInicial = Lista.split(",")
print(ArrayInicial)

# se agregan la cantidad de variables a una lista para utilizar el modulo que se obtendra
for i in range(int(m)):
    ArrayFinal.append("null")

#Recorrera lista inicial para ingresarlos en la final
for i in range(len(ArrayInicial)):
    modu = int(ArrayInicial[i]) % int(m) #Encontramos la posicion en la que debe ir el dato
    posModu = modu
    datoObtenido = ArrayFinal[modu] #Se guardara el dato de esa posicion para poder compararlo
    if datoObtenido == "null":
        ArrayFinal[modu] = int(ArrayInicial[i]) #Se modifica el dato en el array final
    else: #Encontramos la posicion cuando ya esta ocupado la posicion que se tenia anteriormente
        for j in range(len(ArrayFinal)):
            if (posModu != len(ArrayFinal)-1): #Se verifica que no sea pa posicion final del array
                posModu = posModu + 1 #se suma uno para poder recorrer el array
                datoObtenido = ArrayFinal[posModu] #Se guardara el dato de esa posicion para poder compararlo
                if datoObtenido == "null":
                    ArrayFinal[posModu] = int(ArrayInicial[i])#Se modifica el dato en el array final
                    break
            else: #Se pasa al inicio cuando la posicion final ya esta ocupada y no se pudo ingresar el dato anteriormente
                posModu = 0
                if ArrayFinal[posModu] == "null":
                    ArrayFinal[posModu] = int(ArrayInicial[i])
                    break
#Se imprime la lista final con la dispersión
print("\n\nLa lista final de la dispersión es:")
print(ArrayFinal)
