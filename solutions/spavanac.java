import java.text.SimpleDateFormat;
import java.util.*;

public class Main {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int hr = sc.nextInt();
        int min = sc.nextInt();
        Calendar cal = Calendar.getInstance();
        cal.set(Calendar.HOUR_OF_DAY, hr);
        cal.set(Calendar.MINUTE, min - 45);

        Date date = cal.getTime();

        SimpleDateFormat d = new SimpleDateFormat("k m");

        System.out.println(d.format(date));
    }
}