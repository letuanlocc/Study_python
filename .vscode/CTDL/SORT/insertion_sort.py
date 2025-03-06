def insertion_sort(mang): #with 4 3 1 5 7 9 6 2
 n = len(mang) 
 for i in range(1,n):
     key = mang[i] # key = 3 
     pos = i - 1 #pos = 0
     while pos >= 0 and key < mang[pos]: #3 < mang[0](4) 
         mang[pos + 1] = mang[pos] # mang[1] = mang[0] =>> 4 4 1 5 7 9 6 2 
         pos -= 1 #pos = -1
     mang[pos + 1] = key #mang[0] = 3 =>> 3 4 1 5 7 9 6 2 
def main():
 n = int(input(""))
 mang = []
 for i in range(n):
     mang.append(int(input("")))
 insertion_sort(mang)   
 print(mang)    
main()
