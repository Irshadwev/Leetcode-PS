nums = [3, 2, 4]
def twosum(nums):
    target = 6
    lenght = len(nums)

    for i in range(lenght):
            for j in range(i+1, lenght):

                if (nums[i] + nums[j] == target):

                    return [i,j]

print(twosum(nums))