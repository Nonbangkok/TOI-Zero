a = [10,25,3]
b= list(map(int,input().split()))
print(sum(x*y for x,y in zip(a,b)))