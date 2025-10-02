#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    int t;
    cin >> t;
    while(t>0){
        int n;
        cin >>n;
        int arr[n];
        for(int i=0;i<n;i++){
            cin >> arr[i];
        }
        int x=abs(arr[0]-arr[1]);

         for (int j=2;j<n;j++){
            int diff=abs(arr[j]-arr[j-1]);
            x=min(x,diff);
         }
        cout << x<<endl;
        t--;
        }
}