from Procceso import Procceso

p1 = Procceso("P1", 11, 30, 3)
p2 = Procceso("P2", 2, 25, 3)
p3 = Procceso("P3", 2, 20, 3)

lista_agregados = [p1, p2, p3]

lista_espera = [p1]
lista_espera.pop()

lista_proccesados = [p1]
lista_proccesados.pop()


def dar_menor():
    actual = lista_agregados[0]
    for i in range(1, len(lista_agregados)):

        if actual.tiempollega > lista_agregados[i].tiempollega:
            actual = lista_agregados[i]

    return actual


# Llenamos la lista de espera
while len(lista_agregados) > 0:
    lista_espera.append(dar_menor())
    lista_agregados.remove(dar_menor())


def dar_menor_rafaga():
    menor = lista_espera[0]
    for i in range(1, len(lista_espera)):
        if menor.tiempocpu > lista_espera[i].tiempocpu:

            menor = lista_espera[i]

    return menor


print(dar_menor_rafaga().nombre)

reloj = lista_espera[0].tiempollega
# Iniciamos con el algoritmo SJF
while len(lista_espera) > 0:

    espera = dar_menor_rafaga().tiempocpu

    print("Se inicia a proccesar ID: " + dar_menor_rafaga().nombre + " en el tiempo: " + str(reloj) + str("\n"))
    dar_menor_rafaga().tiempoInicio = reloj

    reloj += espera
    for x in range(espera):
        print("Proccesadon ID: " + str(dar_menor_rafaga().nombre))

    print(
        "\n" + "Se terminda de proccesar ID: " + dar_menor_rafaga().nombre + " en el tiempo: " + str(reloj) + str("\n"))
    dar_menor_rafaga().tiempoFinal = reloj

    lista_proccesados.append(dar_menor_rafaga())

    lista_espera.remove(dar_menor_rafaga())

# print(proccesados)"""""
