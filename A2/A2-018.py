n = 0
c = input().split()
if c[0] == 'G':n = 1
elif c[0] == 'B':n = 2
colors = ["Red","Green","Blue"]
print(*list(colors[i%3] for i in range(n,int(c[1])+n)))