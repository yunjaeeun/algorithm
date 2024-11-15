package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no21964 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());
        String input = br.readLine();

        String result = "";
        int n = 11;
        for (int i = N - 5; i < N; i++) {
            result += String.valueOf(input.charAt(i));
        }

        System.out.println(result);
    }
}
