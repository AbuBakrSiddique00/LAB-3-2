import java.io.*;
import java.net.*;

public class client {
    public static void main(String[] args) throws Exception {
        Socket s = new Socket("localhost", 5001);
        System.out.println("Connected to server! Type 'stop' to exit.");

        BufferedReader in = new BufferedReader(new InputStreamReader(s.getInputStream()));
        PrintWriter out = new PrintWriter(s.getOutputStream(), true);
        BufferedReader kb = new BufferedReader(new InputStreamReader(System.in));

        String msg;
        while (true) {
            System.out.print("Client: ");
            msg = kb.readLine();
            out.println(msg);
            if (msg.equalsIgnoreCase("stop")) break;

            System.out.println("Server: " + in.readLine());
        }

        s.close();
        System.out.println("Client closed.");
    }
}