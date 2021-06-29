# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return
        ans = lists[0]
        for i in range(len(lists) - 1):
            ans = self.mergeTwoLists(ans, lists[i+1])
        return ans

    def mergeTwoLists(self, head1, head2):
        protect = ListNode(-1)
        ans = protect
        while head1 and head2:
            if head1.val >= head2.val:
                ans.next = head2
                head2 = head2.next
                ans = ans.next
            else:
                ans.next = head1
                head1 = head1.next
                ans = ans.next
        if head2 is None:
            ans.next = head1
        else:
            ans.next = head2
        return protect.next