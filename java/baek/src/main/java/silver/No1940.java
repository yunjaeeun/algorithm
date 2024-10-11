package silver;

import java.awt.*;
import java.util.Scanner;

public class No1940 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        sc.nextLine();
        int M = sc.nextInt();
        sc.nextLine();
        int[] arr = new int[N];

        for (int i = 0; i < N; i++) {
            arr[i] = sc.nextInt();
        }

        int result = 0;
        for (int i = 0; i < N; i++) {
            int cnt = arr[i];
            for (int j = i; j < N; j++) {
                if(cnt + arr[j] == M && arr[j] != 0) {
                    arr[j] = 0;
                    result++;
                    break;
                }
            }
        }
        System.out.println(result);
    }
}
