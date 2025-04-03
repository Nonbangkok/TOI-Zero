a,sign = int(input()),input()
b = int(str(a)[::-1])

if sign == '+':
    c = a + b
else:
    c = a * b
    
print(f"{a} {sign} {b} = {c}")