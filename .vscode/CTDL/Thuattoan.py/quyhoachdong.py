# #dãy con tăng dần liên tiếp dài nhất:
# arr = []
# n = int(input(""))
# for i in range(n):
#     arr.append(int(input("")))
# max_len = 1
# max_now = 1
# vitri_batdau = 0
# vitri_ketthuc = 0
# for j in range(1, n):
#     if arr[j] > arr[j-1]:
#         max_now += 1
#     else:
#         if max_now > max_len:
#             max_len = max_now
#             vitri_ketthuc = j - 1
#             vitri_batdau = vitri_ketthuc - max_len + 1
#         max_now = 1
# # Kiểm tra dãy tăng dài nhất nếu nó kết thúc ở cuối danh sách
# if max_now > max_len:
#     max_len = max_now
#     vitri_ketthuc = n - 1
#     vitri_batdau = vitri_ketthuc - max_len + 1
# #In dãy con liên tiếp tăng dần dài nhất
# for c in range(vitri_batdau, vitri_ketthuc + 1):
#     print(arr[c], end=" ")
# ================================================================
# dãy con tăng dần không liên tiếp dài nhất
# B1: khởi tạo 2 mảng dp 
# n = int(input(""))
# arr = []
# for _ in range(n):
#     arr.append(int(input("")))
# dp = [1] * n #dp[i] là độ dài dãy con tăng dài nhất kết thúc tại phần tử arr[i],vì mỗi phần tử có thể là dãy con tăng dài với độ dài 1
# for i in range(1,n): #4
#     for j in range(i): # 0 1 2 3
#         if arr[j] < arr[i] and dp[j] + 1 > dp[i]: #thỏa mãn
#             dp[i] = dp[j] + 1 #phần tử i hiện tại sẽ bằng độ dài của phần tử trước + 1
# max_len = max(dp)
# lis = []
# for i in range(n - 1, -1, -1):
#     if dp[i] == max_len:
#         lis.append(arr[i])
#         max_len -= 1
# lis.reverse()
# print("Dãy con tăng dài nhất:", lis)
# dp[1,2,1,1,3]
# prev[-1,0,-1,-1,1]
# [3,10,2,1,20]
# Bài 2: bài toán đổi tiền
# def money_change(a, n, x):
#     # Tạo mảng lưu số lượng tờ tiền cần dùng
#     l = [float('inf')] * (x + 1)  
#     # Gán giá trị ban đầu cho các mệnh giá
#     for i in range(n):
#         if a[i] <= x:
#             l[a[i]] = 1
#     # Duyệt qua các số tiền từ 1 đến x
#     for i in range(1, x + 1): #4
#         for j in range(n): #0 1
#             if i >= a[j]:
#                 # Nếu có thể tạo được i bằng cách thêm mệnh giá a[j]
#                 l[i] = min(l[i],l[i-a[j]] + 1)
#     return l[x]
# # Hàm chính
# if __name__ == "__main__":
#     n = int(input())  # Số lượng mệnh giá
#     a = []
#     for _ in range(n):
#         a.append(int(input()))
#     x = int(input())  # Số tiền cần đổi
#     if money_change(a,n,x) != float('inf'):
#         print(money_change(a, n, x))
#     else:
#        print("0")
# #bài 3:Chọn quà
# def choosegift(mang, n):
#     s = [[0, -1] for _ in range(n)]
#     for c in range(n):
#         s[c][0] = mang[c]
#         s[c][1] = -1
#     for c in range(1,n):
#         for j in range(c):
#             if mang[j] == mang[c] and s[j][0] + mang[c] > s[c][1]:      
#                 s[c][1] = s[j][0] + mang[c] #luc nay gia tri cua mon qua c duoc coi la lan chon chan va chay nguoc ve sau
#         for j in range(c):
#             if s[j][1] + mang[c] > s[c][0]:
#                 s[c][0] = s[j][1] + mang[c]#luc nay gia tri cua mon qua c duoc coi la lan chon le va chay tien toi 
#     max_value = -1    
#     for i in range(n):
#         for j in range(2):
#             if s[i][j] > max_value:
#                 max_value = s[i][j]
#     return max_value
# #tim gia tri lon nhat cua mang
# n = int(input())
# mang = []
# for _ in range(n):
#     mang.append(int(input()))
# print(choosegift(mang,n))
