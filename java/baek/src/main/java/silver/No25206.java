package silver;

import java.util.Scanner;

public class No25206 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        double result = 0;
        double total = 0;   // 총 과목 평점
        for (int i = 0; i < 20; i++) {
            String[] arr = sc.nextLine().split(" ");        // 띄어쓰기를 구분자로 배열에 저장
            double score = Double.parseDouble(arr[1]);            // double형으로 형변환해서 변수에 저장
            String grade = arr[2];

            /* P등급의 경우 계산에서 제외 */
            if(grade.equals("P")){
                continue;
            }

            total += score;     // 총 과목 평점 추가
            /* 등급별로 학점 추가 */
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
