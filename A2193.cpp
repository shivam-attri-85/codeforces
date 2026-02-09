#include<bits/stdc++.h>
using namespace std;

void solve(){
int n,s,x;
cin>>n>>s>>x;
vector<int>a(n);
int sum=0;
for(int i=0;i<n;i++){
    cin>>a[i];
    sum+=a[i];
}
if(sum>s){
    cout <<"NO"<<endl;
}
else{
    if((s-sum)%x==0){
        cout <<"YES"<<endl;
    }
    else{
    cout <<"NO"<<endl;
    }
}
}
int main(){
    int t;
    cin>>t;
    while(t--){
        solve();
    }
}