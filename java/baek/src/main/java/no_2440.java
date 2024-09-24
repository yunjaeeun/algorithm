import java.util.Scanner;

public class no_2440 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for (int i = num; i > 0; i--) {
            String a = "";
            for (int j = 0; j < i; j++) {
                a += "*";
            }
            System.out.println(a);
        }
    }
}
