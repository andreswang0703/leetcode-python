from ListNode import ListNode, print_list

def mergeLists(l1, l2):
    """
    No.21 merge two sorted linked lists

    """
    dummy = ListNode(0)
    cur = dummy
    while l1 and l2:
        if l1.val < l2.val:
            cur.next = l1
            l1 = l1.next
        else:
            cur.next = l2
            l2 = l2.next
        cur = cur.next
    cur.next = l1 if l1 else l2
    return dummy.next

def getList():
    l1 = ListNode(1)
    l2 = ListNode(3)
    l3 = ListNode(6)
    l4 = ListNode(2)
    l5 = ListNode(7)
    l6 = ListNode(8)
    l1.next = l2
    l2.next = l3
    l4.next = l5
    l5.next = l6
    return l1, l4

if __name__ == "__main__":
    l1, l2 = getList()
    merged = mergeLists(l1, l2)
    print_list(merged)