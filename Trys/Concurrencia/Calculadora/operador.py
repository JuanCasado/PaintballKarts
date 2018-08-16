from threading import Thread
from time import time


class Operador(Thread):
    def __init__(self, inicio, operacion, cantidad):
        Thread.__init__(self)
        self.inicio = inicio
        self.operacion = operacion
        self.cantidad = cantidad
        self.fin = self.inicio + self.cantidad
        self.resultado = 0
        self.time = 0

    def _to_string(self):
        print("from ", self.inicio, " does " + self.operacion + " until the reach of ", self.fin)

    def _to_string_extended(self):
        to_show = ""
        for operando in range(self.inicio, self.fin - 1):
            to_show += (str(operando) + " " + str(self.operacion) + " ")
        print(to_show, self.fin)

    def show_answer(self):
        self._to_string_extended()
        print("= ", self.resultado)
        print("in ", self.time)

    def get_answer(self):
        return self.resultado

    def get_time(self):
        return self.time

    def run(self):
        time_i = time()
        if self.operacion == "+":
            for operando in range (self.inicio, self.fin):
                self.resultado += operando
        elif self.operacion == "-":
            for operando in range (self.inicio, self.fin):
                self.resultado -= operando
        elif self.operacion == "*":
            self.resultado = 1
            for operando in range (self.inicio, self.fin):
                self.resultado *= operando
        elif self.operacion == "/":
            self.resultado = 1
            for operando in range (self.inicio, self.fin):
                if operando != 0:
                    self.resultado /= operando
        elif self.operacion == "pow":
            self.resultado = 1
            for operando in range(self.inicio, self.fin):
                self.resultado = pow(self.resultado, operando)
        time_f = time()
        self.time = time_f - time_i





