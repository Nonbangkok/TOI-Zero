a = [int(input()) for _ in range(3)]
b = sorted(a)
c = sorted(a,reverse=True)

if len(set(a)) != 3:
    print("neither")
elif a == b:
    print("increasing")
elif a == c:
    print("decreasing")
else:
    print("neither")