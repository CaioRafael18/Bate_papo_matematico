import threading
import socket
import tkinter as tk
from tkinter import messagebox

clientes = []
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
        
def enviar_mensagens():
    if len(clientes) > 0:
        try:
            indice = int(indice_cliente.get())
            resposta = resposta_servidor.get() + "\n"
            cliente = clientes[indice]
            cliente.send(resposta.encode("utf-8"))
            exibe_mensagem(cliente, resposta, "server")
            mensagens.delete(0, tk.END)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao enviar mensagem: {e}")

def atualizar_clientes():
    lista_clientes.delete(0, tk.END) 
    for i, cliente in enumerate(clientes):
        lista_clientes.insert(tk.END, f"{i} - {cliente.getpeername()}")

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

def exibe_mensagem(cliente, mensagem, tipo):
    mensagens.config(state=tk.NORMAL)
    if(tipo == "server"):
        mensagens.insert(tk.END, f"Para <{cliente.getpeername()}> {mensagem} \n")
    else:
        mensagens.insert(tk.END, f"{mensagem} \n")
    mensagens.yview(tk.END)
    mensagens.config(state=tk.DISABLED)

def deletar_cliente(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        atualizar_clientes()

# Função para iniciar a thread do servidor
def iniciar_servidor():
    iniciarServerThread = threading.Thread(target=conectar_servidor)
    # Responsável por efetivamente acabar com a thread
    # Pois ela ficava ligada mesmo após fechar o console 
    iniciarServerThread.daemon = True 
    iniciarServerThread.start()

# Configuração da interface gráfica
tela = tk.Tk()
tela.title("Chat")

# Janela principal
frame_principal = tk.Frame(tela)
frame_principal.pack(padx=20, pady=20)

# Lista de clientes conectados
lista_clientes = tk.Listbox(frame_principal, width=40, height=13)
lista_clientes.pack(side=tk.LEFT, padx=20)

# Área de mensagens recebidas
mensagens = tk.Text(frame_principal, width=60, height=30, state=tk.DISABLED)
mensagens.pack(side=tk.RIGHT, padx=20)

# Área de entrada de resposta
frame_entrada = tk.Frame(tela)
frame_entrada.pack(padx=10, pady=10)

indice_cliente = tk.Entry(frame_entrada, width=5)
indice_cliente.pack(side=tk.LEFT, padx=10)
resposta_servidor = tk.Entry(frame_entrada, width=40)
resposta_servidor.pack(side=tk.LEFT, padx=10)

# Botão para enviar a resposta
botao_enviar = tk.Button(frame_entrada, text="Enviar", command=enviar_mensagens)
botao_enviar.pack(side=tk.LEFT, padx=10)

# Botão iniciar servidor
botao_servidor = tk.Button(tela, text="Iniciar Servidor", command=iniciar_servidor)
botao_servidor.pack(pady=10)

# Inicia a interface gráfica
tela.mainloop()
