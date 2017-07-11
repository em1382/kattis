import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int numCases = 0;
        numCases = input.nextInt();

        for(int i = 0; i < numCases; i++) {
            int num = input.nextInt();
            if (num % 2 == 0)
                System.out.println(num + " is even");
            else
                System.out.println(num + " is odd");
        }
    }
}