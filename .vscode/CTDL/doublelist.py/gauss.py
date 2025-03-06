# def check(n,matrix):
#     button = True
#     for i in range(1, n):
#         for j in range(i):
#             if matrix[i][j] != 0:
#                 button = False
#                 break
#     return button
def main():
    n = int(input("row: "))
    m = int(input("colum: "))
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
                    print(f"swap row {c+1} and row {i+1}")
                    for row in matrix:
                        print(row)
                    break
            pivot = matrix[i][i]
        for j in range(i+1,n):
            percent_40 = matrix[j][i] / pivot 
            for k in range(i,m):
                matrix[j][k]-= int((percent_40 * matrix[i][k]))
    print("Result: ")
    for row in matrix:
        print(row)
main()