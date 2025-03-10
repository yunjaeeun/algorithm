package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no28453 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int num = Integer.parseInt(br.readLine());
        String[] arr = br.readLine().split(" ");

        for (int i = 0; i < num; i++) {
            int level = Integer.parseInt(arr[i]);

            if (level < 250) {
                System.out.print(4 + " ");
            } else if (level < 275) {
                System.out.print(3 + " ");
            } else if (level < 300) {
                System.out.print(2 + " ");
            } else {
                System.out.print(1 + " ");
            }
        }
    }
}
