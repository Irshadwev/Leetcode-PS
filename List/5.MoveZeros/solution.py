'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 
'''

nums = [0,1,0,3,12]
for i in range(len(nums)):
    for j in range(1+i, len(nums)):
        if(nums[i] == 0):
            move_zero = nums[j]
            nums[j] = nums[i]
            nums[i] = move_zero
print(nums)