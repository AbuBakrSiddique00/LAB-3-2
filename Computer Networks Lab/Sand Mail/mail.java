import java.io.*;
import java.time.LocalDateTime;
import javax.net.ssl.*;
import java.util.*;

public class mail {

    private static DataOutputStream dos;
    public static BufferedReader br;

    public static void main(String[] args) throws Exception {
        String user = "s2310476140@ru.ac.bd";
        String pass = "woqdyoiipgmehiru";


        String username = new String(Base64.getEncoder().encode(user.getBytes()));
        String password = new String(Base64.getEncoder().encode(pass.getBytes()));
        SSLSocket s = (SSLSocket) SSLSocketFactory.getDefault().createSocket("smtp.gmail.com", 465);
        dos = new DataOutputStream(s.getOutputStream());
        br = new BufferedReader(new InputStreamReader(s.getInputStream()));
        send("EHLO smtp.gmail.com\r\n");
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());
            System.out.println("SERVER: " + br.readLine());

        send("AUTH LOGIN\r\n");
            System.out.println("SERVER: " + br.readLine());
        send(username + "\r\n");
            System.out.println("SERVER: " + br.readLine());
        send(password + "\r\n");
            System.out.println("SERVER: " + br.readLine());
        send("MAIL FROM:<s2310476140@ru.ac.bd>\r\n");
            System.out.println("SERVER: " + br.readLine());
        send("RCPT TO:<asif@ru.ac.bd>\r\n");
            System.out.println("SERVER: " + br.readLine());
        send("DATA\r\n");
            System.out.println("SERVER: " + br.readLine());


        send("FROM: s2310476149@ru.ac.bd\r\n");
        send("TO: asif@ru.ac.bd\r\n");
        send("Subject: Test Mail\r\n");
        send("This is Abu Backer Siddique\r\n");
        send("Roll No.: 2310476140\r\n");
        send("MAC address: d4:6d:6d:e2:ff:59\r\n");

        send(".\r\n");
            System.out.println("SERVER: " + br.readLine());

        send("QUIT\r\n");
            System.out.println("SERVER: " + br.readLine());

    }
    private static void send(String s) throws Exception {
        dos.writeBytes(s);
        Thread.sleep(1000);
        System.out.println("CLIENT: " + s);
    }
    
}
