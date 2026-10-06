import java.io.*;
import java.net.*;
import java.util.regex.*;

public class ftp {
    static Socket controlSocket;
    static BufferedReader reader;
    static PrintWriter writer;

    static String readResponse() throws IOException {
        String line;
        StringBuilder response = new StringBuilder();

        while ((line = reader.readLine()) != null) {
            System.out.println("< " + line);
            response.append(line).append('\n');

            // FTP response is complete when 3 digit code arrive fellowed by space
            if(line.matches("^\\d{3} .*")) {
                break;
            }


        }
        return response.toString();
    }

    // Send FTP command  
    static void sendCommand(String command) throws IOException {
        System.out.println("> " + command);
        writer.print(command + "\r\n");
        writer.flush();
    }

    public static void main(String[] args) {
        String server = "test.rebex.net";

        try {
            // 1. Connect FTP server
            controlSocket = new Socket(server, 21);
            reader = new  BufferedReader(
                new InputStreamReader(
                    controlSocket.getInputStream()));

            writer = new PrintWriter(
                controlSocket.getOutputStream(), true);
            System.out.println("Connected to " + server);

            // server welcome message
            readResponse();
            
            // 2. Login
            sendCommand("USER demo");
            readResponse();
            sendCommand("PASS password");
            readResponse();

            // 3. Enter passive mode
            sendCommand("PASV");
            String response = readResponse();


            Pattern pattern = Pattern.compile(
                "\\((\\d+),(\\d+),(\\d+),(\\d+),(\\d+),(\\d+)\\)"
            );

            Matcher matcher = pattern.matcher(response);

            if(!matcher.find()) {
                throw new IOException("Could not parse PASV response");
            }

            String dataIP = matcher.group(1) + "." + 
                            matcher.group(2) + "." +
                            matcher.group(3) + "." +
                            matcher.group(4);

            int p1 = Integer.parseInt(matcher.group(5));
            int p2 = Integer.parseInt(matcher.group(6));

            int dataPort = p1 * 256 + p2;

            System.out.println("Data IP: " + dataIP);
            System.out.println("Data Port: " + dataPort);
         
            // 4. Connect to data port 
            Socket dataSocket = new  Socket(dataIP, dataPort);
            
            // 5. Request directory listing 
            sendCommand("LIST");
            readResponse();

            // 6. Read dictionary listing
            BufferedReader dataReader = new BufferedReader(
                new InputStreamReader(dataSocket.getInputStream()));
            
            System.out.println("\n===== Directory Listing =====");
            String line;
            while ((line = dataReader.readLine()) != null) {
                System.out.println(line);
            }
            dataReader.close();
            dataSocket.close();

            // 7. Read final FTP response 
            readResponse();
            
            // 8. Logout
            sendCommand("QUIT");
            readResponse();
            controlSocket.close();
            System.out.println("\n Server Disconnected.");
            } catch(Exception e) {
                e.printStackTrace();
            }
    }
}
