def shell_sort(mang):  #5, 4, 3, 2, 1 
    n = len(mang) #len(mang) = 5
    interval = n // 2 #interval = 2 !! [5,3,1]; [4,2]
    while interval  > 0:
      for i in range(interval): #0 => 4
         mangtam = [mang[x]  for x in range(i,len(mang),interval)]  # i = 0
         for j in range(1,len(mangtam)): #[5,3,1]
           key = mangtam[j] #key = 3
           pos = j - 1 #pos = 0
           while pos >= 0 and key < mangtam[pos]: 
              mangtam[pos + 1] = mangtam[pos] #[5,5,1]
              pos -= 1
           mangtam[pos + 1] = key #[3,5,1]
         for j in range(len(mangtam)):
                mang[i + j * interval] = mangtam[j]
      interval //= 2
def main():
    n = int(input(""))
    mang = []
    for i in range(n):
       mang.append(int(input("")))
    shell_sort(mang)
    print(mang)
main()