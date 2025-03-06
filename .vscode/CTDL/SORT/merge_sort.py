def merge_sort(arr):
    if len(arr) > 1: #with  5 4 6 1 2 7 3 
        mid = len(arr) // 2  #mid 7//2 = 4
        left_half = arr[:mid]  #5 4 6 1
        right_half = arr[mid:]  #2 7 3

        merge_sort(left_half) # 5 4 ! 6 1
        merge_sort(right_half) # 2 7 ! 3
        i = j = k = 0
        while i < len(left_half) and j < len(right_half): # 0 < 1(4)and 0 < 1(6)
            if left_half[i] < right_half[j]: 
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
n = int(input(""))
mang= []
for c in range(n):  
    mang.append(int(input("")))
merge_sort(mang)
for c in mang:
    print(c,end=" ")
