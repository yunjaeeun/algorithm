package bronze;

import java.util.Scanner;

public class No2490 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 3; i++) {
            int cnt = 0;
            for (int j = 0; j < 4; j++) {
                int dice = sc.nextInt();
                /* 배의 갯수를 카운팅 */
                if (dice == 0) {
                    cnt++;
                }
            }
            switch (cnt) {
                case 0:    // 모
                    System.out.println("E");
                    break;      // break로 switch를 탈출하지 않으면 아래 case문도 실행된다.
                case 1:   // 도
                    System.out.println("A");
                    break;
                case 2:    // 개
                    System.out.println("B");
                    break;
                case 3:    // 걸
                    System.out.println("C");
                    break;
                case 4:    // 윷
                    System.out.println("D");
                    break;
            }
        }
    }
}
