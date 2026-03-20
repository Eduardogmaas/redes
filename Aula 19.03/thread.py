import threading
from time import sleep

def tarefa():
    print("Executando tarefa...")
    for i in range(10):
        print(i)
        sleep(1)
    # sleep(5)
    # print("Tarefa finalizada")


# tarefa()

t0 = threading.Thread(target=tarefa)
t1 = threading.Thread(target=tarefa)
t0.start()
t1.start()
# sleep(1)
# print("Aguardando thread finalizar")
t0.join()
t1.join()

print("Finalizado")