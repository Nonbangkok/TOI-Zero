n,c = map(int,input().split())
data = [list(map(int,input().split())) for _ in range(n)]
player = [i for i in range(1,n+1)]

while len(player) > 1:
    winner = []
    for i in range(1,len(player),2):
        if (c == player[i-1] or c == player[i]) and c != data[player[i-1]-1][player[i]-1]:
            winner.append(c)
            c = 0
        else:
            winner.append(data[player[i-1]-1][player[i]-1])
    player = winner
    
print(player[0])