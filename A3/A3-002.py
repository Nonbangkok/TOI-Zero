# n = int(input())
# l = 0
# while (l+1)*(l+1) < n:
#     l += 1
# print(2*l-(l&1==n&1))

from math import *
n = int(input())
l = floor(sqrt(n-1))
print(2*l-(l&1==n&1))