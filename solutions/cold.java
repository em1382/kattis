import java.util.Scanner;
public class Cold {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int days = 0, times = sc.nextInt();
        
        for (int i = 0; i < times; i++) {
            if (sc.nextInt() < 0) {
                days++;
            }
        }
        
        System.out.println(days);
    }
    
}