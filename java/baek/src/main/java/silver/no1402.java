package silver;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class no1402 {
    public static void main (String[] args) throws java.lang.Exception
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int cnt = Integer.parseInt(br.readLine());
        for(int i = 0; i < cnt; i++){
            StringTokenizer st = new StringTokenizer(br.readLine());
            System.out.println("yes");
        }

    }
}
