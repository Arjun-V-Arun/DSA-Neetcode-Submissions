# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # [Time Complexity: O(n) | Space Complexity: O(1) since we use pointers]
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        return prev
    
    # # Attempt Recursively [Time Complexity: O(n) | Space Complexity: O(1)]
    # def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    #     if not head:
    #         return None

    #     newHead = head
    #     if head.next:
    #         newHead = self.reverseList(head.next)
    #         head.next.next = head
    #     head.next = None

    #     return newHead

