class Procceso:
    tiempoInicio = 0
    tiempoFinal = 0

    tiempocpu = 0
    tiempollega = 0
    nombre = "cc"
    prioridad = 0

    def __init__(self, nombre, cpu, llega, pri):
        self.nombre = nombre
        self.tiempocpu = cpu
        self.tiempollega = llega
        self.prioridad = pri

    def imprimir(self):
        print("Procceso ID: " + self.nombre + " Tiempo de ejecucion: " + str(
            self.tiempocpu) + " Tiempo de llegada: " + str(self.tiempollega))
