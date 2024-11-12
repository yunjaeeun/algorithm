package silver;

import java.util.Scanner;

public class no1343 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        sc.close();

        String res = "";

        res = change(s);

        System.out.println(res);
    }

    private static String change(String s) {
        String ans = "";
        String A = "AAAA";
        String B = "BB";

        s = s.replaceAll("XXXX", A);
        ans = s.replaceAll("XX", B);

        if(ans.contains("X")) {
            ans = "-1";
        }

        return ans;
    }
}
