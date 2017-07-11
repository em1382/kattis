import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int total = 0;
        int max = 0;
        int maxIndex = 0;

        String scores[] = new String[5];
        int contestants[] = new int[5];

        for(int i = 0; i < contestants.length; i++) {
            scores[i] = input.nextLine();
        }

        for(int i = 0; i < scores.length; i++) {
            String loc[] = new String[4];
            loc = scores[i].split(" ");

            for(int y = 0; y < loc.length; y++) {
                total += Integer.parseInt(loc[y]);
            }

            contestants[i] = total;
            if(total > max) {
                max = total;
                maxIndex = i + 1;
            }
            total = 0;
        }

        System.out.println(maxIndex + " " + max);
    }
}