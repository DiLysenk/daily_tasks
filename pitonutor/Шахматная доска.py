n, m = [int(i) for i in input().split()]

a = [["." for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        if j % 2 == 1 and i % 2 == 0:
            a[i][j - m] = "*"
        elif j % 2 == 1:
            a[i][j - m - 1] = "*"
            a[i][j - m + 1] = "*"

if m == 1:
    for i in range(n):
        for j in range(m):
            if i % 2 == 1:
                a[i][j - m] = "*"


for row in a:
    print(' '.join(row))
