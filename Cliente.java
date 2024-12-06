

import java.io.IOException;
import java.io.PrintWriter;
import java.net.Socket;
import java.net.UnknownHostException;
import java.util.Scanner;

class Receber_mensagens extends Thread {
    private Socket cliSocket;

    public Receber_mensagens(Socket cliSocket) {
        this.cliSocket = cliSocket;
    }

    @Override
    public void run() {
        while (true) {
            try {
                Scanner scanner = new Scanner(cliSocket.getInputStream());
                while (scanner.hasNextLine()) {
                    System.out.println("Servidor: " + scanner.nextLine());
                }
                scanner.close();
            } catch (Exception e) {
                System.out.print("\nErro inesperado: " + e);
                break;
            }
        }
    }   
}

class Enviar_mensagens extends Thread {
    private Socket cliSocket;

    public Enviar_mensagens(Socket cliSocket) {
        this.cliSocket = cliSocket;
    }

    @Override
    public void run() {
        try {
            System.out.println("Digite mensagens para o servidor (ou 'exit' para encerrar):");

            Scanner teclado = new Scanner(System.in);
            PrintWriter saida = new PrintWriter(cliSocket.getOutputStream(), true);
            while (teclado.hasNextLine()) {
                String mensagem = teclado.nextLine();
                if (mensagem.equalsIgnoreCase("exit")) {
                    System.out.println("Encerrando conexão...");
                    teclado.close();
                    cliSocket.close();
                    break;
                }
                saida.println(mensagem);
            }
        } catch (Exception e) {
            System.out.print("\nErro inesperado: " + e);
        }
    }   
}

public class Cliente {
    public static void main(String[] args) throws UnknownHostException, IOException, InterruptedException {
        try {
            Socket cliente = new Socket("localhost", 1212);
            Scanner teclado = new Scanner(System.in);
            System.out.println("Conectado ao servidor!");
            System.out.print("Usuário: ");
            String usuario = teclado.next();
            System.out.println(usuario + " conectado.");

            Thread recebeThread = new Receber_mensagens(cliente);
            recebeThread.start();

            Thread enviaThread = new Enviar_mensagens(cliente);
            enviaThread.start();

            recebeThread.join();
            enviaThread.join();
            
            teclado.close();
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}

