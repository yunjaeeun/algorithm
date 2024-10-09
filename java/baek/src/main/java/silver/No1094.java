package silver;

import java.util.Scanner;

public class No1094 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int X = sc.nextInt();

        int[] arr = new int[]{64, 32, 16, 8, 4, 2, 1};      // 막대기를 반으로 잘랐을 때 나올 수 있는 경우의 수
        int result = 0;

        for (int stick : arr) {     // 전체 배열 순회

            if (X >= stick) {   // 만약 막대기의 길이가 더 작다면
                result++;       // 갯수 증가
                X -= stick;     // 만들어야 하는 길이 감소
            }
            if (X == 0) {       // 다 만들었다면 반복문 탈출
                break;
            }
        }

        System.out.println(result);
    }
}
