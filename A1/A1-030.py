n = int(input())
numbers = [int(x) for x in input().split()]
ans = []
sum = 0

for i in range(0,len(numbers),2):
    mx = max(numbers[i],numbers[i+1])
    sum = sum + mx
    ans.append(mx)

print(sum if len(ans) == 1 else f"{' + '.join(str(x) for x in ans)} = {sum}")