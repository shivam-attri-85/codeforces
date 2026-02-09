import java.util.*;
public class A112{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s1=sc.nextLine();
        String s2=sc.nextLine();

        int s=s1.compareToIgnoreCase(s2);
        if(s==0){
            System.out.println(s);
        }
        else if(s>0)
        System.out.println(1);
        else{
            System.out.println(-1);
        }
    }
}
