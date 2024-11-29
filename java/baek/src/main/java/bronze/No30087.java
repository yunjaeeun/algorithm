package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class No30087 {
    public static void main(String[] args) throws IOException {
        BufferedReader br  = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        for (int i = 0; i < n; i++) {
            String input = br.readLine();
            if (input.equals("Algorithm")) {
                System.out.println(204);
            } else if (input.equals("DataAnalysis")) {
                System.out.println(207);
            } else if (input.equals("ArtificialIntelligence")) {
                System.out.println(302);
            } else if (input.equals("CyberSecurity")) {
                System.out.println("B101");
            } else if (input.equals("Network")) {
                System.out.println(303);
            } else if (input.equals("Startup")) {
                System.out.println(501);
            } else {
                System.out.println(105);
            }
        }
    }
}
