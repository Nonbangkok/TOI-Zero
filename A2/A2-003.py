n = int(input())
a = list(map(int,input().split()))
print(sum(1 for i in range(len((a))) if i == 0 and a[i] > a[i+1] or i == n-1 and a[i-1] < a[i] or a[i-1] < a[i] > a[i+1]))