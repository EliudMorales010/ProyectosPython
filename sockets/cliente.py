import socket

nombre = input("Nombre de Usuario (Cliente): ")
sc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sc.connect(("localhost", 8000))

while True:
    mensajeServidor = (sc.recv(1024)).decode()
    print("Servidor dice: " , mensajeServidor)
    mensajeCliente = input("Escribe: ")
    sc.send(mensajeCliente.encode())