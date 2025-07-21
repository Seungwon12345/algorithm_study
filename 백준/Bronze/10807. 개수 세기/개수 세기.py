N = int(input())
a = list(map(int, input().split()))
v = int(input())

if N == len(a):
    count = 0
    for i in range(len(a)):
        if a[i] == v:
            count += 1
    print(count)