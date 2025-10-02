#include<iostream>
using namespace std;
int main(){
int t;
cin >>t;
while(t>0){
    int n,k;
    cin >>n >> k;
    int arr[n];
    for(int i=0;i<n;i++){
        cin >> arr[i];


    }
    int s=0;
    for(int i=0;i<n;i++){
        if(arr[i]==k){
            s++;
        }
    }
    cout << s <<endl;

    
    
    
    
    
    
    
    t--;
}
}