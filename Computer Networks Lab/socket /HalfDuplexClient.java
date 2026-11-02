import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class HalfDuplexClient {
    public static void main(String[] args) {
        final String host = "127.0.0.1";
        final int port = 5000;

        try (
            Socket socket = new Socket(host, port);
            BufferedReader socketReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
            PrintWriter socketWriter = new PrintWriter(socket.getOutputStream(), true);
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in))
        ) {
            System.out.println("Connected to server " + host + ":" + port);
            System.out.println("Type messages. Use 'exit' to end chat.");
    
            while (true) {
                // Server turn: receive one message.
                String serverMessage = socketReader.readLine(); 
                if (serverMessage == null) {
                    System.out.println("Server disconnected.");
                    break;
                }

                System.out.println("Server: " + serverMessage);
                if ("exit".equalsIgnoreCase(serverMessage.trim())) {
                    System.out.println("Chat ended by server.");
                    break;
                }

                // Client turn: send one message.
                System.out.print("Client: ");
                String clientMessage = consoleReader.readLine();
                if (clientMessage == null) {
                    break;
                }
                socketWriter.println(clientMessage);

                if ("exit".equalsIgnoreCase(clientMessage.trim())) {
                    System.out.println("Chat ended by client.");
                    break;
                }
            }
        } catch (IOException e) {
            System.out.println("Client error: " + e.getMessage());
        }
    }
}
