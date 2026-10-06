// Starting with the name of Almighty ALLAH
#include <bits/stdc++.h>
using namespace std;

#define int long long 
#define nl "\n"
const int N = 1e9 + 7;
#define TC int t;cin >> t;while (t--)

#define FIO ios_base::sync_with_stdio(0);cin.tie(0);cout.tie(0);


void mgf() {
    int n;
    string a, b;
    cin >> n >> a >> b;
    
    int ao = 0, bo = 0;    
    for(int i = 1; i < n; i += 2) {
        if(a[i] == '1') ao++;
        if(b[i] == '1') bo++;
    }

    int ap = 0, bp = 0;    
    for(int i = 0; i < n; i += 2) {
        if(a[i] == '1') ap++;
        if(b[i] == '1') bp++;
    }
    
    if(ao == bo && ap == bp) cout << "YES" << nl; 
    else cout << "NO" << nl;
}

int32_t main() {
    FIO
    TC
    mgf();
    return 0;
}
// Coded by Abu Bakr Siddique [@AbuBakrSiddique]
