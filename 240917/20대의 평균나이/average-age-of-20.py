age = []
cnt = 0
while True:
    n = int(input())
    if n//10!=2:
        print(f'{sum(age)/cnt:.2f}')
        break
    age.append(n)
    cnt +=1