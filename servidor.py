import threading
import socket

clientes = []

def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(("localhost", 1212))
        servidor.listen()
        print("Servidor iniciado... \n")
    except Exception as e:
        print(f"\n Erro ao iniciar o servidor: {e} \n")
        return

    try:
        while True:
            cliente, addr = servidor.accept()
            clientes.append(cliente)
            print(f"Nova conexão {addr}. \n")

            thread = threading.Thread(target=mensagens, args=[cliente,addr])
            thread.start()
    except:
        servidor.close()
        print("Servidor encerrado.")

def mensagens(cliente,addr):
    mensagem = None

    while True:
        try:
            mensagem = cliente.recv(2048).decode("utf-8")
            if mensagem != None:
                broadcast(mensagem, cliente)
        except:
            print(f"Conexão {addr} encerrada. \n")
            deletar_cliente(cliente)
            cliente.close()
            break

def broadcast(mensagem,cliente):
    for clienteitem in clientes:
        if clienteitem != cliente:
            try:
                clienteitem.send(mensagem.encode("utf-8"))
            except Exception as e:
                print(f"Erro ao enviar mensagem para {clienteitem.getpeername()}: {e} \n")
                deletar_cliente(clienteitem)
             
def deletar_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)

if __name__ == "__main__":
    main()