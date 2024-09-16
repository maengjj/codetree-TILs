cond = True

for _ in range(5):
    n = int(input())
    if n %3!=0:
        cond=False

if cond==True:
    print(1)
else: print(0)