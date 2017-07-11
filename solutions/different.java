import java.util.Scanner;

public class Different {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        while (sc.hasNextLine()) {
            String[] line = sc.nextLine().split(" ");
            if (!"\n".equals(line[0])) {
                long a, b;
                a = Long.parseLong(line[0]);
                b = Long.parseLong(line[1]);
                System.out.println(java.lang.Math.abs(a - b));
            }
            else {
                break;
            }
        }
    }

}