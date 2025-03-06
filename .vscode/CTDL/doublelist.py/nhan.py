#ma tran 1
n = int(input("nhap so hang ma tran 1: "))
m = int(input("nhap so cot ma tran 1: "))
matrix1 = []
for _ in range(n):
    temp = list(map(int,input().split()))
    matrix1.append(temp)
#ma tran 2
x = int(input("nhap so hang ma tran 2: "))
y = int(input("nhap so cot ma tran 2: "))
matrix2 = []
for _ in range(x):
    temp = list(map(int,input().split()))
    matrix2.append(temp)
if m != x:
    print("hai ma tran khong the nhan nhau")
else:
    result = [[0] * y for _ in range(n)]
    for i in range(n):
        for j in range(y):
            for k in range(m):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
for row in result:  
    print(row)
