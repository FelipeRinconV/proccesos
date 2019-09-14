from Procceso import Procceso

p1 = Procceso("P1", 3, 30, 3)
p2 = Procceso("P2", 7, 19, 3)
p3 = Procceso("P3", 20, 20, 3)

agregados = [p1, p2, p3]

listaEspera = [p1]
listaEspera.pop()

lista_proccesados = [p1]
lista_proccesados.pop()


def dar_menor():
    actual = agregados[0]
    for i in range(1, len(agregados)):

        if actual.tiempollega > agregados[i].tiempollega:
            actual = agregados[i]

    return actual


# Llenamos la lista de espera ¿
while len(agregados) > 0:
    listaEspera.append(dar_menor())
    agregados.remove(dar_menor())

cant = len(listaEspera)

reloj = listaEspera[0].tiempollega

while len(listaEspera) > 0:

    if listaEspera[0].tiempollega <= reloj:

        espera = listaEspera[0].tiempocpu

        print("Se inicia a proccesar ID: " + listaEspera[0].nombre + " en el tiempo: " + str(reloj) + str("\n"))
        listaEspera[0].tiempoInicio = reloj

        reloj += espera
        for x in range(espera):
            print("Proccesadon ID: " + str(listaEspera[0].nombre))

        print("\n"+"Se terminda de proccesar ID: " + listaEspera[0].nombre + " en el tiempo: " + str(reloj) + str("\n"))
        listaEspera[0].tiempoFinal = reloj

        lista_proccesados.append(listaEspera[0])

        listaEspera.remove(listaEspera[0])
    else:
        reloj += 1

# print(proccesados)
