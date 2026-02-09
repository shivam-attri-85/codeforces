#include<iostream>
using namespace std;
int main(){
    int l,b;

    cin >> l >> b;
    int c=0;
    while(l<=b){
        l=l*3;
        b=b*2;
        c++;
    } 
    cout << c <<endl;
}