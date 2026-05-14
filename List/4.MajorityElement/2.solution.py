nums = [2,2,1,1,1,2,2]
numslenght = len(nums)
for i in range(numslenght):
    count = 0
    for j in range(numslenght):
        if (nums[i] == nums[j]):
            count += 1
    if(count > 1 and count > numslenght/2):
            print(nums[i])
            break