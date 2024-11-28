package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No28444 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] input = br.readLine().split(" ");
        int[] nums = new int[5];

        for (int i = 0; i < 5; i++) {
            nums[i] = Integer.parseInt(input[i]);
        }

        int num1 = nums[0] * nums[1];
        int num2 = nums[2] * nums[3] * nums[4];

        System.out.println(num1 - num2);
    }
}
