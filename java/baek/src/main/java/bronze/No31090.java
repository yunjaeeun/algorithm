package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No31090 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int T = Integer.parseInt(br.readLine());

        for (int i = 0; i < T; i++) {
            String input = br.readLine();
            int num = Integer.parseInt(input.substring(2,4));
            int nextYear = Integer.parseInt(input) + 1;

            if (nextYear % num == 0) {
                System.out.println("Good");
            } else {
                System.out.println("Bye");
            }
        }
    }
}
