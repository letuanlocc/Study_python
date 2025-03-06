# def check(n,matrix):
#     button = True
#     for i in range(1, n):
#         for j in range(i):
#             if matrix[i][j] != 0:
#                 button = False
#                 break
#     return button
def main():
    n = int(input("Nhap so row: "))
    m = int(input("Nhap so colum: "))
    matrix = []
    for _ in range(n):
        temp = list(map(int,input().split()))
        matrix.append(temp)
    for i in range(min(n,m)):
        pivot = matrix[i][i]
        if pivot == 0:
            for c in range(i+1,n):
                if matrix[c][i] != 0:
                    matrix[c],matrix[i] = matrix[i],matrix[c]
                    print(f"hoan doi hang {c} va hang {i}")
                    break
            pivot = matrix[i][i]
        for j in range(i+1,n):
            percent_40 = matrix[j][i] / pivot 
            for k in range(i,m):
                matrix[j][k]-= int((percent_40 * matrix[i][k]))
    for row in matrix:
        print(row)
main()