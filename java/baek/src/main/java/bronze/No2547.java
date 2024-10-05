package bronze;

import java.math.BigInteger;
import java.util.Scanner;

public class No2547 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();       // 테스트 케이스의 수
        for (int i = 0; i < T; i++) {
            sc.nextLine();      // 테스트 케이스 구분
            int N = sc.nextInt();
            sc.nextLine();      // nextInt()는 개행처리를 하지 않으므로 띄어쓰기처리
            BigInteger student = new BigInteger(N + "");    // 학생 수
            BigInteger result = new BigInteger("0");        // 사탕의 총 갯수
            for (int j = 0; j < N; j++) {
                BigInteger candy = new BigInteger(sc.nextLine());
                result = result.add(candy);     // Biginteger.add(num) = Biginteger + num
            }

            /* compareTo(num) -> 비교 메서드 num 보다 크면 1 같으면 0 작으면 -1 반환 */
            /* remainder -> BigInteger의 % 연산자 */
            if (result.remainder(student).compareTo(BigInteger.ZERO) == 0) {
                System.out.println("YES");
            } else {
                System.out.println("NO");
            }
        }
    }
}
