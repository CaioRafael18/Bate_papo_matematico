import threading
import socket

def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(("localhost", 1212))
    except:
        print("Não foi possivel se conectar ao servidor! \n")
        return 

    usuario = input("Usuário: ")
    print(f'\n{usuario} Conectado. \nQuando desejar encerrar a conexão, digite "exit". \n')

    thread1 = threading.Thread(target=receber_mensagens, args=[cliente])
    thread2 = threading.Thread(target=enviar_mensagens, args=[cliente, usuario])

    thread1.start()
    thread2.start()
    
    thread1.join()
    thread2.join()

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            if mensagem:
                print(f"\n{mensagem}")
            else:
                print("\nConexão encerrada pelo servidor.")
                break
        except:
            break

def enviar_mensagens(cliente,usuario):
    while True:
        try:
            mensagem = input("\n ")
            cliente.send(f'<{usuario}> {mensagem}\n'.encode("utf-8"))
            if mensagem.lower() == "exit":
                print("Encerrando a conexão...")
                cliente.close()
                break
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            break

if __name__ == "__main__":
    main()
