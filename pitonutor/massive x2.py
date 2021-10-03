n, m = [int(i) for i in input().split()]
a = [[int(j) for j in input().split()] for i in range(n)]


row, column = 0, 0
curr_max = a[0][0]

for i in range(n):
    for j in range(m):
        if a[i][j] > curr_max:
            curr_max = a[i][j]
            row, column = i, j

print(row, column)