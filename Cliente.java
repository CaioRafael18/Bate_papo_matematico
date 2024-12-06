

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintStream;
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
        try {
            System.out.println("OOOppaaa");
            BufferedReader mensagem = new BufferedReader(new InputStreamReader(cliSocket.getInputStream()));
            System.out.println("Mensage: " + mensagem);
            while (mensagem.readLine() != null) {
                System.out.println("Servidor: " + mensagem.readLine());
            }
        } catch (Exception e) {
            System.out.print("\nErro inesperado: " + e);
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
            Scanner teclado = new Scanner(System.in);

            PrintStream saida = new PrintStream(cliSocket.getOutputStream());
            while (teclado.hasNextLine()) {
                if (teclado.nextLine().equalsIgnoreCase("exit")) {
                    System.out.println("Encerrando conexão...");
                    cliSocket.close();
                    teclado.close();
                    break;
                }
                saida.println(teclado.nextLine());
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
            System.out.print(usuario + " conectado. \nQuando desejar encerrar a conexão, digite 'exit'. \n");

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