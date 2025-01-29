package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no1259 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));


        while (true) {
            String input = br.readLine();
            if (input.equals("0")) break;
            StringBuilder reverse = new StringBuilder();

            for (int i = input.length() - 1; i >= 0; i--) {
                reverse.append(input.charAt(i));
            }
            String reverseInput = String.valueOf(reverse);

            if (input.equals(reverseInput)) {
                System.out.println("yes");
            } else {
                System.out.println("no");
            }
        }
    }
}
