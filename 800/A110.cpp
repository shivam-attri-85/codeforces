    #include <bits/stdc++.h>
    using namespace std;
     
    int main() {
        long long n;
        cin >> n;
        int cnt=0;
        while (n>0) 
        {
            int d=n%10;
            if (d==4||d==7)
                cnt++;
            n =n/10;
        }
     
        if(cnt==0) {
            cout<<"NO"<<endl;
            return 0;
        }
     
        while (cnt >0){
            int d=cnt%10;
            if (d !=4&&d!=7) {
                cout << "NO" << endl;
                return 0;
            }
            cnt /= 10;
        }
     
        cout << "YES" << endl;
        return 0;
    }