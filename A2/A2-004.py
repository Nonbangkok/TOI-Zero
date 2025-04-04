from collections import Counter

n = int(input())
a = [int(input()) for _ in range(n)]
print(Counter(a).most_common(1)[0][1])