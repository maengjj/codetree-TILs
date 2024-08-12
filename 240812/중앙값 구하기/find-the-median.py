a, b, c = map(int, input().split())

if a<=b:
    if c<=a:
        print(a)
    elif b<=c:
        print(b)
    else:
        print(c)
elif b<=a:
    if c<=b:
        print(b)
    elif c<=a:
        print(c)
    else:
        print(a)