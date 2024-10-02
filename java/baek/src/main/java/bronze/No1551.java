package bronze;

import java.util.Scanner;

public class No1551 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();       // N = 배열의 길이
        int K = sc.nextInt();       // K = 반복할 횟수
        sc.nextLine();              // 중간 엔터 버리기
        String[] str = sc.nextLine().split(",");    // str.split(",") = ,를 기준으로 문자열을 쪼개 배열에 담음
        int[] arr = new int[N];

        /* 문자열을 숫자로 형변환 해서 배열에 담아줌 */
        for (int i = 0; i < N; i++) {
            arr[i] = Integer.parseInt(str[i]);          // Integer.parseInt(str) = 문자열을 숫자로 형변환
        }

        for (int i = 0; i < K; i++) {                   // 반복 횟수
            for (int j = 0; j < N - 1; j++) {
                int first = arr[j];                     // 처음 숫자
                int second = arr[j + 1];                // 두번째 숫자
                arr[j] = second - first;                // 배열 값 변경
            }
        }
        for (int i = 0; i < N - K; i++) {               // 반복 횟수만큼 배열의 길이가 줄기 때문에 N - K번 반복
            if (i == (N - K - 1)) {                     // 마지막에는 , 를 추가하지 않음.
                System.out.println(arr[i]);
            } else {
                System.out.print(arr[i] + ",");

            }
        }
    }
}
