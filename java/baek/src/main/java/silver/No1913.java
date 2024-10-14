package silver;

import java.util.Scanner;

public class No1913 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        sc.nextLine();
        int M = sc.nextInt();
        int[][] arr = new int[N][N];
        int[] dr = {-1, 0, 1, 0};
        int[] dc = {0, 1, 0, -1};
        int r = N / 2;
        int c = N / 2;
        arr[r][c] = 1;
        String direction = "U";
        String mIdx = "";
        int c_num = 0;
        while (arr[r][c] < N * N) {
            if (c_num == N * N) {
                break;
            }

            if (direction.equals("U")) {
                while (true) {
                    int nr = r + dr[0];
                    int nc = c + dc[0];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] + 1;
                        r = nr;
                        c = nc;
                        c_num = arr[r][c] + 1;
                        continue;
                    }
                    direction = "R";
                    break;
                }
            } else if (direction.equals("R")) {
                while (true) {
                    int nr = r + dr[1];
                    int nc = c + dc[1];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] + 1;
                        r = nr;
                        c = nc;
                        c_num = arr[r][c] + 1;
                        continue;
                    }
                    direction = "D";
                    break;
                }
            } else if (direction.equals("D")) {
                while (true) {
                    int nr = r + dr[2];
                    int nc = c + dc[2];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] + 1;
                        r = nr;
                        c = nc;
                        c_num = arr[r][c] + 1;
                        continue;
                    }
                    direction = "L";
                    break;
                }
            } else if (direction.equals("L")) {
                while (true) {
                    int nr = r + dr[3];
                    int nc = c + dc[3];
                    if (nr >= 0 && nr < N && nc >= 0 && nc < N && arr[nr][nc] == 0) {
                        arr[nr][nc] = arr[r][c] + 1;
                        r = nr;
                        c = nc;
                        c_num = arr[r][c] + 1;
                        continue;
                    }
                    direction = "U";
                    break;
                }
            }
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < N; j++) {
                System.out.print(arr[i][j] + " ");
            }
            System.out.println();
        }
        System.out.println(mIdx);
    }
}
