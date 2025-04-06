import sys
input = sys.stdin.readline
a = input().strip().lower()
b = input().strip().lower()

# a = input().lower()
# b = input().lower()

if len(a) < len(b):
    a,b = b,a

ans = []
i,j = 0,0
nw,cnw,mx = 0,0,0

while i < len(a):
    if a[i] in 'love' or b[j] in 'love':
        ans.append('w')
        nw,cnw = nw + 1,cnw + 1
        mx = max(mx,cnw)
    else:
        ans.append('$')
        cnw = 0
    i,j = i + 1,j + 1
    if j == len(b):
        j = 0

if nw&1:ans.append(str(mx))
elif mx<2:ans.append('#')

print(''.join(ans))