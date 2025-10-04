import java.sql.SQLOutput;
import java.util.*;
public class A236{
    public static void main(String []args){
        Scanner sc=new Scanner(System.in);
        String s=sc.nextLine();
        int n=s.length();
        String ch;
        int sum=0;
        for(int i=0;i<n;i++){
            ch=s.charAt(i);
          if(s.contains(ch)==true){
              sum++;
          }
        }
        if(sum%2==0){
            System.out.println("CHAT WITH HER!");
        }
        else{
            System.out.println("IGNORE HIM!");
        }
        sc.close();
    }
}

//we can do it by using hashset kyoki usme set ka use hoga toh repititive nhi aayegi 
