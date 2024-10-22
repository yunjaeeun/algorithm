package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Queue;

public class no16173 {
    static int N;
    static int[][] arr;
    static int[][] visited;

    static int[] dr = {1, 0};
    static int[] dc = {0, 1};

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        N = n;
        arr = new int[n][n];
        visited = new int[n][n];
        for (int i = 0; i < n; i++) {
            String[] s = br.readLine().split(" ");
            for (int j = 0; j < n; j++) {
                arr[i][j] = Integer.parseInt(s[j]);
            }
        }

        String result = find_root(0, 0, arr[0][0]);

        System.out.println(result);

    }

    private static String find_root(int r, int c, int cnt) {    // cnt = 가야 할 칸수
        if (r == N - 1 && c == N - 1) {     // 도착했다면
            return "HaruHaru";
        }

        for (int i = 0; i < 2; i++) {
            int nr = r + dr[i] * cnt;   //  cnt 만큼 곱해 다음 도착지로 인덱스 설정
            int nc = c + dc[i] * cnt;

            if (isValid(nr, nc) && visited[nr][nc] == 0) {  // 범위를 벗어나지 않고 방문하지 않았다면
                if (i == 0) {
                    for (int j = 1; j <= cnt; j++) {    // 왔던 길에 전부 방문 등록
                        visited[r + j][c] = 1;
                    }
                } else {
                    for (int j = 1; j <= cnt; j++) {
                        visited[r][c + j] = 1;
                    }
                }
                String result = find_root(nr, nc, arr[nr][nc]);

                if (result.equals("HaruHaru")) {
                    return "HaruHaru";
                }

                if (i == 0) {
                    for (int j = 1; j <= cnt; j++) {
                        visited[r + j][c] = 0;
                    }
                } else {
                    for (int j = 1; j <= cnt; j++) {
                        visited[r][c + j] = 0;
                    }
                }

            }
        }

        return "Hing";
    }


    private static boolean isValid(int r, int c) {
        return 0 <= r && r < N && 0 <= c && c < N;
    }
}
