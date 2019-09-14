from Procceso import Procceso

p1 = Procceso("P1", 8, 3, 3)
p2 = Procceso("P2", 20, 10, 11)
p3 = Procceso("P3", 40, 5, 10)

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

    return lista_cola


def eliminar_preparados(lista):
    lista_copia = lista
    for x in lista_copia:
        for y in lista_preparados:
            if x.nombre == y.nombre:
                lista_preparados.remove(y)


def prioridad_expulsivo():
    reloj = 0
    while not len(lista_proccesados) == total_proccesos:

        cola_aux = dar_cola(reloj)
        eliminar_preparados(cola_aux)
        if cola_aux:

            cola_aux.sort(key=lambda x: x.prioridad)
            cola_aux.reverse()

            print(" Reloj: " + str(reloj))
            actual = cola_aux[0]

            print("Se esta proccesando: " + actual.nombre)
            actual.tiempocpu = actual.tiempocpu - 1

            if actual.tiempocpu == 0:
                lista_proccesados.append(actual)
                print("Se procceso: " + actual.nombre)
                cola_aux.remove(actual)
        else:
            print("Ocio " + str(reloj))
        reloj += 1


prioridad_expulsivo()

print("ORDEN DE PROCCESADO")
for p in lista_proccesados:
    print(p.nombre+"--")
