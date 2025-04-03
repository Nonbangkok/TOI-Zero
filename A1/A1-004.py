standard = [5,20,25]
chk = True

for x in standard:
    a = int(input())
    if a < x:
        chk = False
    
if chk:
    print("pass")
else:
    print("fail")