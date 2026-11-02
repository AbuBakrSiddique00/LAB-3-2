import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.Socket;

public class client {
    public static void main(String[] args) throws Exception {
        Socket s2 = new Socket("localhost", 7777);
        DataOutputStream dos = new DataOutputStream(s2.getOutputStream());
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            System.out.print("Enter message (type exit to stop): ");
            String msg = br.readLine();

            if (msg.equalsIgnoreCase("exit")) {
                dos.writeUTF(msg);
                dos.flush();
                break;
            }

            dos.writeUTF(msg);
            dos.flush();
        }

        s2.close();
    }
}