import threading
import socket
import subprocess

import enviar_msg


# Abrir dois novos terminais, cada um rodando um script diferente
# subprocess.run('start cmd /k "python script1.py"', shell=True)
# subprocess.run('start cmd /k "python script2.py"', shell=True)

def main():
    #                        Endereços IPv4 - protocolo TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientes = []

    try:
        servidor.bind(("localhost", 1212))
        servidor.listen()
        print("Servidor iniciado... \n")

        enviaThread = threading.Thread(target=enviar_msg.enviar_mensagens, args=[clientes])
        enviaThread.start()
        
    except Exception as e:
        print(f"\n Erro ao iniciar o servidor: {e} \n")
        return

    while True:
        try:
            cliente, addr = servidor.accept()
            clientes.append(cliente)
            print(f"\nNova conexão {addr}. \n")

            recebeThread = threading.Thread(target=receber_mensagens, args=[cliente])
            recebeThread.start()
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

def deletar_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        print(f"Conexão com {cliente.getpeername()} encerrada.")

if __name__ == "__main__":
    main()
