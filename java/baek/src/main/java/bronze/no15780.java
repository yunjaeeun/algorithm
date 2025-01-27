package bronze;

import java.util.Scanner;

public class no15780 {
    public static void main(String[] args)  {

        Scanner scan = new Scanner(System.in);
        int Student = scan.nextInt();
        int MutiN = scan.nextInt();
        //멀티탭수

        int [] arr= new int [MutiN];

        int sum = 0;
        //사용 가능 멀티탭 구멍 갯수 샐 변수
        for(int i = 0; i < arr.length; i++) {
            arr[i] = scan.nextInt();
            if(arr[i] % 2 == 0) {
                sum += arr[i] / 2;
            }else {
                sum += (arr[i] / 2)  + 1;
            }
        }
        //한칸씩 뛰어주어야 하기 때문에
        //짝수의 구멍이면 (n / 2) 개가 사용가능하며,
        //홀수의 구멍이면 (n / 2) + 1 개가 사용가능하다.


        if(sum >= Student) {
            System.out.println("Yes");
        }else {
            System.out.println("No");
        }
    }
}
