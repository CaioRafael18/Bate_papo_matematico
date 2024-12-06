class Modelo:
    def __init__(self, cliente, clientes):
        self.cliente = cliente
        self.clientes = clientes

    def receber_mensagens(self):
        while True:
            try:
                mensagem = self.cliente.recv(2048).decode('utf-8')
                if mensagem:
                    print(f"\n{mensagem}")
                    self.enviar_mensagens()
                elif mensagem.lower() == "exit":
                    self.deletar_cliente()
            except:
                print("Erro ao receber mensagem.")
                break

    def enviar_mensagens(self):
        print("Clientes:")
        for i, cliente in enumerate(self.clientes):
            print(f"{i} - {cliente.getpeername()}") 

        indice = int(input("Selecione qual cliente responder: "))
        resposta = input("Digite a resposta: ")
        cliente = self.clientes[indice]
        cliente.send(resposta.encode("utf-8"))

    def deletar_cliente(self):
        if self.cliente in self.clientes:
            self.clientes.remove(self.cliente)
            print(f"Conexão com {self.cliente.getpeername()} encerrada.")
            self.cliente.close()