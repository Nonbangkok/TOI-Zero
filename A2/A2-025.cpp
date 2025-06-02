#include <bits/stdc++.h>
typedef long long ll;
using namespace std;

const int N = 10010;
const int di[] = {-1,-1,-1, 0,0, 1,1,1};
const int dj[] = {-1, 0, 1,-1,1,-1,0,1};
int n,m,dx,dy,p,a,b,cnt;
int warn[N][N];
vector<tuple<int,int,int>> v;

int main(){ios::sync_with_stdio(0);cin.tie(0);cout.tie(0);

    cin >> n >> m >> dx >> dy >> p;
    for(int i=0;i<p;i++){
        cin >> a >> b;
        v.push_back({a,b,100});
        warn[a][b] = 100;
    }

    while(!v.empty()){
        auto [x,y,val] = v.back();
        v.pop_back();
        if(val<0)continue;

        for(int k=0;k<8;k++){
            int xx = x + di[k];
            int yy = y + dj[k];

            if(xx<0||xx>=n||yy<0||yy>=m)continue;
            if(warn[xx][yy]>=val-40)continue;
            warn[xx][yy] = val - 40;
            v.push_back({xx,yy,val-40});
        }
    }

    for(int i=0;i<n;i++)for(int j=0;j<m;j++)if(!warn[i][j])cnt++;
    cout << cnt << "\n" << warn[dx][dy] << '%';

    return 0;
}