amath, aeng = map(int, input().split())
bmath, beng = map(int, input().split())

if bmath>amath:
    print("B")
elif amath>bmath:
    print("A")
else:
    if aeng>beng:
        print("A")
    elif beng>amath:
        print("B")