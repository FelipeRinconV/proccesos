from Procceso import Procceso

p1 = Procceso("P1", 1, 25, 3)
p2 = Procceso("P2", 2, 25, 3)
p3 = Procceso("P3", 10, 25, 3)

agregados = [p1, p2, p3]

lista_espera = [p1]
lista_espera.pop()

lista_proccesados = [p1]
lista_proccesados.pop()

lista_cola = [p1]
lista_cola.pop()


# Da el menor de los agregador
def dar_menor():
    menor_actual = agregados[0]
    for i in range(1, len(agregados)):

        if menor_actual.tiempollega > agregados[i].tiempollega:
            menor_actual = agregados[i]

    return menor_actual


# Llenamos la lista de espera
while len(agregados) > 0:
    lista_espera.append(dar_menor())
    agregados.remove(dar_menor())


# Da el menor de la lista de espera en timepo de cpu
def dar_menor_rafaga():
    menor = lista_espera[0]
    for i in range(1, len(lista_espera)):
        if menor.tiempocpu > lista_espera[i].tiempocpu:
            menor = lista_espera[i]

    return menor


# Da el menor en timepo rafaga de la cola
def dar_menor_rafaga_cola():
    menor = lista_cola[0]
    for i in range(1, len(lista_cola)):
        if menor.tiempocpu > lista_cola[i].tiempocpu:
            menor = lista_cola[i]

    return menor


"""# Imprimir la lista de espera antes de entrar al metodo
for x in listaEspera:
    print(x.nombre + str(x.tiempollega))"""


# Da la cola de proccesos respecto al timempo del cpu
def dar_cola_proccesos(tiempo):
    for i in range(len(lista_espera)):

        if lista_espera[i].tiempollega <= tiempo and not lista_cola.__contains__(lista_espera[i]):
            lista_cola.append(lista_espera[i])

    return lista_cola


# Reloj del proccesador
reloj = 0

# Iniciamos con el algoritmo SJF
while len(lista_espera) > 0:

    # Revisado
    total_cola = len(dar_cola_proccesos(reloj))

    if total_cola > 0:

        actual = dar_menor_rafaga_cola()

        espera = actual.tiempocpu

        print(
            "Se inicia a proccesar ID: " + actual.nombre + " en el tiempo: " + str(reloj) + str("\n"))
        actual.tiempoInicio = reloj

        for x in range(espera):
            print("PROCCESANDO ID: " + actual.nombre)

            # IMPLEMENTAR EL CODIGO PARA EXPULSIVO

            reloj += 1

        print(
            "\n" + "Se terminda de proccesar ID: " + dar_menor_rafaga().nombre + " en el tiempo: " + str(reloj) + str(
                "\n"))

        actual.tiempoFinal = reloj

        centinela = False
        x = 0
        while not centinela:

            if lista_espera[x].nombre == actual.nombre:
                # Se quita bien de la lista de espera
                lista_espera.pop(x)
                lista_proccesados.append(actual)
                lista_cola.remove(actual)
                centinela = True
        # Aumentamos
        x += 1
    else:
        reloj += 1
        print("tiempo de ocio")

print(lista_proccesados)
