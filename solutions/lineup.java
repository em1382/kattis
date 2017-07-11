import java.util.Scanner;
import java.util.ArrayList;
import java.util.Collections;

public class Lineup {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int total = sc.nextInt();
        ArrayList<String> names = new ArrayList<>();
        
        for (int i = 0; i < total; i++) {
            names.add(sc.next());
        }
        
        ArrayList<String> namesCopy = new ArrayList<>(names);

        Collections.sort(namesCopy);
        if (namesCopy.equals(names)) {
            System.out.println("INCREASING");
        } else {
            Collections.reverse(namesCopy);
            if (namesCopy.equals(names)) {
                System.out.println("DECREASING");
            } else {
                System.out.println("NEITHER");
            }
        }        
        sc.close();
    }
}