n = int(input())
dict1,dict2 = {},{}

for i in range(n):
    x,y = map(int,input().split())
    dict1[x-y] = [min(dict1.get(x-y,[x,x])[0],x),max(dict1.get(x-y,[x, x])[1],x)]
    dict2[x+y] = [min(dict2.get(x+y,[x,x])[0],x),max(dict2.get(x+y,[x, x])[1],x)]

print(max([y-x for x,y in dict1.values()]+[y-x for x,y in dict2.values()]))