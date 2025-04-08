#include <bits/stdc++.h>
#define coutf(n, m) cout << fixed << setprecision(n) << m
#define forr(i, a, n) for (int i = a; i < n; i++)
#define forl(i, a, n) for (int i = a; i > n; i--)
#define macos ios::sync_with_stdio(0);cin.tie(0);cout.tie(0)
#define endll "\n"
#define sp " "
typedef long long ll;
using namespace std;

const int N = 1e5 + 10;
int n,m,k,a,cnt;
int tar[N],indeg[N];
bool vis[N];
vector<int> adj[N];
queue<int> q;

int main(){macos;

    cin >> n >> m;
    forr(i,1,m+1){
        cin >> k;
        forr(j,1,k+1){
            cin >> a;
            adj[a].push_back(i);
        }
        cin >> a;
        indeg[i] = k;
        tar[i] = a;
    }

    q.push(1);
    while(!q.empty()){
        int u = q.front();
        q.pop();

        if(vis[u])continue;
        vis[u] = true;
        cnt++;

        for(int i:adj[u]){
            indeg[i]--;
            if(!indeg[i])q.push(tar[i]);
        }
    }

    cout << cnt;

    return 0;
}