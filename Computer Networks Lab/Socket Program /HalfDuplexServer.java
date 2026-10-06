import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.ServerSocket;
import java.net.Socket;

public class HalfDuplexServer {
    public static void main(String[] args) {
        final int port = 5000;

        try (
            ServerSocket serverSocket = new ServerSocket(port);
            BufferedReader consoleReader = new BufferedReader(new InputStreamReader(System.in))
        ) {
            System.out.println("Half-duplex server started on port " + port);
            System.out.println("Waiting for client connection...");

            try (
                Socket socket = serverSocket.accept();
                BufferedReader socketReader = new BufferedReader(new InputStreamReader(socket.getInputStream()));
                PrintWriter socketWriter = new PrintWriter(socket.getOutputStream(), true)
            ) {
                System.out.println("Client connected: " + socket.getInetAddress());
                System.out.println("Type messages. Use 'exit' to end chat.");

                while (true) {
                    // Server turn: send one message.
                    System.out.print("Server: ");
                    String serverMessage = consoleReader.readLine();
                    if (serverMessage == null) {
                        break;
                    }
                    socketWriter.println(serverMessage);

                    if ("exit".equalsIgnoreCase(serverMessage.trim())) {
                        System.out.println("Chat ended by server.");
                        break;
                    }

                    // Client turn: receive one message.
                    String clientMessage = socketReader.readLine();
                    if (clientMessage == null) {
                        System.out.println("Client disconnected.");
                        break;
                    }

                    System.out.println("Client: " + clientMessage);
                    if ("exit".equalsIgnoreCase(clientMessage.trim())) {
                        System.out.println("Chat ended by client.");
                        break;
                    }
                }
            }
        } catch (IOException e) {
            System.out.println("Server error: " + e.getMessage());
        }
    }
}
