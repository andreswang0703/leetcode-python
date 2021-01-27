from ListNode import ListNode

def remove_duplicates_from_sorted_list_2(head: ListNode) -> ListNode:
    """
    No.82 Remove duplicates from sorted list II. (medium)
    
    input: 1 -> 1 -> 1 -> 2 -> None
    output: 2 -> None
    
    Date: 01/26/2021
    
    time: O(n)
    space: O(1)
    """

    # need to use dummy since the first node could be removed
    dummy = ListNode(0, head)
    prev = dummy
    
    while head:

        # check head.next before accessing
        if head.next and head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            prev.next = head.next
        else:
            prev = prev.next
        
        # move the head to next for both cases
        head = head.next

    return dummy.next

