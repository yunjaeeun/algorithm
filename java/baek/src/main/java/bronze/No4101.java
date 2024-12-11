package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No4101 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        while (true) {
            String[] input = br.readLine().split(" ");

            if (input[0].equals("0") && input[1].equals("0")) {
                break;
            }

            long num1 = Long.parseLong(input[0]);
            long num2 = Long.parseLong(input[1]);

            if (num1 > num2) {
                System.out.println("Yes");
            } else {
                System.out.println("No");
            }
        }
    }
}
