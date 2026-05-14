nums = [3,2,3]
numslenght = len(nums)
for i in range(numslenght):
    if (nums.count(nums[i]) > 1 and nums.count(nums[i]) > numslenght/2):
        print(nums[i])
        break