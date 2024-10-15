package silver;

import java.util.Scanner;

public class No1913 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        int M = sc.nextInt();
        int[][] arr = new int[N][N];
        /* 델타 생성 */
        int[] dr = {1, 0, -1, 0};
        int[] dc = {0, 1, 0, -1};
        int r = 0;
        int c = 0;
        arr[r][c] = N * N;
        char direction = 'D';      // 진행방향을 저장할 변수
        String mIdx = "";

        while (arr[r][c] != 1) {
            /* 아래 -> 오른쪽 -> 위 -> 왼쪽으로 밖에서부터 배열을 채움 */
            if (direction == 'D') {
                while (true) {
                    int nr = r + dr[0];
                    int nc = c + dc[0];
                    /* 배열을 벗어나지 않고 다음 칸을 채우지 않았으면 이동 후 채움 */
                    if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] - 1;
                        r = nr;
                        c = nc;
                    } else {
                        direction = 'R';
                        break;
                    }
                }
            } else if (direction == 'R') {
                while (true) {
                    int nr = r + dr[1];
                    int nc = c + dc[1];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] - 1;
                        r = nr;
                        c = nc;
                    } else {
                        direction = 'U';
                        break;
                    }
                }
            } else if (direction == 'U') {
                while (true) {
                    int nr = r + dr[2];
                    int nc = c + dc[2];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] - 1;
                        r = nr;
                        c = nc;
                    } else {
                        direction = 'L';
                        break;
                    }
                }
            } else if (direction == 'L') {
                while (true) {
                    int nr = r + dr[3];
                    int nc = c + dc[3];
                    if (0 <= nr && nr < N && 0 <= nc && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] - 1;
                        r = nr;
                        c = nc;
                    } else {
                        direction = 'D';
                        break;
                    }
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(arr[i][j] + " ");
                if (arr[i][j] == M) {
                    mIdx = (i + 1) + " " + (j + 1);
                }
            }
            System.out.println();
        }

        System.out.println(mIdx);
    }
}
