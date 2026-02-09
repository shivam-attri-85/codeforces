// import java.util.Scanner;
// public class A546 {
//     public static void main(String[] args) {
//     Scanner sc=new Scanner(System.in);
//     int k=sc.nextInt();
//     int n=sc.nextInt();
//     int w=sc.nextInt();
//         int s=0;
//         for(int i=1;i<=w;i++){
//             s=k*i+s;
//         }
//         System.out.println(s-n);//total mon- money uske pass h - 
    
    
//         sc.close();        
//     }
// }
//or


import java.util.Scanner;
public class A546 {
    public static void main(String[] args) {
    Scanner sc=new Scanner(System.in);
    int k=sc.nextInt();
    int n=sc.nextInt();
    int w=sc.nextInt();
    
       int s=k*(w*(w+1))/2;
        
        System.out.println(Math.max(0,s-n));   //total mon- money uske pass h - 
        sc.close();        
    }
}
