package silver;

import java.util.Scanner;

public class no26169 {
    static int[] dr = {1, -1, 0, 0};        // 상 하 좌 우
    static int[] dc = {0, 0, 1, -1};
    static int[][] board = new int[5][5];
    static int[][] visited = new int[5][5]; // 방문을 등록할 배열

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            String[] input = sc.nextLine().split(" ");
            for (int j = 0; j < 5; j++) {
                board[i][j] = Integer.parseInt(input[j]);
            }
        }

        int r = sc.nextInt();
        int c = sc.nextInt();

        visited[r][c] = 1;
        int result = findRoot(r, c, 0, 0);

        System.out.println(result);
    }

    private static int findRoot(int r, int c, int count, int move) {
        if (move > 3) {     // 3번 이상 이동하면
            return 0;
        } else if (count == 2) {    // 사과를 2번 먹었다면
            return 1;
        }

        for (int i = 0; i < 4; i++) {
            int nr = r + dr[i];
            int nc = c + dc[i];

            /* 인덱스 범위 체크, 방문했던곳인지 체크, 장애물이 있는지 체크 */
            if (isValid(nr, nc) && visited[nr][nc] == 0 && board[nr][nc] != -1) {
                visited[nr][nc] = 1;

                int result = 0;

                if (board[nr][nc] == 1) {       // 다음 위치가 사과라면 count 증가
                    result = findRoot(nr, nc, count + 1, move + 1);
                } else {
                    result = findRoot(nr, nc, count, move + 1);
                }
                visited[nr][nc] = 0;

                if (result == 1) {      // 값을 구했다면 성공 반환
                    return result;
                }
            }
        }

        return 0;
    }

    private static boolean isValid(int nr, int nc) {

        return nr >= 0 && nr < 5 && nc >= 0 && nc < 5;
    }


}
