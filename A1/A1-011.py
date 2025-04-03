a = input()
cnt = 1
for i in range(1,len(a)):
    if a[i] == a[i-1]:
        cnt = cnt + 1
    else:
        print(f"{cnt}{a[i-1]}",end='')
        cnt = 1
print(f"{cnt}{a[-1]}",end='')