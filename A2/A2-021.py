import sys
input = sys.stdin.readline

n,k = map(int,input().split())
in1,in2 = list(map(int,input().split())),list(map(int,input().split()))
out1,out2 = list(map(int,input().split())),list(map(int,input().split()))
in1.sort(),in2.sort(),out1.sort(),out2.sort()

print(in1)
print(in2)
print(out1)
print(out2)