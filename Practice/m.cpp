#include<iostream>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t>0){
        int n;
        cin >> n;
        int arr[n];
        int sum0=0;
        int sum1=0;
        for(int i=0;i<n;i++){
            cin >> arr[i];
        }
        for(int i=0;i<n;i++){
            if(arr[i]==0){
                sum0++;
            
            }
            if(arr[i]==-1){
                sum1++;
            }

        }
        int r=sum1%2;
        if(sum1%2==0){
            sum1=0;
        }
        else{
        sum1=r*2;
        }
       cout << sum0+sum1<<endl;


        t--;
    }
}