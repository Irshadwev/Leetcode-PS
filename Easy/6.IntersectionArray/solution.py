'''
349. Intersection of Two Arrays

Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
Explanation: [4,9] is also accepted.

'''

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
result = []
for i in range(len(nums1)):
    for j in range(len(nums2)):
        if (nums1[i] == nums2[j] and nums1[i] not in result):
                result.append(nums1[i])
print(result)