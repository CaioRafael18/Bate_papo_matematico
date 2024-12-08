import threading
import socket
import tkinter as tk
from tkinter import messagebox
from Tela import Tela

clientes = []

# Função para conectar com o servidor
def conectar_servidor():
    #                        Endereços IPv4 - protocolo TCP
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        servidor.bind(("localhost", 1212))
        servidor.listen()
        print("Servidor iniciado... \n")
        enviarThread = threading.Thread(target=enviar_mensagens)
        enviarThread.daemon = True
        enviarThread.start()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao iniciar o servidor: {e}")
        return

    while True:
        try:
            cliente, addr = servidor.accept()
            clientes.append(cliente)
            atualizar_clientes()

            receberThread = threading.Thread(target=receber_mensagens, args=[cliente])
            receberThread.daemon = True
            receberThread.start()
        except:
            messagebox.showerror("Erro", f"Erro ao se conectar com o cliente: {e}")
            break
    servidor.close()
        
# Função para enviar mensagens para o cliente selecionado
def enviar_mensagens():
    if len(clientes) > 0:
        try:
            indice = int(tela.indice_cliente.get())
            resposta = tela.resposta_servidor.get() + "\n"
            cliente = clientes[indice]
            cliente.send(resposta.encode("utf-8"))
            exibe_mensagem(cliente, resposta, "server")
            tela.mensagens.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar mensagem: {e}")

# Função para atualizar a lista de clientes toda vez que um novo cliente entrar ou sair
def atualizar_clientes():
    tela.lista_clientes.delete(0, tk.END) 
    for i, cliente in enumerate(clientes):
        tela.lista_clientes.insert(tk.END, f"{i} - {cliente.getpeername()}")

# Função para tratar as mensagens enviadas dos clientes
def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(2048).decode('utf-8')
            if mensagem:
                exibe_mensagem(cliente, mensagem, "cliente")
            elif mensagem.lower() == "exit":
                deletar_cliente(cliente)
            else:
                deletar_cliente(cliente)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao receber mensagem: {e}")

# Função para exibir as mensagens na area de mensagens recebidas
def exibe_mensagem(cliente, mensagem, tipo):
    tela.mensagens.config(state=tk.NORMAL)
    if(tipo == "server"):
        tela.mensagens.insert(tk.END, f"Enviado para <{cliente.getpeername()}>: {mensagem} \n")
    else:
        tela.mensagens.insert(tk.END, f"{mensagem} \n")
    tela.mensagens.yview(tk.END)
    tela.mensagens.config(state=tk.DISABLED)

# Função para remover o cliente da lista
def deletar_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        atualizar_clientes()

# Função para iniciar a thread do servidor
def iniciar_servidor():
    iniciarServerThread = threading.Thread(target=conectar_servidor)
    # Interrompe a conexão quando fechar a janela da interface
    iniciarServerThread.daemon = True 
    iniciarServerThread.start()

tela = Tela(enviar_mensagens=enviar_mensagens, iniciar_servidor=iniciar_servidor)
tela.iniciar()