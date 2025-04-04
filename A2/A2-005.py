w,h,m,n = map(int,input().split())
a = [0] + list(map(int,input().split())) + [w]
b = [0] + list(map(int,input().split())) + [h]

mx1,mx2 = 0,0
for i in range(1,len(a)):
    for j in range(1,len(b)):
        area = (a[i]-a[i-1]) * (b[j]-b[j-1])
        if area > mx1:
            mx2 = mx1
            mx1 = area
        elif area > mx2:
            mx2 = area

print(mx1,mx2)