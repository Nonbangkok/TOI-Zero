import sys
input = sys.stdin.readline

l,n = map(int,input().split())
A = [0 for _ in range(l+1)]
mx = 0

for i in range(n):
    a,b = map(int,input().split())
    for j in range(a,b):
        A[j] += 1
        mx = max(mx,A[j])

print(mx)