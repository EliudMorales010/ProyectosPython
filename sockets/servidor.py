import socket
nombre = input("Nombre de usuario (Servidor):")
ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ss.bind(("localhost", 8000))
ss.listen(1)
con, datos = ss.accept()

while True:
    mensajeServidor = input(nombre + " Escribe: ")
    con.send(mensajeServidor.encode())
    mensajeCliente = con.recv(1024)
    mensajeCliente2 = mensajeCliente.decode()
    print("Cliente dice: ", mensajeCliente2)