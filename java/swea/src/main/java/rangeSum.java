import java.util.Scanner;

public class rangeSum {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();
        for (int tc = 1; tc <= T; tc++) {

            int N = sc.nextInt();
            int M = sc.nextInt();
            int[] arr = new int[N];
            for (int i = 0; i < N; i++) {
                arr[i] = sc.nextInt();
            }
            int min_sum = 100000000;
            int max_sum = 0;

            for (int i = 0; i <= N - M; i++) {
                int sum = 0;
                for (int j = 0; j < M; j++) {
                    sum += arr[i + j];
                }
                if (sum < min_sum) {
                    min_sum = sum;
                }
                if (sum > max_sum) {
                    max_sum = sum;
                }
            }
            System.out.println("#" + tc + " " + (max_sum - min_sum));


        }

    }
}
