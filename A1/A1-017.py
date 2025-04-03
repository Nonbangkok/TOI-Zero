first = [int(input()) for _ in range(3)]
second = [int(input()) for _ in range(3)]

def solve():
    for i in range(3):
        if first[i] < second[i]:
            return 1
        elif second[i] < first[i]:
            return 2
    return 0

print(solve())