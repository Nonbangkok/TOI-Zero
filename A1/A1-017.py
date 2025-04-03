first = []
second = []

for i in range(3):
    first.append(int(input()))

for i in range(3):
    second.append(int(input()))

def solve():
    for i in range(3):
        if first[i] < second[i]:
            return 1
        elif second[i] < first[i]:
            return 2
    return 0

print(solve())