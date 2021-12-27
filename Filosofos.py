import argparse
import threading
import time
import random

estadoFilosofo = None # vacio
candados = [] # declaro una lista para los candados
cantidad_filosofos = 0 
maximo_intetos_fallidos = 10 
rafaga_comer = 0
total_tiempo_comer = 0   

# Estados de los filosofos
estado_filosofando = "F" # estado en el que estan pensando
estado_hambriento = "H"
estado_comiendo = "C"
estado_satisfecho = "S"
estado_muerto = "M"

def agarrarTenedor(id_filosofo):
    """ Objetivo: Tratar de tomar los tenedores izquierdo y derecho en ese orden y 
    devuelve verdadero si ha podido adquirir ambos y Falso si es lo contrario"""
    tenedor_izq = candados[id_filosofo]
    tenedor_der = candados[(id_filosofo - 1) % cantidad_filosofos]
    tenedor_izq.acquire()
    
    if tenedor_der.acquire(blocking = False):
        return True
    else:
        tenedor_izq.release()# Liberar un semáforo, incrementando su contador interno en una unidad. Si era cero a la entrada y otro hilo está esperando a que sea mayor que cero, despertar a dicho hilo.
        return False


def soltarTenedor(id_filosofo):
    """ Soltar los tenedores del filosofo """
    candados[id_filosofo].release()
    candados[(id_filosofo - 1) % cantidad_filosofos].release()


# Función que va ejecutar cada filosofo o cada hilo
def iniciar(id_filosofo):
    intentos_fallidos = 0
    tiempo_comiendo = 0

    # mientras que el tiempo en que esté comiendo no rebase del tiempo total que tiene cada filosofo
    while tiempo_comiendo < total_tiempo_comer: 
        if agarrarTenedor(id_filosofo):
            # Limpiar los intentos, ya que ya ha terminado de comer
            intentos_fallidos = 0

            # Filosofo comiendo
            tiempo_comer = min(rafaga_comer, total_tiempo_comer - tiempo_comiendo)
            tiempo_comiendo += tiempo_comer
            print(f"Filosofo {id_filosofo} comiendo se tarda: [{tiempo_comer} seg.]")
            time.sleep(tiempo_comiendo)
            soltarTenedor(id_filosofo)

            # Filosofo pensando
            estadoFilosofo[id_filosofo] = estado_filosofando
            tiempo_filosofar = random.uniform(0, 5) # creo una variable para que me de un rango de numeros entre 0 y 5 
            print(f"Filosofo {id_filosofo} pensando se tarda: [{tiempo_filosofar:.2f} seg.]")
            time.sleep(tiempo_filosofar)
        else:
            # si el estado del filosofo es hambriento, entonces los intentos fallidos se acumularán
            estadoFilosofo[id_filosofo] = estado_hambriento
            intentos_fallidos += 1

            if intentos_fallidos >= maximo_intetos_fallidos: # si los intentos fallidos rebasan el limite el filosofo muere 
                estadoFilosofo[id_filosofo] = estado_muerto
                print(f" Filosofo {id_filosofo} muerto")
                return
            
            tiempo_reintentar = random.uniform(0, 3)
            print(f"Filosofo {id_filosofo} esperando los tenedores"
                  f" Intento {intentos_fallidos} [{tiempo_reintentar:.2f} seg.]")
            time.sleep(tiempo_reintentar)
        
def obtenerArgumentos():
    """ Función que lee los argumentos pasados por la línea de comandos """
    parser = argparse.ArgumentParser()
    parser.add_argument("-n", "--num_filosofos", 
                        type=int, default=5, help="Número de Filósofos")
    parser.add_argument("-r", "--rafaga_comer", 
                        type=int, default=4, help="Ráfaga de comer de los filósofos")
    parser.add_argument("-t", "--tiempo_total", 
                        type=int, default=10, help="Tiempo total que necesita comer un filosofo ")
    parser.add_argument("-i", "--num_intentos", 
                        type=int, default=10, help="Todos los intentos antes de que el filósofo muera")
    return parser.parse_args()


if __name__ == '__main__':
    args = obtenerArgumentos()

    # Establecer los argumentos leídos por línea de comandos
    cantidad_filosofos = args.num_filosofos
    rafaga_comer = args.rafaga_comer
    total_tiempo_comer = args.tiempo_total
    maximo_intetos_fallidos = args.num_intentos

    estadoFilosofo = cantidad_filosofos * [estado_filosofando] # multiplico la cantidad por el estado en el que estan los filosofos

    # Inicialización de candados
    for i in range(cantidad_filosofos):
        candados.append(threading.RLock())

    hilos = [] # declaro una lista donde almacenarán los hilos
    for i in range(args.num_filosofos): 
        nuevo_hilo = threading.Thread(target = iniciar, args=(i,)) # creo un hilo
        hilos.append(nuevo_hilo)
    
    # Iniciar ejecución de los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar a que terminen los hilos
    for hilo in hilos:
        hilo.join()
