import java.util.Scanner;

public class Aaah {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String a = sc.nextLine();
        String b = sc.nextLine();

        sc.close();

        if (a.length() < b.length()) {
            System.out.println("no");
        } else {
            System.out.println("go");
        }
    }
}