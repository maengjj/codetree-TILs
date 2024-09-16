n = int(input())
cnt = 0

while True:
    if n>=1000:
        print(cnt)
        break
    
    if n%2==0:
        n=3*n+1
        cnt += 1
        continue
    else:
        n=2*n+2
        cnt += 1
        continue