package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no31561 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int input = Integer.parseInt(br.readLine());

        double result = 0;
        result = (input <= 30.0 ? input/2.0 : input * 3.0/2.0 - 30.0);

        System.out.printf("%.1f", result);
    }
}
