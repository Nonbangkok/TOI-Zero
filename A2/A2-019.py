import sys
input = sys.stdin.readline
s = input().strip()
up = s.upper()

txt = "BUU"
mx,cnt = 0,0
first = -1
for i in range(len(up)):
    if first == -1 and up[i] == 'B':first = i
    if i>0 and up[i] == 'U' and up[i-1] == 'B':cnt = 1
    elif cnt and up[i] == 'U':cnt += 1
    else:cnt = 0
    mx = max(mx,cnt)

if mx:sys.stdout.write(f"Yes {mx}")
elif first != -1:sys.stdout.write(f"{s[:first+1]}{'U'*(len(s)-(first+1))}")
else:sys.stdout.write(''.join(txt[i%3] for i in range(len(s))))