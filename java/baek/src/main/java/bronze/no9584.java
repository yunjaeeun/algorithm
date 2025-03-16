package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class no9584 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String code = br.readLine();

        int num = Integer.parseInt(br.readLine());

        List<String> arr = new ArrayList<>();

        for (int i = 0; i < num; i++) {
            String input = br.readLine();
            boolean isTrue = true;
            for (int j = 0; j < code.length(); j++) {
                if (code.charAt(j) != input.charAt(i) && code.charAt(i) != '*') {
                    isTrue = false;
                    break;
                }
            }

            if (isTrue) {
                arr.add(input);
            }
        }

        System.out.println(arr.size());
        for (String string : arr) {
            System.out.println(string);
        }
    }
}
