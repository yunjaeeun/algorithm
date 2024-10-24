package silver;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no1620 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String[] nAndM = br.readLine().split(" ");
        int N = Integer.parseInt(nAndM[0]);
        int M = Integer.parseInt(nAndM[1]);

        String[] arr = new String[N + 1];
        for (int i = 0; i < N; i++) {
            arr[i + 1] = br.readLine();
        }

        for (int i = 0; i < M; i++) {
            String find = br.readLine();
            if (48 <= find.charAt(0) && find.charAt(0) <= 57) {
                System.out.println(arr[Integer.parseInt(find)]);
            } else {
                for (int j = 1; j < N + 1; j++) {
                    if (arr[j].equals(find)) {
                        System.out.println(j);
                        break;
                    }
                }
            }
        }
    }
}
