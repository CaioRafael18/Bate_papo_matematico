import threading
import socket

clientes = []

def main():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(("localhost", 1010))
        servidor.listen()
    except:
        return print("\n O servidor ja Está Conectado \n")


    while clientes != 0:
        cliente, addr = servidor.accept()
        clientes.append(cliente)

        thread = threading.Thread(target=mensagens, args=[cliente])
        thread.start()
    servidor.close()

def mensagens(cliente):
    mensagem = None
    while mensagem != "exit":
        try:
            mensagem = cliente.recv(2048)
            brodcast(mensagem,cliente)
        except:
            deletar_clientes(cliente)
            break

def brodcast(mensagem,cliente):
    for clienteitem in clientes:
        if clienteitem != cliente:
            try:
                clienteitem.send(mensagem)
            except:
                deletar_clientes(clienteitem)
             
def deletar_clientes(cliente):
    clientes.remove(cliente)

main()