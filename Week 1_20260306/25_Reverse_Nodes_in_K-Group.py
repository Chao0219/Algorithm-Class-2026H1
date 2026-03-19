# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        former = []
        inverse = []
        
        # 求listnode長度
        length = 0
        pending = 0
        temp_head = head
        while temp_head:
            length += 1
            temp_head = temp_head.next
        pending = length//k  #要反置幾次
        
        # 讀出並反置
        for i in range(pending):
            for j in range(k):
                former.append(head.val)
                head = head.next
            for j in range(k):
                inverse.append(former[k-j-1])
            former = []
        while head:
            inverse.append(head.val)
            head = head.next

        #創立 Listnode 因為要輸出成這個格式
        dummy = ListNode(0)
        curr = dummy
        for val in inverse:
            curr.next = ListNode(val) 
            curr = curr.next
        return dummy.next     
        
 