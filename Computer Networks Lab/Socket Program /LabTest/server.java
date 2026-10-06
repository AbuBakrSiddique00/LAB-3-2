import java.io.*;
import java.net.*;

public class server {
    public static void main(String[] args) throws Exception {
        ServerSocket ss = new ServerSocket(5001);
        System.out.println("Server started. Waiting for client...");
        
        Socket s = ss.accept();
        System.out.println("Client connected!");

        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));

        String msg;
        while ((msg = in.readLine()) != null && !msg.equalsIgnoreCase("stop")) {
            System.out.println("Client: " + msg);
            System.out.print("Server: ");
            out.println(kb.readLine());
        }

        s.close();
        ss.close();
        System.out.println("Server closed.");
    }
}
