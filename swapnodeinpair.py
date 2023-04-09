from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        tmp_two = []
        tmp_head = None
        while head.next is not None:
            tmp_two.insert(0, head.val)
            if len(tmp_two) == 2:
                if tmp_head is None:
                    tmp_head = tmp_tail = ListNode(tmp_two[0])
                    tmp_tail.next = ListNode(tmp_two[1])
                    tmp_tail = tmp_tail.next
                else:
                    for value in tmp_two:
                        tmp_tail.next = ListNode(value)
                        tmp_tail = tmp_tail.next
                tmp_two = []
            head = head.next
        tmp_two.insert(0, head.val)
        if tmp_head is None:
            if len(tmp_two) == 2:
                tmp_head = tmp_tail = ListNode(tmp_two[0])
                tmp_tail.next = ListNode(tmp_two[1])
                return tmp_head
            else:
                return head
        for value in tmp_two:
            tmp_tail.next = ListNode(value)
            tmp_tail = tmp_tail.next
        return tmp_head


def make_listnode(l:List) -> ListNode:
    for i, value in enumerate(l):
        if i == 0:
            tail = head = ListNode(value)
        else:
            tail.next = ListNode(value)
            tail = tail.next
    return head

sol = Solution()
a = [1, 2]
a_nodes = make_listnode(a)
hoge = sol.swapPairs(a_nodes)
while a_nodes.next is not None:
    print(a_nodes.val)
    a_nodes = a_nodes.next
print(a_nodes.val)

while hoge.next is not None:
    print(hoge.val)
    hoge = hoge.next
print(hoge.val)