package silver;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class No1158 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int K = sc.nextInt();
        int[] peoples = new int[N];
        ArrayList<Integer> result = new ArrayList<>();

        /* 초기 배열 세팅 */
        for (int i = 1; i <= N; i++) {
            peoples[i - 1] = i;
        }

        int count = 1;
        int idx = 0;
        while (result.size() != N) {    // 요세푸스가 다 완성될때까지
            if (idx == N) {         // 인덱스 범위가 벗어나면 0으로 초기화
                idx = 0;
            }
            if (peoples[idx] == 0) {    // 현재 인덱스에 0이 있다면
                for (int i = 0; i < 7; i++) {   // 가장 가까운 0이 아닌 숫자를 찾음
                    idx++;
                    if (idx == N) {
                        idx = 0;
                    }
                    if (peoples[idx] != 0) {    // 찾으면 탈출
                        break;
                    }
                }
                continue;
            }

            if (count == K) {       // K번째 사람에 도착했다면
                result.add(peoples[idx]);   // 결과에 추가
                peoples[idx] = 0;       // 빈자리로 만들기
                count = 0;              // 카운트 초기화
            }
            count++;
            idx++;
        }

        String output = "<";
        for (int i = 0; i < N; i++) {
            if (i == N - 1) {
                output += result.get(i) + ">";
            } else {
                output += result.get(i) + ", ";
            }
        }

        System.out.println(output);
    }
}
