'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
example:
 Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].'''

#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_indices={}
        
        for i,num in enumerate(nums):
            difference=target-num
            if difference in num_indices:
                return [num_indices[difference],i]
            num_indices[num]=i
        
        
        
  

        


# In[ ]:




