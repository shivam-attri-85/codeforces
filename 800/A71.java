import java.util.*;
public class A71{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        sc.nextLine();
        while(t-->0){
        String s=sc.nextLine();
        int n=s.length();

        if(n>10){
            System.out.println(s.charAt(0)+ String.valueOf(n-2) +s.charAt(n-1));
        }      
        else{
            System.out.println(s);
        }
    }
        sc.close();
    }
}