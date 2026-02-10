import java.util.*;
public class A677 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int h=sc.nextInt();
        int s=0;
        int height=0;
        for(int i=0;i<n;i++){
        height=sc.nextInt();
        
        if(height>h){
            s=s+2;
        }
        else{
            s++;
        }
    }
        System.out.println(s);
    
    
    sc.close();}
}
