package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no2167 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] input = br.readLine().split(" ");

        int N = Integer.parseInt(input[0]);
        int M = Integer.parseInt(input[1]);

        int[][] arr = new int[N][M];
        for (int i = 0; i < N; i++) {
            String[] nums = br.readLine().split(" ");
            for (int j = 0; j < M; j++) {
                arr[i][j] = Integer.parseInt(nums[j]);
            }
        }

        int K = Integer.parseInt(br.readLine());
        for (int i = 0; i < K; i++) {
            String[] range = br.readLine().split(" ");
            int ci = Integer.parseInt(range[0]) - 1;
            int cj = Integer.parseInt(range[1]) - 1;
            int ei = Integer.parseInt(range[2]) - 1;
            int ej = Integer.parseInt(range[3]) - 1;
            int result = 0;
            if (ei == ci && ej == cj) {
                result = arr[ci][ej];
            } else {
                while (true) {
                    if (cj == M) {
                        ci++;
                        cj = 0;
                    }
                    result += arr[ci][cj];
                    cj++;

                    if (ci == ei && cj == ej) {
                        result += arr[ci][cj];
                        break;
                    }
                }
            }
            System.out.println(result);
        }

    }
}
