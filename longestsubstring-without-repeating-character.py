'''Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.'''




    
#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d={}
        res=0
        i=0
        for j in range(0,len(s)):
            if s[j] in d:
                i=max(i,(d[s[j]]+1))
            res=max(res,(j-i+1))
            d[s[j]]=j
        return res
        


# In[ ]:




