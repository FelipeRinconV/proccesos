from Procceso import Procceso

p1 = Procceso("P1", 20, 3, 3)
p2 = Procceso("P2", 5, 10, 3)
p3 = Procceso("P3", 10, 7, 3)

agregados = [p1, p2, p3]

listaEspera = [p1]
listaEspera.pop()

proccesados = [p1]
proccesados.pop()

listaCola = [p1]
listaCola.pop()


# Da el menor de los agregador
def dar_menor():
    menor_actual = agregados[0]
    for i in range(1, len(agregados)):

        if menor_actual.tiempollega > agregados[i].tiempollega:
            menor_actual = agregados[i]

    return menor_actual


# Llenamos la lista de espera
while len(agregados) > 0:
    listaEspera.append(dar_menor())
    agregados.remove(dar_menor())


# Da el menor de la lista de espera en timepo de cpu
def dar_menor_rafaga():
    menor = listaEspera[0]
    for i in range(1, len(listaEspera)):
        if menor.tiempocpu > listaEspera[i].tiempocpu:
            menor = listaEspera[i]

    return menor


# Da el menor en timepo rafaga de la cola
def dar_menor_rafaga_cola():
    menor = listaCola[0]
    for i in range(1, len(listaCola)):
        if menor.tiempocpu > listaCola[i].tiempocpu:
            menor = listaCola[i]

    return menor


"""# Imprimir la lista de espera antes de entrar al metodo
for x in listaEspera:
    print(x.nombre + str(x.tiempollega))"""


# Da la cola de proccesos respecto al timempo del cpu
def dar_cola_proccesos(tiempo):
    for i in range(len(listaEspera)):

        if listaEspera[i].tiempollega <= tiempo and not listaCola.__contains__(listaEspera[i]):
            listaCola.append(listaEspera[i])

    return listaCola


# Reloj del proccesador
reloj = 0

# Iniciamos con el algoritmo SJF
while len(listaEspera) > 0:

    # Revisado
    total_cola = len(dar_cola_proccesos(reloj))

    if total_cola > 0:

        actual = dar_menor_rafaga_cola()

        espera = actual.tiempocpu

        print(
            "Se inicia a proccesar ID: " + actual.nombre + " en el tiempo: " + str(reloj) + str("\n"))

        actual.tiempoInicio = reloj
        finalizo = False
        cambio = False
        while not cambio and not finalizo:

            reloj += 1
            actual.tiempocpu = actual.tiempocpu - 1

            print("PROCCESANDO ID: " + actual.nombre + "  Tiempo de cpu " + str(reloj) + " Cpu faltante: " + str(
                actual.tiempocpu))

            # IMPLEMENTAR EL CODIGO PARA EXPULSIVO
            total_cola_pacial = len(dar_cola_proccesos(reloj))

            if total_cola_pacial > 0:
                aux = dar_menor_rafaga_cola();

                if aux != actual:

                    for index in range(len(listaEspera)):
                        if actual.nombre == listaEspera[index]:
                            listaEspera[index] = actual

                    print("Se cambio por el procceso ID: " + actual.nombre + " por el procceso ID:  " + aux.nombre)
                    actual = aux
                    cambio = True

            if actual.tiempocpu == 0:
                centinela = False
                x = 0
                while not centinela and x <= len(listaEspera):

                    # Problema se queda en  while  se queda

                    if listaEspera[x].nombre == actual.nombre:
                        centinela = True
                        # Se quita bien de la lista de espera
                        actual.tiempoFinal = reloj
                        listaEspera.pop(x)
                        proccesados.append(actual)
                        listaCola.remove(actual)

                        print(
                            "\n" + "Se terminda de proccesar ID: " + actual.nombre + " en el tiempo: " + str(
                                reloj) + str(
                                "\n"))
                    x += 1

                finalizo = True




    else:
        reloj += 1
        print("tiempo de ocio")

print(proccesados)
