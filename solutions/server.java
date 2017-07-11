import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int t = sc.nextInt();

        int total = 0, tasks = 0;

        for(int i = 0; i < n; i++) {
            int task = sc.nextInt();

            if (task + total > t) {
                break;
            }
            else {
                total += task;
                tasks += 1;
            }
        }

        System.out.println(tasks);
    }
}