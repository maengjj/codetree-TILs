n = int(input())
cond = True

for i in range(2, n+1):
    if n % i == 0 and n!=i:
        cond = False

if cond==False:
    print("C")
else: print("P")