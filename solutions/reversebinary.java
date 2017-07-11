import java.util.Scanner;

/**
 *
 * @author Ellis
 */
public class Reversebinary {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int norm = sc.nextInt();
        String bin = Integer.toBinaryString(norm);
        bin = new StringBuilder(bin).reverse().toString();
        System.out.println(Integer.parseInt(bin, 2));
    }
}
