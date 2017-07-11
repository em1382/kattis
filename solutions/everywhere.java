import java.util.Scanner;
import java.util.ArrayList;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int x = 0, y = 0, c = 0, i = 0;
        String str;
        ArrayList<String> cities = new ArrayList<String>();

        // Get num test cases
        c = sc.nextInt();

        // for each test case
        for (i = 0; i < c; i++) {
            // for each list of cities
            x = sc.nextInt();
            for (y = 0; y < x; y++) {
                str = sc.next();

                if (!cities.contains(str)) {
                    cities.add(str);
                }
            }
            System.out.println(cities.size());
            cities.clear();
        }
    }
}