package gold;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no2239 {
    static int[][] sdoku = new int[9][9];
    static boolean[][] change = new boolean[9][9];
    static int[] dr = {1, -1, 0, 0};
    static int[] dc = {0, 0, 1, -1};

    public static void main(String[] args) throws IOException {
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//
//        for (int i = 0; i < 9; i++) {
//            String input = br.readLine();
//            for (int j = 0; j < 9; j++) {
//                sdoku[i][j] = input.charAt(j) - 48;
//                if (input.charAt(j) - 48 == 0) {
//                    change[i][j] = true;
//                }
//            }
//        }
//
//        makeSdoku();
//
//        for (int i = 0; i < 9; i++) {
//            for (int j = 0; j < 9; j++) {
//                System.out.print(sdoku[i][j]);
//            }
//            System.out.println();
//        }
        System.out.println(7/3);
    }

    /*
     *  1. 열 체크
     *  2. 행 체크
     *  3. 박스 체크
     */
    public static int makeSdoku() {
        return 0;
    }
}
