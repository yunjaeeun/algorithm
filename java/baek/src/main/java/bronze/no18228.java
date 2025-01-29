package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no18228 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int input = Integer.parseInt(br.readLine());
        int[] arr = new int[input];
        String[] sArr = br.readLine().split(" ");
        for (int i = 0; i < input; i++) {
            arr[i] = Integer.parseInt(sArr[i]);
        }

        int lMin = 200000000;
        int rMin = 200000000;
        boolean isPen = false;
        for (int i = 0; i < input; i++) {
            if (!isPen && lMin > arr[i] && arr[i] != -1) {
                lMin = arr[i];
            } else if (arr[i] == -1) {
                isPen = true;
            } else if (isPen && rMin > arr[i] && arr[i] != -1) {
                rMin = arr[i];
            }
        }

        System.out.println(rMin + lMin);
    }
}
