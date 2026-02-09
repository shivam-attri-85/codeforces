import java.util.Scanner;

public class A460 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();  
        int m = sc.nextInt();
        int days = 0;
        while (n > 0) {
            days++;
            n--;  
            if (days % m == 0) {
                n++;  
            }
        }

        System.out.println(days);
        sc.close();
    }
}