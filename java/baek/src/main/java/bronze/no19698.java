package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no19698 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] arr = br.readLine().split(" ");
        int bread = Integer.parseInt(arr[0]) / 2;
        int meat = Integer.parseInt(arr[1]);
        if (bread > meat) {
            System.out.println(meat);
        } else {
            System.out.println(bread);
        }
    }
}
