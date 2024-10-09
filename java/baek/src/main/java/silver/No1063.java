package silver;

import java.util.Scanner;

public class No1063 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String king = sc.next();
        String stone = sc.next();
        int cnt = sc.nextInt();
        sc.nextLine();
        char[][] board = new char[8][8];

        /* 자바는 char형을 정수형으로 인식한다(아스키코드 기준)
         * A ~ H = 65 ~ 72
         * 1 ~ 8 = 49 ~ 55
         */

        /* i열은 인덱스 범위를 반대로 생각해야 하기 때문에 -7을 해주고 절대값을 씌워 인덱스 범위를 일치시키기 */
        int[] kingsIdx = new int[]{Math.abs(king.charAt(1) - 49 - 7), Math.abs(king.charAt(0) - 65)};
        int[] stonesIdx = new int[]{Math.abs(stone.charAt(1) - 49 - 7), Math.abs(stone.charAt(0) - 65)};

        board[kingsIdx[0]][kingsIdx[1]] = 'K';
        board[stonesIdx[0]][stonesIdx[1]] = 'S';


        for (int i = 0; i < cnt; i++) {     // 문제에서 주어진 횟수만큼 이동
            int[] direct = find_direct(sc.nextLine());      // 가야 할 방향의 인덱스를 일치시키는 함수 호출
            /* 이동해야 할 인덱스 */
            int kingI = kingsIdx[0] + direct[0];
            int kingJ = kingsIdx[1] + direct[1];
            int stoneI = stonesIdx[0] + direct[0];
            int stoneJ = stonesIdx[1] + direct[1];


            if (0 <= kingI && kingI < 8 && 0 <= kingJ && kingJ < 8) {      // 킹이 이동 가능한 상태이면
                if (board[kingI][kingJ] != 'S') {   // 갈 곳에 돌이 없다면
                    board[kingsIdx[0]][kingsIdx[1]] = ' ';  // 왔던 자리 빈칸으로 초기화
                    board[kingI][kingJ] = 'K';  // 킹 이동
                    kingsIdx[0] = kingI;        // 현재 킹의 위치 저장
                    kingsIdx[1] = kingJ;
                } else if (board[kingI][kingJ] == 'S') {    // 갈 곳에 돌이 있다면
                    if (0 <= stoneI && stoneI < 8 && 0 <= stoneJ && stoneJ < 8) {    // 돌이 이동 가능한지 체크
                        board[stoneI][stoneJ] = 'S';    // 돌 이동
                        stonesIdx[0] = stoneI;      // 현재 돌의 위치 저장
                        stonesIdx[1] = stoneJ;
                        board[kingI][kingJ] = 'K';      // 킹 이동
                        board[kingsIdx[0]][kingsIdx[1]] = ' ';  // 왔던 자리 초기화
                        kingsIdx[0] = kingI;        // 현재 킹의 위치 저장
                        kingsIdx[1] = kingJ;
                    }
                }
            }

        }
        String lastKing = "";
        String lastStone = "";

        /* 마지막으로 위치한 킹과 돌의 위치를 찾아 변수에 저장 */
        for (int i = 0; i < 8; i++) {
            for (int j = 0; j < 8; j++) {
                if (board[i][j] == 'K') {
                    lastKing += (char) (65 + j);
                    lastKing += Math.abs(i - 8);
                } else if (board[i][j] == 'S') {
                    lastStone += (char) (65 + j);
                    lastStone += Math.abs(i - 8);
                }
            }
        }


        System.out.println(lastKing);
        System.out.println(lastStone);
    }

    /* 입력값별로 가야할 방향을 배열로 반환하는 함수 */
    public static int[] find_direct(String move) {
        int[] direct = new int[2];
        switch (move) {
            case "R":
                direct[1] = 1;
                break;
            case "L":
                direct[1] = -1;
                break;
            case "B":
                direct[0] = 1;
                break;
            case "T":
                direct[0] = -1;
                break;
            case "RT":
                direct[0] = -1;
                direct[1] = 1;
                break;
            case "LT":
                direct[0] = -1;
                direct[1] = -1;
                break;
            case "RB":
                direct[0] = 1;
                direct[1] = 1;
                break;
            case "LB":
                direct[0] = 1;
                direct[1] = -1;
                break;

        }
        return direct;
    }
}
