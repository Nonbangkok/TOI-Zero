a = set()
a.add(int(input()))
a.add(int(input()))
a.add(int(input()))

if len(a) == 1:
    print("all the same")
elif len(a) == 3:
    print("all different")
else:
    print("neither")