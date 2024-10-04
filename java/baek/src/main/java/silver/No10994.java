package silver;

import java.util.Scanner;

public class No10994 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int size = 1 + (N - 1) * 4;     // 별찍기의 총 크기
        if (size == 0) {
            System.out.println("*");
        } else {
            char[][] arr = new char[size][size];      // 별을 저장할 배열 선언

            arr[size / 2][size / 2] = '*';            // 중간에 별 하나 먼저 채우기

            /* 테두리부터 채우기 위해 상하좌우 변수 선언 */
            int top = 0;
            int bottom = size - 1;
            int left = 0;
            int right = size - 1;

            /* 채울 별의 갯수 */
            int star = size;

            /* 가운데 기준으로 테두리를 N - 1번 채우면 되기 때문에 N - 1번 반복 */
            for (int i = 1; i < N; i++) {

                /* 별찍기 시작 */
                for (int j = 0; j < star; j++) {
                    arr[top][left +j] = '*';        // 위쪽 채우기
                    arr[bottom][left + j] = '*';    // 아래쪽 채우기
                    arr[top + j][left] = '*';       // 왼쪽 채우기
                    arr[top + j][right] = '*';      // 오른쪽 채우기
                }

                star -= 4;      // 가운데로 갈수록 찍어야 하는 별의 갯수가 4개씩 준다.
                left += 2;      // 다음 테두리까지 1칸의 빈칸이 존재하므로 1칸씩 건너뛰기
                right -= 2;
                top += 2;
                bottom -= 2;
            }

            for (int i = 0; i < size; i++) {
                for (int j = 0; j < size; j++) {
                    /* 별을 찍지 않은 곳에 빈 문자열 추가 */
                    if(arr[i][j] != '*'){
                        arr[i][j] = ' ';
                    }
                    System.out.print(arr[i][j]);
                }
                System.out.println();
            }
        }
    }
}
