n = int(input("Row: "))
m = int(input("Colunm:  "))
matrix = []
for _ in range(n):
    temp = list(map(int,input().split()))
    matrix.append(temp)
for row in matrix:
    print(row)
if m == n:
    print("Matrix square")
else:
    print("Matrix Normal")
