n = int(input("nhap so hang: "))
m = int(input("nhap so cot: "))
matrix1 = []
for _ in range(n):
    temp = list(map(int,input().split()))
    matrix1.append(temp)
x = int(input("nhap so hang: "))
y = int(input("nhap so cot: "))
matrix2 = []
for _ in range(x):
    temp = list(map(int,input().split()))
    matrix2.append(temp)
if x*y != m*n:
    print("----------------Eror Logic-------------------")
else:
    result = [[0] * m for _ in range(n)]
    for i in range(n):
       for j in range(m):
        result[i][j] += matrix1[i][j] +  matrix2[i][j]
    for row in result:
        print(row)

