package silver;

import java.util.Scanner;

public class No25206 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double result = 0;
        double total = 0;
        for (int i = 0; i < 20; i++) {
            String[] arr = sc.nextLine().split(" ");
            double score = Double.parseDouble(arr[1]);
            String grade = arr[2];

            if(grade.equals("P")){
                continue;
            }

            total += score;
            switch (grade) {
                case "A+":
                    result += 4.5 * score;
                    break;
                case "A0":
                    result += 4.0 * score;
                    break;
                case "B+":
                    result += 3.5 * score;
                    break;
                case "B0":
                    result += 3.0 * score;
                    break;
                case "C+":
                    result += 2.5 * score;
                    break;
                case "C0":
                    result += 2.0 * score;
                    break;
                case "D+":
                    result += 1.5 * score;
                    break;
                case "D0":
                    result += 1.0 * score;
                    break;
            }
        }
        System.out.println(result / total);

    }
}
