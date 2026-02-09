import java.util.Scanner;public class A271 {
public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    
    while(n++ <9876){
    int a = n % 10;
    int b = (n / 10) % 10;
    int c = (n / 100) % 10;
    int d = (n / 1000) % 10;

        if(a!=b && b!=c && c!=d && d!=a && a!=c && b!=d){
            System.out.println(n);
            break ;
        }
    }
sc.close();
}
}
