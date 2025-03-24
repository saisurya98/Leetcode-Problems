# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # get the count of linkedlist
        count = 0
        curr = head
        while curr is not None:
            count += 1
            curr = curr.next
        new_curr = head
        # reverse count
        forward_count = count - n
        # create a dummy linkedlist point to a dummy node
        dummy = ListNode()
        # make sure dummy points to head of given linkedlist
        dummy.next = head
        prev = dummy
        iterable_count = 0
        while new_curr is not None:
            # check if counts are matching if they are just skip it, else u can point to it
            if iterable_count == forward_count:
                prev.next = new_curr.next
                new_curr = new_curr.next
                iterable_count += 1
            else:
                prev.next = new_curr
                new_curr = new_curr.next
                prev = prev.next
                iterable_count += 1
        # return the dummy linkedlist
        return dummy.next

        # TC-O(N)
        #SC-O(1)


