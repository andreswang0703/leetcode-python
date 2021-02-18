
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def print_list(head):
    s = ""
    while head:
        s += str(head.val)
        s += "  "
        head = head.next
    print(s)