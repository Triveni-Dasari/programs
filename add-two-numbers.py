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




