import threading
import socket

clientes = []

def main():
    #                        Endereços IPv4 - protocolo TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(("localhost", 1227))
        servidor.listen()
        print("Servidor iniciado... \n")
    except Exception as e:
        print(f"\n Erro ao iniciar o servidor: {e} \n")
        return

    while True:
        try:
            cliente, addr = servidor.accept()
            clientes.append(cliente)
            print(f"\n Nova conexão {addr}. \n")

            thread1 = threading.Thread(target=receber_mensagens, args=[cliente])
            thread2 = threading.Thread(target=enviar_mensagens, args=[cliente])

            thread1.start()
            thread2.start()
        except:
            print("conexão encerrada.")
            break
    servidor.close()

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            if mensagem:
                print(f"\n{mensagem}")
            elif mensagem.lower() == "exit":
                deletar_cliente()
        except:
            break
        
def enviar_mensagens(cliente):
    while len(clientes) > 0:
        print("Clientes:")
        for i, cliente in enumerate(clientes):
            print(f"{i} - {cliente.getpeername()}") 

        try:
            indice = int(input("Selecione qual cliente deverá receber a resposta: "))
            resposta = input("Digite a resposta: ")
            cliente = clientes[indice]
            cliente.send(resposta.encode("utf-8"))
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            break
        
def deletar_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        print(f"Conexão com {cliente.getpeername()} encerrada.")

if __name__ == "__main__":
    main()
