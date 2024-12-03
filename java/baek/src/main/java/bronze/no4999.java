package bronze;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class no4999 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String sound = br.readLine();
        String reqSound = br.readLine();

        if (sound.length() >= reqSound.length()) {
            System.out.println("go");
        } else {
            System.out.println("no");
        }
    }
}
