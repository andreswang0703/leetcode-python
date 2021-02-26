
def checkCycle(head):
    """
    No.141 Linked list cycle

    Return true if linked list has cycle, false otherwise.
    
    """
    s = f = head
    while f and f.next:
        s = s.next
        f = f.next.next

        if f == s:
            return True

    return False
