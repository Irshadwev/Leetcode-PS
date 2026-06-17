nums = [7,3,4,9,1]

# Count Function 
def countn(num, nums):
    c = 0
    for i in range(len(nums)):
        if (num == nums[i]):
            c += 1
    return c

print(countn(3, nums))

# Sort function
# Assending Sort Function
def assendingsort(nums):
    for i in range(len(nums)):
        for j in range(1 + i, len(nums)):
            if (nums[i] > nums[j]):
                sort = nums[j]
                nums[j] = nums[i]
                nums[i] = sort
    return nums

# Dessending Sort Function
def dessendingsort(nums):
    for i in range(len(nums)):
        for j in range(1 + i, len(nums)):
            if (nums[i] < nums[j]):
                sort = nums[j]
                nums[j] = nums[i]
                nums[i] = sort
    return nums

print(assendingsort(nums))
print(dessendingsort(nums))
