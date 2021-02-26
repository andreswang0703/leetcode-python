
def findCycleStart(head):
    """
    No.142 Linked list cycle II.

    Find the start of the cycle. If there's no cycle return None.

    Floyd's tortoise and hare algorithm for cycle detection.
    """
    s = f = head
    while f and f.next:
        s = s.next
        f = f.next.next
        if s == f:
            break
    
    if not f or not f.next:
        return None
    
    s = head
    while s != f:
        s = s.next
        f = f.next
    return s