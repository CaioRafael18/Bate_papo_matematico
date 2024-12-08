import tkinter as tk

class Tela:
    def __init__(self, enviar_mensagens, iniciar_servidor):
        self.enviar_mensagens = enviar_mensagens
        self.iniciar_servidor = iniciar_servidor

    def iniciar(self):
        # Configuração da interface grafica
        tela = tk.Tk()
        tela.title("Chat")

        # Janela principal
        frame_principal = tk.Frame(tela)
        frame_principal.pack(padx=20, pady=20)

        # Lista de clientes conectados
        self.lista_clientes = tk.Listbox(frame_principal, width=40, height=13)
        self.lista_clientes.pack(side=tk.LEFT, padx=20)

        # Area de mensagens recebidas
        self.mensagens = tk.Text(frame_principal, width=60, height=30, state=tk.DISABLED)
        self.mensagens.pack(side=tk.RIGHT, padx=20)

        # Area de entrada de resposta
        frame_entrada = tk.Frame(tela)
        frame_entrada.pack(padx=10, pady=10)

        # Input do indice
        self.indice_cliente = tk.Entry(frame_entrada, width=5)
        self.indice_cliente.pack(side=tk.LEFT, padx=10)

        # Input da resposta
        self.resposta_servidor = tk.Entry(frame_entrada, width=40)
        self.resposta_servidor.pack(side=tk.LEFT, padx=10)

        # Botão para enviar a resposta
        botao_enviar = tk.Button(frame_entrada, text="Enviar", command=self.enviar_mensagens)
        botao_enviar.pack(side=tk.LEFT, padx=10)

        # Botão iniciar servidor
        botao_servidor = tk.Button(tela, text="Iniciar Servidor", command=self.iniciar_servidor)
        botao_servidor.pack(pady=10)

        # Inicia a interface grafica e mantem ela ate ser fechada
        tela.mainloop()