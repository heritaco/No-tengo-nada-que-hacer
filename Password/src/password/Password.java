package password;

import java.io.FileWriter;
import java.io.IOException;
import java.util.Random;
import java.util.Scanner;

public class Password {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        while (true) {
            // Generate a password
            String password = generatePassword(99); // You can change the length as needed

            // Get the filename from the user
            System.out.print("Enter the filename (without extension) or 'exit' to quit: ");
            String filename = scanner.nextLine();

            // Check if the user wants to exit
            if ("exit".equalsIgnoreCase(filename)) {
                break;
            }

            // Save the password to the file
            try {
                savePasswordToFile(password, filename);
                System.out.println("Password saved to " + filename + ".txt");
            } catch (IOException e) {
                System.out.println("An error occurred while saving the password to the file.");
                e.printStackTrace();
            }
        }

        scanner.close();
    }

    public static String generatePassword(int length) {
        String characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                + "abcdefghijklmnopqrstuvwxyz"
                + "0123456789.";
        StringBuilder password = new StringBuilder(length);
        Random random = new Random();

        for (int i = 0; i < length; i++) {
            int index = random.nextInt(characters.length());
            password.append(characters.charAt(index));
        }

        return password.toString();
    }

    public static void savePasswordToFile(String password, String filename) throws IOException {
        // Ensure the filename has the .txt extension
        if (!filename.endsWith(".txt")) {
            filename += ".txt";
        }

        try (FileWriter fileWriter = new FileWriter(filename)) {
            fileWriter.write(password);
        }
    }
}
