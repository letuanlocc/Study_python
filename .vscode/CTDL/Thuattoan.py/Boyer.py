nums = [3,2,3,4,2,3,3]
candidate = None
count = 0
for c in nums:
    if count == 0:
        candidate = c
    if c == candidate:
        count += 1
    else:
        count -= 1
print(candidate) 