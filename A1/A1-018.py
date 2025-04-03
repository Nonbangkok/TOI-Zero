a = int(input())

if a < 0:
    print("Error : Please input positive number")
elif a == 0 or a >= 10:
    print("Error : Out of range")
elif a <= 3:
    for i in range(a):
        print("I",end='')
elif a == 4:
    print("IV")
elif a == 5:
    print("V")
elif a <= 8:
    print("V",end='')
    for i in range(a-5):
        print("I",end='')
else:
    print("IX")
    