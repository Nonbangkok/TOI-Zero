a = set([input() for _ in range(3)])

if len(a) == 1:
    print("all the same")
elif len(a) == 3:
    print("all different")
else:
    print("neither")