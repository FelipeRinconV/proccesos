from Procceso import Procceso

p1 = Procceso("P1", 5, 20, 5)
p2 = Procceso("P2", 2, 20, 3)
p3 = Procceso("P3", 10, 20, 20)

lista_preparados = [p1, p2, p3]

total_proccesos = len(lista_preparados)

lista_cola = [p1]
lista_cola.pop()

lista_proccesados = [p1]
lista_proccesados.pop()


def dar_cola(reloj_cpu):
    for indice in range(len(lista_preparados)):
        if lista_preparados[indice].tiempollega <= reloj_cpu:
            lista_cola.append(lista_preparados[indice])

    lista_cola.sort(key=lambda x: x.prioridad)
    lista_cola.reverse()
    return lista_cola


def eliminar_preparados(lista):
    lista_copia = lista
    for x in lista_copia:
        for y in lista_preparados:
            if x.nombre == y.nombre:
                lista_preparados.remove(y)


# Inicio del algoritmo prioridad no expulsivo funciona
def prioritario_no_expulsivo():
    reloj = 0
    while len(lista_proccesados) != total_proccesos:

        cola_aux = dar_cola(reloj)
        eliminar_preparados(cola_aux)

        if cola_aux:

            actual = cola_aux[0]

            while actual.tiempocpu >= 0:
                reloj += 1
                actual.tiempocpu = actual.tiempocpu - 1
                print("PROCESANDO ID: " + actual.nombre + " reloj: " + str(reloj))

            lista_proccesados.append(actual)
            print("\n"+ "----------------------------------")
            print("SE PROCCESO ID: " + actual.nombre + " reloj: " + str(reloj))
            lista_cola.remove(actual)
        else:
            print("Ocio")
            reloj += 1


prioritario_no_expulsivo()

print(len(lista_proccesados))
