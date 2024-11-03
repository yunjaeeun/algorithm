package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class no1235 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        String[] arr = new String[N];
        for (int i = 0; i < N; i++) {
            arr[i] = br.readLine();
        }

        int passLen = arr[0].length();

        int result = 1;
        ArrayList<Integer> valid = new ArrayList<>();
        while (true) {
            for (int i = 0; i < N; i++) {
                int num = Integer.parseInt(arr[i].substring(passLen - result, passLen));
                if(!valid.contains(num)) {
                    valid.add(num);
                }
            }

            if (valid.size() == N) {
                break;
            }
            valid.clear();
            result++;
        }

        System.out.println(result);
    }
}
