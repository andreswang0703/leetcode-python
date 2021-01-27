from ListNode import ListNode

def remove_duplicates_from_sorted_list(head):
    """
    No.83 Remove duplicates from sorted list. (easy)
    Date: 01/26/2021

    Difference between No.82, for duplicated numbers, no need to remove all


    input: 2 -> 1 -> 1 -> 3 -> 3 -> None
    output: 2 -> 1 -> 3 -> None

    time: O(n)
    space: O(1)
    """

    # check head first
    if not head:
        return None

    cur = head
    while cur.next:
        if cur.val == cur.next.val:
            cur.next = cur.next.next
        else:
            cur = cur.next
    return head
