package bronze;

import java.util.Scanner;

public class No1236 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        char[][] arr = new char[N][M];
        sc.nextLine();

        for (int i = 0; i < N; i++) {
            String dum = sc.nextLine();
            for (int j = 0; j < M; j++) {
                arr[i][j] = dum.charAt(j);
            }
        }
        int rCnt = 0;
        int cCnt = 0;

        for (int i = 0; i < N; i++) {
            boolean rIsCan = true;
            for (int j = 0; j < M; j++) {
                if (arr[i][j] == 'X') {
                    rIsCan = false;
                }
            }
            if (rIsCan) {
                rCnt++;
            }
        }

        for (int i = 0; i < M; i++) {
            boolean cIsCan = true;
            for (int j = 0; j < N; j++) {
                if (arr[j][i] == 'X') {
                    cIsCan = false;
                }
            }
            if (cIsCan) {
                cCnt++;
            }
        }
        rCnt = rCnt;
        cCnt = cCnt;
        int result = Math.max(rCnt, cCnt);
        System.out.println(result);

    }
}
