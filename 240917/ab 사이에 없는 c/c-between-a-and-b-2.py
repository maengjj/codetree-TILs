a, b, c = map(int, input().split())
cond=False

for i in range(a, b+1):
    if i % c != 0:
        cond=True

if cond==True:
    print("YES")
else: print("NO")