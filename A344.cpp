#include<bits/stdc++.h>
using namespace std;
int main(){
    long long int t;
    cin>>t;
    long long int arr[t];
    long long int c=1;
   cin>>arr[0];
    for(int i=1;i<t;i++){
        cin>>arr[i];
        if(arr[i]!=arr[i-1]){
            //cout <<arr[i]<<" ";
            c++;
        }
        }
        cout <<c<<endl;
        return 0;
}