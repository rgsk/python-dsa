#include <bits/stdc++.h>
using namespace std;

int main() {
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
#endif
    int n;
    cin >> n;
    vector<pair<int, int>> events;
    for (int i = 0; i < n; i++) {
        int a, l;
        cin >> a >> l;
        events.push_back({a, 1});
        events.push_back({l, -1});
    }
    sort(events.begin(), events.end());
    int occupied = 0;
    int max_occupied = 0;
    for (int i = 0; i < 2 * n; i++) {
        occupied += events[i].second;
        max_occupied = max(max_occupied, occupied);
    }
    cout << max_occupied << endl;
}