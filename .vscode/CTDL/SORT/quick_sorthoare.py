import random
def partitionhoare(mang,low,high):
    pivot = mang[low] #pivot = vi tri dau tien
    i = low - 1  # truoc vi tri 0
    j = high + 1 #sau vi tri cuoi cung
    while i < j: #with [4] 8 4 1 1 1 3 8 6 2 
        i += 1
        while mang[i] < pivot:
            i += 1
        j -= 1
        while mang[j] > pivot:
            j -= 1
        if i >= j:
            return j
        mang[i],mang[j] = mang[j],mang[i]   
def quick_sort(mang,low,high):
    if low < high:
        pos_pivot = partitionhoare(mang,low,high) #low = 0 ! high = len(mang) - 1
        quick_sort(mang,low,pos_pivot )
        quick_sort(mang,pos_pivot + 1,high)
def main():
    n = int(input(""))
    mang = []
    for i in range(n):
        mang.append(int(input("")))
    #quy hoach hoare::
    quick_sort(mang,0,len(mang) - 1) #mean is run 2 => 8 
    #================
    print(mang)     
main()