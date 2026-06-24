'''
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
 
Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
'''

s = "anagram"
t = "nagaram"


def isanagram(s, t):
    if len(s) == len(t):
        sourcefrequency = {}
        targetfrequency = {}

        for i in range(len(s)):
            sourcefrequency[s[i]] = sourcefrequency.get(s[i], 0) + 1

        for j in range(len(t)):
            targetfrequency[t[j]] = targetfrequency.get(t[j], 0) + 1

        if(sourcefrequency == targetfrequency):
            return True
        else: 
            return False
        
    else: 
        return False


a = isanagram(s, t)
print(a)