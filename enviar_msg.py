def enviar_mensagens(clientes: list):
    while True:
        print("Clientes:")

        # if(len(clientes) == 0):
        #     print("Não há clientes no momento. Aguarde a chegada de novos clientes...")
        
        for i, cliente in enumerate(clientes):
            print(f"{i} - {cliente.getpeername()}") 

        try:
            indice = int(input("Selecione qual cliente deverá receber a resposta: "))
            resposta = input("Digite a resposta: ")
            resposta = resposta + "\n"
            cliente = clientes[indice]
            cliente.send(resposta.encode("utf-8"))
        except Exception as e:
            print(f"\nErro inesperado: {e}")
            break