package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No27389 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        float num1 = 4.0F;
        float num2 = Float.parseFloat(br.readLine());
        System.out.println(num2/num1);
    }
}
