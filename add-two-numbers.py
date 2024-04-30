'''You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.'''




#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummyhead=ListNode(0)
    carry=0
    curr=dummyhead
    while l1 or l2:
        if l1:
            l1_val=l1.val
        else:
            l1_val=0
        if l2:
            l2_val=l2.val
        else:
            l2_val=0
        sum=l1_val+l2_val+carry
        curr.next=ListNode(sum%10)
        curr=curr.next
        carry=sum//10
        if l1:
            l1=l1.next
        if l2:
            l2=l2.next
    if carry:
        curr.next=ListNode(carry)
    return dummyhead.next
        


# In[ ]:




