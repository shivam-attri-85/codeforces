import java.util.*;
public class A110 {
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int n=sc.nextInt();
    int s=0;
    int c=0;
    while(n>0){
        if(s==c){
        if (n%10==4 || n%10==7){
            s++;
        }
        c++;
        n=n/10;
    }
    else{
        break;
    }
    }     
    if(c==s){
        System.out.println("YES");
    }
    else{
        System.out.println("NO");
    }
    }
}
//it requied study of Big Integer and Big Decimals 