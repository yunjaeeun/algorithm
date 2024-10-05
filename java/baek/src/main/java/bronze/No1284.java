package bronze;

import java.util.Scanner;

public class No1284 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            String a = sc.nextLine();
            if(a.equals("0")){
                break;
            }

            int aLen = a.length();

            int zero = 0;
            int one = 0;
            int other = 0;
            for (int i = 0; i < aLen; i++) {
                if (a.charAt(i) == '1') {
                    one++;
                } else if (a.charAt(i) == '0') {
                    zero++;
                } else {
                    other++;
                }
            }
            int result = (zero * 4) + (one * 2) + (other * 3) + (aLen + 1);
            System.out.println(result);
        }

    }
}
