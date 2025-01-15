class Solution:
    def linkdelete(self, head, n, m):
        curr = head
        
        while curr:
            for _ in range(m):
                if curr is None:
                    return head  
                prev = curr
                curr = curr.next

            for _ in range(n):
                if curr is None:
                    break  
                prev.next = curr.next
                curr = curr.next
                
        return head