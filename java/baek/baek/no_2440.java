import java.util.Scanner;

public class no_2440 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int num = sc.nextInt();

        for (int i = 0; i < num; i++) {
            for (int j = num; j > 0 ; j--) {
                System.out.println("*");
            }
            System.out.println();
        }

    }

}
