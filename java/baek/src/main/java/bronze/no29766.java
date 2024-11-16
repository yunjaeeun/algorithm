package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no29766 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String input = br.readLine();
        int len = input.length();
        int result = 0;

        for (int i = 0; i < len - 3; i++) {
            if (input.charAt(i) == 'D' && input.charAt(i + 1) == 'K' &&
                    input.charAt(i + 2) == 'S' && input.charAt(i + 3) == 'H' ) {
                result++;
            }
        }

        System.out.println(result);
    }
}
