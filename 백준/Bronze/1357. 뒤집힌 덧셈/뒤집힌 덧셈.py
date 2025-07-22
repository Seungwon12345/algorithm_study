X, Y = input().split()

r_X = int(X[::-1])
r_Y = int(Y[::-1])
r_sum = str(r_X + r_Y)[::-1]

print(int(r_sum))