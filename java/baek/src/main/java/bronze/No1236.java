package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class No1236 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken()); // 성의 세로 크기
        int m = Integer.parseInt(st.nextToken()); // 성의 가로 크기
        int colSecurity = n; // 층 수 만큼 경비원 수 초기화
        char flag = ' '; // 층별 X가 나오면 한번 저장하고 다시 저장 안 되도록 하기 위한 것
        int[] rowStatus = new int[m]; // 열에 추가할 경비원 수 저장

        Arrays.fill(rowStatus, 1); // rowStatus 1(경비가 배치된)로 초기화

        for (int i = 0; i < n; i++) { // 세로 만큼 반복
            String castle = br.readLine(); // 성 상태 입력
            char[] colStatus = castle.toCharArray(); // 성 상태 char[]로 변환

            for (int j = 0; j < m; j++) { // 가로 만큼 반복
                // 열에 추가할 경비원 수 계산 코드
                if (colStatus[j] == 'X') { // 해당 열에 경비원이 있으면 그 열은 추가할 경비원 없음
                    rowStatus[j] = 0;
                }
                // 행에 추가할 경비원 수 계산 코드
                if (flag == (char)i) { // 이미 X가 나왔을 시, colSecurity 감소 없이 진행
                    continue;
                } else if (colStatus[j] == 'X') { // X(경비원)이 있을 시, 추가할 경비원 수 감소
                    colSecurity--;
                    flag = (char) i;
                }
            } // 가로 반복 끝
        } // 세로 반복 끝

        int rowSecurity = 0; // 열 기준으로 배치할 경비원 수 저장 공간
        for (int i=0; i<m; i++) { // 배열 길이만큼 반복해서 배치할 경비원 수 더함
            rowSecurity += rowStatus[i];
        }

        System.out.println(Math.max(colSecurity, rowSecurity)); // 추가할 경비원의 최솟값 출력
    }
}
