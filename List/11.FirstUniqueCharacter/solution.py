'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

Example 1:
Input: s = "leetcode"
Output: 0

Explanation:
The character 'l' at index 0 is the first character that does not occur at any other index.

Example 2:
Input: s = "loveleetcode"
Output: 2

Example 3:
Input: s = "aabb"
Output: -1

Constraints:
1 <= s.length <= 105
s consists of only lowercase English letters.
'''

s = "loveleetcode"

def firstUniqChar(s):
    for i in range(len(s)):
        count = 0
        for j in range(len(s)):
            if (s[i] == s[j]):
                count += 1
        if (count == 1):
            result = i
            break
        else:
            result = -1
    return result

print(firstUniqChar(s))
                