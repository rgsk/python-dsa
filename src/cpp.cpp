#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n, x;
    cin >> n >> x;
    map<int, int> mp;
    for (int i = 0; i < n; i++) {
        int v;
        cin >> v;
        if (mp.find(x - v) != mp.end()) {
            cout << mp[x - v] + 1 << " " << i + 1 << endl;
            return 0;
        }
        mp[v] = i;
    }
    cout << "IMPOSSIBLE" << endl;
}