package bronze;

import java.util.Scanner;

public class No2775 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();       // 테스트케이스의 수
        sc.nextLine();      // 개행처리
        for (int i = 0; i < T; i++) {
            int K = sc.nextInt();   // 층수
            sc.nextLine();
            int N = sc.nextInt();   // 호의 갯수
            sc.nextLine();
            int[][] arr = new int[K + 1][N];    // 0층부터 존재하므로 1층을 더 만들어준다.
            for (int j = 0; j < N; j++) {       // 0층의 사람 세팅
                arr[0][j] = j + 1;
            }
            for (int j = 1; j < K + 1; j++) {   // 1층부터 배열 순회
                for (int k = 0; k < N; k++) {   // 전체 동 순회
                    int sum = 0;
                    for (int l = 0; l <= k; l++) {  // 자신의 아래층의 사람 더하기
                        sum += arr[j -1][l];
                    }
                    arr[j][k] = sum;
                }
            }
            System.out.println(arr[K][N - 1]);
        }
    }
}
