import java.util.Scanner;
public class A231{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        int t=sc.nextInt();
        int imp=0;
        while(t>0){
            int c=0;
            int arr[]=new int[3];

            for(int i=0;i<3;i++){
                arr[i]=sc.nextInt();
               c=c+arr[i];
            }
            // for(int i=0;i<3;i++){
            //     c=c+arr[i];
            // }
            if(c>=2){
                imp=imp+1;;
            }
            t--;
        }
        System.out.println(imp);
        sc.close();
    }
}