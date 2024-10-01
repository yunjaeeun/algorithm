package bronze;

import java.util.ArrayList;
import java.util.Scanner;

public class No1977 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int M = sc.nextInt();   // 최소값
        int N = sc.nextInt();   // 최대값
        ArrayList<Integer> list = new ArrayList<>();
        for (int i = 1; i <= 100; i++) {    // M, N 은 10000이하의 자연수이므로 수의 범위는 100까지
            if (M <= i * i && i * i <= N) { // 최대, 최소를 넘지 않는다면
                list.add(i * i);        // 리스트에 추가
            } else if (i * i > M) {     // 최댓값을 넘는다면 반복문 탈출
                break;
            }
        }
        int result = 0;
        for (int i = 0; i < list.size(); i++) {     // 배열의 크기만큼 순회하며 요소들 더하기
            result += list.get(i);
        }
        if (result == 0) {          // result가 0이면 배열의 길이가 0이므로 제곱수가 존재하지 않음
            System.out.println(-1);
        } else {
            System.out.println(result);
            System.out.println(list.get(0));
        }
    }
}
