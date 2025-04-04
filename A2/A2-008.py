n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort()

eff = data[0][1]
cnt = n-1
for i in range(1,n):
    if eff < data[i][1]:
        eff = data[i][1]
        cnt -= 1

print(cnt)