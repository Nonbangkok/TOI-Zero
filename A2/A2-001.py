n,m = map(int,input().split())
a = [0] + list(map(int, input().split()))
b = [0] + list(map(int, input().split()))

cnt = 1
for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i] == b[j]:
            cnt += 1
        elif i % 2 == j % 2:
            if (a[i] < b[j] and a[i-1] > b[j-1]) or (a[i] > b[j] and a[i-1] < b[j-1]):
                cnt += 1
        else:
            if (a[i-1] < b[j] and a[i] > b[j-1]) or (a[i-1] > b[j] and a[i] < b[j-1]):
                cnt += 1
                
print(cnt)