
def main():
    arrival1 = [0,0,1,2,0,3,5,2,4,0,6,1,8,7,5,0,9,10,4,0]
    index = ["p1","p2","p3","p4","p5","p6","p7","p8","p9","p10",
               "p11","p12","p13","p14","p15","p16","p17","p18","p19","p20"]
    burst1 = [3,1,2,4,2,3,1,2,3,1,4,2,3,2,1,3,2,4,2,1]
    priority1 = [8,3,14,1,7,20,5,9,4,2,16,11,6,12,18,10,3,7,13,1]
    tt = [0] * len(arrival1)
    wt = [0] * len(arrival1)
    indices = list(range(len(arrival1)))
    arrival = [arrival1[i] for i in indices]
    process = [index[i] for i in indices]
    burst = [burst1[i] for i in indices]
    priority = [priority1[i] for i in indices]
    queue = []
    time = 0
    remain = burst.copy()
    added = [False] * len(burst)
    quantum = 4
    completion = [0] * len(burst)
    # thêm các process bằng 0 vào hàng đợi
    for i in range(len(arrival)):
        if arrival[i] == 0:
            queue.append(i)
            added[i] = True
    # kiểm tra còn process nào chưa hoàn thành và chạy các tiến trình đã thêm vào queue cũng như thêm các tiến trình mới vào queue
    while any(r > 0 for r in remain):
        if not queue:
            time += 1
            for i in range(len(arrival)):
                if arrival[i] <= time and not added[i]:
                    queue.append(i)
                    added[i] = True
            continue
        p = queue.pop(0)
        run = min(quantum, remain[p])
        time += run
        remain[p] -= run
        for i in range(len(arrival)):
            if arrival[i] <= time and not added[i]:
                queue.append(i)
                added[i] = True
        if remain[p] > 0:
            queue.append(p)
        else:
            completion[p] = time
    for i in range(len(completion)):
        tt[i] = completion[i] - arrival[i]
    for i in range(len(completion)):
        wt[i] = tt[i] - burst[i]
    print("Process  Arrival  Burst Completion TT      WT")
    for i in range(20):
        print(f"P{i}        {arrival[i]}        {burst[i]}    {completion[i]}           {tt[i]}       {wt[i]}")
main()