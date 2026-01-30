def nhap():
    return list(map(int, input().split()))
def main():
    process = [1, 2, 3, 4]
    print("arrival: "); arrival = nhap()
    print("busrt: "); burst = nhap()
    n = 4
    start = [0] * n
    start[0] = arrival[0]
    finish = [0] * n
    finish[0] = start[0] + burst[0]
    for i in range(1,n):
        start[i] = max(finish[i-1], arrival[i])
        finish[i] = start[i] + burst[i]
    wt = [0] * n
    for i in range(n):
        wt[i] = start[i] - arrival[i]
    Turnaround = [0] * n
    for i in range(n):
        Turnaround[i] = finish[i] - arrival[i]
    print("Process  Arrival  Burst  Waiting  Turnaround")
    for i in range(len(process)):
        print(f"P{process[i]}        {arrival[i]}        {burst[i]}        {wt[i]}        {Turnaround[i]}")
main()