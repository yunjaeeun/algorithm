package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No11365 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = "";
        while (!input.equals("END")) {
            input = br.readLine();

            if (!input.equals("END")) {
                int sLen = input.length();

                for (int i = sLen - 1; i >= 0; i--) {
                    System.out.print(input.charAt(i));
                }
                System.out.println();
            }
        }
    }
}
