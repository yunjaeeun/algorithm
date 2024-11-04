package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no1268 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[] cnt = new int[N];
        int[][] board = new int[N][5];

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < 5; j++) {
                int idx = Integer.parseInt(s[j]);
                board[i][j] = idx;
            }
        }

        // 1. 세로 탐색(범위 한칸씩 줄여가며)
        // 2. 오른쪽으로 한칸씩 가며 탐색
        for (int k = 0; k < 5; k++) {
            for (int i = 0; i < N; i++) {
                int cls = board[i][k];
                for (int j = i + 1; j < N; j++) {
                    if (cls == board[j][k]) {
                        cnt[i]++;
                        cnt[j]++;
                    }
                }
            }
        }

        int max_cnt = 0;
        int result = 0;
        // 3. 마지막 최종 카운트 집계
        for (int i = N - 1; i >= 0; i--) {
//            System.out.print(cnt[i] + ", ");
            if (cnt[i] > max_cnt) {
                max_cnt = cnt[i];
                result = i + 1;
            }
        }

        System.out.println(result);
    }
}
