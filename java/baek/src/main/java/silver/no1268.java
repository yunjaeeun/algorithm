package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashSet;
import java.util.Set;

public class no1268 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        int[][] board = new int[N][5];
        int max = 0;
        int result = 0;

        for (int i = 0; i < N; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(s[j]);
            }
        }

        for (int i = 0; i < N; i++) {
            Set<Integer> sameClass = new HashSet<>();

            for (int j = 0; j < 5; j++) {
                for (int k = 0; k < N; k++) {
                    if (board[i][j] == board[k][j] && k != i) {
                        sameClass.add(k);
                    }
                }
            }

            if (max < sameClass.size()) {
                max = sameClass.size();
                result = i;
            }
        }

        System.out.println(result + 1);
    }
}
