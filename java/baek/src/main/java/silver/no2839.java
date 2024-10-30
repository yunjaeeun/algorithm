package silver;

import java.util.Scanner;

public class no2839 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();

        int[] arr = new int[5001];

        arr[3] = 1;
        arr[5] = 1;

        for (int i = 6; i <= N ; i++) {
            if (i % 5 == 0) {
                arr[i] = arr[i - 5] + 1;
            } else if (i % 3 == 0) {
                arr[i] = arr[i - 3] + 1;
            } else {
                if (arr[i - 3] != 0 && arr[i - 5] != 0) {
                    arr[i] = Math.min(arr[i - 3], arr[i - 5]) + 1;
                }
            }
        }

        if (arr[N] == 0) {
            System.out.println(-1);
        } else {
            System.out.println(arr[N]);
        }

//        int result = solution(N);
//        System.out.println(result);
    }

    public static int solution(int n) {
        int count = 0;              // 들고 갈 최소 봉지 갯수

        while (true) {

            /* 설명. 5킬로그램 봉지로 바로 나눌 수 있으면 n/5를 반환 */
            if (n % 5 == 0) {
                return (n / 5) + count;        // (+ count)의 개념은 이전 반복에서 가져간 3킬로그램 봉지의 수이다.
            } else if (n < 3) {
                return -1;
            }

            /* 설명. 3킬로그램 봉지로 한 봉지 들고 간다. */
            n = n - 3;
            count++;
        }
    }
}
