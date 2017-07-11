import java.util.Scanner;

public class Conundrum {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int days = 0, c = 0;
        
        String encrypted = sc.nextLine();
        
        for(int i = 0; i < encrypted.length(); i++) {
            if (c == 0 && encrypted.charAt(i) != 'P') {
                days++;
            }
            else if (c == 1 && encrypted.charAt(i) != 'E') {
                days++;
            }
            else if (c == 2 && encrypted.charAt(i) != 'R') {
                days++;
            }
            
            if (c == 2) {
                c = 0;
            }
            else {
                c++;
            }
        }
        
        System.out.println(days);
    }
    
}