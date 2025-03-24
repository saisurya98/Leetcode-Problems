class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow,fast algorithm or #floyd cycle finding algorithm
        dummy=ListNode()
        dummy.next=head
        slow,fast=dummy,dummy
        # have two pointers slow,fast move slow by 1x speed, move fast by 2x speed
        while fast is not None and fast.next is not None:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
                return True
        return False
    #TC-O(N)
    #SC-O(1)
