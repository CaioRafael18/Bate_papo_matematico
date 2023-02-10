import threading
import socket
import time 

def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect(("localhost", 1010))
    except:
        return print("\n não foi possivel se conectar ao servidor! \n")

    usuario = input("Usuário> ")
    print(f'\n {usuario} Conectado \n Quando desejar encerrar a conexão é só digitar "exit" \n Digite "calculadora" para acessar a Mini Calculadora')

    thread1 = threading.Thread(target=receber_mensagens,args =[cliente])
    thread2 = threading.Thread(target=enviar_mensagens,args =[cliente,usuario])

    thread1.start()
    thread2.start()
    
def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            print(mensagem+"\n")
        except:
            time.sleep(1)
            print("Agradecemos pela preferência, espero que tenha gostado dos nossos serviços!")
            print("Desconectando...")
            time.sleep(3)
            print("Cliente desconectado")
            break

def enviar_mensagens(cliente,usuario):
    while True:
        try:
            mensagem = input("\n")
            cliente.send(f' <{usuario}> {mensagem}'.encode("utf-8"))
            if(mensagem == "exit"):
                cliente.close()
                break
            if(mensagem == "calculadora"):
                print("---------")
                print("Entrando na Mini Calculadora...")
                time.sleep(2)
                print(" Digite '1' Para somar \n Digite '2' para Subtrair \n Digite '3' para Multiplicar \n Digite '4' para Dividir \n Quando desejar sair é só digitar 'sair' \n")
                escolha = input("O que você deseja?")
                while(escolha != "sair"):
                    print("---------")
                    if(escolha == "1"):
                        soma()
                    if(escolha == "2"):
                        subtracao()
                    if(escolha == "3"):
                        multiplicacao()
                    if(escolha == "4"):
                        divisao()
                    escolha = input("Oque você deseja agora? ")
        except:
            return

def soma():
    n1 = int(input("Digite um Numero:"))
    n2 = int(input("Digite outro Numero:"))
    soma = n1+n2
    print(f'A Soma de {n1} e {n2} é igual a {soma}')
    print("---------")

def subtracao():
    n1 = int(input("Digite um Numero:"))
    n2 = int(input("Digite outro Numero:"))
    subtracao = n1-n2
    print(f'A Subtracao de {n1} e {n2} é igual a {subtracao}')
    print("---------")

def multiplicacao():
    n1 = int(input("Digite um Numero:"))
    n2 = int(input("Digite outro Numero:"))
    multiplicacao = n1*n2
    print(f'A Multiplicacao de {n1} e {n2} é igual a {multiplicacao}')
    print("---------")

def divisao():
    n1 = int(input("Digite um Numero:"))
    n2 = int(input("Digite outro Numero:"))
    divisao = n1 / n2
    print(f'A Divisao de {n1} e {n2} é igual a {divisao}')
    print("---------")

main()