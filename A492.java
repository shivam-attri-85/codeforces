import java.util.Scanner;
public class A492 {
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int cb=sc.nextInt();
        int sum=0;
        int lv=0;
        for(int i=1; ;i++){
            sum=sum+(i*(i+1)/2);
            if(sum>cb){
                break;
            }
            lv++;
        }
        System.out.println(lv);

        sc.close();
    }
    
}
