package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No15727 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int minute = Integer.parseInt(br.readLine());

        int per = minute / 5;

        if (5 * per != minute) {
            System.out.println(per + 1);
        } else {
            System.out.println(per);
        }
    }
}
