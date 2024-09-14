a, b = map(int, input().split())


if b>a : 
    c = b-a
    while c >= 0 :
        print(b, end=' ')
        b -= 1
        c -= 1
else : 
    c = a-b
    while c >= 0 :
        print(a, end=' ')
        a -= 1
        c -= 1