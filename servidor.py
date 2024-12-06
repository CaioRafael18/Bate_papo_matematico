import threading
import socket
from Modelo import Modelo

clientes = []

def main():
    #                        Endereços IPv4 - protocolo TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(("localhost", 1212))
        servidor.listen()
        print("Servidor iniciado... \n")
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e} \n")
        return

    while True:
        try:
            cliente, addr = servidor.accept()
            clientes.append(cliente)
            print(f"Nova conexão {addr}. \n")

            modelo = Modelo(cliente, clientes)

            thread1 = threading.Thread(target=modelo.receber_mensagens)

            thread1.start()
        except Exception as e:
            print(f"Erro na conexão: {e} \n")
            break
    servidor.close()

if __name__ == "__main__":
    main()
