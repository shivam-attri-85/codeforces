#include<iostream>
using namespace std;
int main(){
    int n,m,days=0;
    cin >> n >> m;
    while(n>0){
        days++;
        n--;
        if(days%m==0){
            n++;
        }

    }
    cout << days <<endl;
}