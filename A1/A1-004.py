standard = [5,20,25]
chk = True

for x in standard:
    a = int(input())
    if a < x:
        chk = False
    
print("yes" if chk else "fail")