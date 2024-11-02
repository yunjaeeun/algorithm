package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class no10703 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        String[][] arr = new String[N][M];

        int firstR = 0;
        for (int i = 0; i < N; i++) {
            String[] input = br.readLine().split("");
            for (int j = 0; j < M; j++) {
                arr[i][j] = input[j];

                if (input[j].equals("#") && firstR == 0) {
                       firstR = j;
                }
            }
        }

        solution(firstR - 1, arr, M);

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }

    public static void solution(int start, String[][] arr, int M) {
        System.out.println(M);
        int currentR = start;
        boolean isCan = false;
        while (true) {
            for (int i = currentR; i >= 0; i--) {
                for (int j = 0; j < M; j++) {
                    if (arr[i][j].equals("X")) {
                        if (arr[i + 1][j].equals("#")) {
                            isCan = true;
                            break;
                        }
                        arr[i + 1][j] = "X";
                        arr[i][j] = ".";
                    }
                }
                if (isCan) {
                    break;
                }
            }
            currentR++;
            if (isCan) {
                break;
            }
        }
    }
}
