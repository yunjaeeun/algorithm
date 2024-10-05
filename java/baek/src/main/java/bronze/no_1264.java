package bronze;

import java.util.Scanner;

public class no_1264 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        char[] arr = {'a', 'e', 'i', 'o', 'u'};

        while (true) {
            String input = sc.nextLine();
            if(input.equals("#")) {
                break;
            }
            String a = input.toLowerCase();
            int result = 0;
            for (int i = 0; i < a.length(); i++) {
                for (int j = 0; j < 5; j++) {
                    if (a.charAt(i) == arr[j]) {
                        result++;
                    }
                }
            }
            System.out.println(result);
        }
    }
}
