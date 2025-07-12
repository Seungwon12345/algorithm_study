T = int(input())

if T % 10 != 0:
    print(-1)
else:
    A = B = C = 0
    while T > 0:
        if T >= 300:
            T -= 300
            A += 1
        elif T >= 60:
            T -= 60
            B += 1
        else:
            T -= 10
            C += 1
    print(A, B, C)