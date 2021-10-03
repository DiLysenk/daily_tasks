n = int(input())

a = [["." for i in range(n)] for j in range(n)]

for i in range(n):
    a[n // 2][i] = "*"
    a[i][n // 2] = "*"
    a[i][n-1-i]= "*"
    a[i][i] = "*"

[print(a[i]) for i in range(n)]