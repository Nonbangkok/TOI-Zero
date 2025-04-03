even,odd = 0,0

for i in range(3):
    a = int(input())
    if a % 2 == 0:
        even += 1
    else:
        odd += 1;

print(f"even {even}")
print(f"odd {odd}")