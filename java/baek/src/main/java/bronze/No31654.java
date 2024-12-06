package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No31654 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");

        if (Integer.parseInt(input[0]) + Integer.parseInt(input[1]) == Integer.parseInt(input[2])) {
            System.out.println("correct!");
        } else {
            System.out.println("wrong!");
        }
    }
}
