matrix = [[0,1,2,0],
          [3,4,5,2],
          [1,3,1,5]
]
m = len(matrix)
n = len(matrix[0]) if m > 0 else 0
x = []
for i in range(m):
    for j in range(n):
        if matrix[i][j] == 0:
            x.append((i,j))
for i in range(m):
    for j in range(n):
        for row,col in x:
            if i == row or j == col:
                matrix[i][j] = 0
print(x)
for row in matrix:
    print(row)