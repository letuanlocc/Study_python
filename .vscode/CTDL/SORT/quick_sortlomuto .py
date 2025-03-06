
def partitionlomuto(mang,low,high):
    pivot = mang[high] #pivot = mang[7]
    i = low -1
    for j in range(low,high):
        if mang[j] < pivot:
            i += 1
            mang[i],mang[j] = mang[j],mang[i]
    #sau khi ket thuc vong for thi gia tri cua i = 2 mean is tro vao 3
    #i + 1 tuong duong voi 8 in oder swap with 4 
    mang[i+1],mang[high] = mang[high],mang[i+1] # 2 1 3 [4] 5 7 6 8 
    return i + 1
def quick_sort(mang,low,high):
    if low < high:
       pos_pivot = partitionlomuto(mang,low,high) #low = 0 ! high = len(mang) - 1
       quick_sort(mang,low,pos_pivot - 1)
       quick_sort(mang,pos_pivot + 1,high)
def main():
    n = int(input(""))
    mang = []
    for i in range(n):
        mang.append(int(input("")))
    #quy hoach lomuto::
    quick_sort(mang,0,len(mang) - 1) #mean is run 2 => 8 
    #================
    for c in mang:
        print(c,end=" ")
    
main()
    