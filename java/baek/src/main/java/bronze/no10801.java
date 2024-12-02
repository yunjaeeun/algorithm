package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no10801 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] aArr = br.readLine().split(" ");
        String[] bArr = br.readLine().split(" ");

        int aCtn = 0;
        int bCtn = 0;

        for (int i = 0; i < 10; i++) {
            if (Integer.parseInt(aArr[i]) > Integer.parseInt(bArr[i])) {
                aCtn++;
            } else if (Integer.parseInt(aArr[i]) < Integer.parseInt(bArr[i])) {
                bCtn++;
            }
        }

        if (aCtn > bCtn) {
            System.out.println("A");
        } else if (aCtn < bCtn) {
            System.out.println("B");
        } else {
            System.out.println("D");
        }
    }
}
