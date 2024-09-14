a, b = map(int, input().split())
c = b-a

while c >= 0 :
    print(b, end=' ')
    b -= 1
    c -= 1