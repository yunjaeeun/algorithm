package silver;

import java.util.Scanner;

public class No2579 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] stairs = new int[301];    // 계단의 갯수는 최대 300개 인덱스를 일치기키기 위해 300 + 1만큼 선언
        int N = sc.nextInt();
        for (int i = 1; i <= N; i++) {  // 계단 입력 받기
            sc.nextLine();
            stairs[i] = sc.nextInt();
        }
        int[] dp = new int[301];
        /* DP 풀이
         * 현재 계단에서 올 수 있는 경우의 수
         * 1. 한칸 전
         *  1-1. 한칸 전의 경우 두칸 전을 밟을 수 없으므로 n - 3, n - 1, n
         * 2. 두칸 전
         *  2-2 두칸 전의 경우 이 전의 선택지는 상관 없음 n - 2, n
         *
         * 결국 최선의 방법을 택하며 올라온 값을 배열에 저장 후 두가지 경우의 수 중 최선을 택한다.
         */

        /* 1 ~ 3층 초기화 */
        dp[1] = stairs[1];
        dp[2] = stairs[1] + stairs[2];
        dp[3] = Math.max(stairs[3] + stairs[1], stairs[2] + stairs[3]);

        /* 4층부터 시작 */
        for (int i = 4; i <= N; i++) {
                    /* 한칸 전에서 온 경우 = 현재 위치 + 한칸 전 + 세칸 전의 최선의 선택지 */
            dp[i] = Math.max(stairs[i] + dp[i - 3] + stairs[i - 1],

                    /* 두칸 전에서 온 경우 = 현재 위치 + 두칸 전의 최선의 선택지*/
                    dp[i - 2] + stairs[i]);
        }

        System.out.println(dp[N]);
    }
}
