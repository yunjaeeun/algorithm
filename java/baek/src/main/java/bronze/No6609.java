package bronze;

import java.util.Scanner;

public class No6609 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (sc.hasNext()) {      // 입력이 끝날 때 까지 받음
            int mosquito = sc.nextInt();       // 첫째주 모기
            int pupa = sc.nextInt();       // 번데기
            int larva = sc.nextInt();       // 유충
            int E = sc.nextInt();       // 한 모기가 낳는 알의 수
            int R = sc.nextInt();       // 살아남는 유충의 비율
            int S = sc.nextInt();       // 살아남는 번데기의 비율
            int N = sc.nextInt();       // 주
            int egg = 0;
            for (int i = 0; i < N; i++) {       // N주만큼반복
                egg = mosquito * E;     // 알의 갯수 구하기
                /* 새로 생긴 알, 번데기, 유충이 포함되서 계산 되지 않게 순서 설정 */
                mosquito = pupa / S;
                pupa = larva / R;
                larva = egg;
            }
            System.out.println(mosquito);
        }
    }
}
