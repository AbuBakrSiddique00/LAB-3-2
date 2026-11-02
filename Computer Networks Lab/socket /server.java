import java.io.DataInputStream;
import java.net.ServerSocket;
import java.net.Socket;

public class server {
    public static void main(String[] agrs) throws Exception {
        ServerSocket ss = new ServerSocket(7777);
        System.out.println("Server started... waiting for client");

        while (true) {
            Socket s = ss.accept();
            System.out.println("Client connected");

            DataInputStream dis = new DataInputStream(s.getInputStream());

            while (true) {
                String msg = dis.readUTF();
                
                if (msg.equalsIgnoreCase("exit")) {
                    System.out.println("Client disconnected");
                    break;
                }
                System.out.println("Message from client: " + msg);
            }

            s.close();
        }
    }
}