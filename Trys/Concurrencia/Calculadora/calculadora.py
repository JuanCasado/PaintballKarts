from Calculadora.operador import Operador
from time import time

tiempo_i = time()
resultado = 1
for operando in range(1, 400001):
    resultado *= operando
tiempo_f = time()
print("= ", resultado)
print("in ", tiempo_f - tiempo_i)

print("---------")

operador_1 = Operador(1, "*", 100000)
operador_2 = Operador(100001, "*", 100000)
operador_3 = Operador(200001, "*", 100000)
operador_4 = Operador(300001, "*", 100000)
operador_1.start()
operador_2.start()
operador_3.start()
operador_4.start()
operador_1.join()
operador_2.join()
operador_3.join()
operador_4.join()
print("= ", operador_1.get_answer()*operador_2.get_answer()*operador_3.get_answer()*operador_4.get_answer())
print("in ", operador_1.get_time()+operador_2.get_time()+operador_3.get_time()+operador_4.get_time())
