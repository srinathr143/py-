class DoubleNode:

    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return str(self.val)


head = tail = DoubleNode(1)


# print(tail)

def display(head):
    l = []
    curr = head
    while curr:
        l.append((str(curr.val)))
        curr = curr.next
    print(' <-> '.join(l))


# display(head)

"""
Inserting a value at the beginning node

"""


def insert_at_beginning(head, tail, val):
    new_node = DoubleNode(val, next=head)
    head.prev = new_node
    return new_node, tail


head, tail = insert_at_beginning(head, tail, 3)
head, tail = insert_at_beginning(head, tail, 4)



# display(head)

def insert_at_end(head, tail, val):
    new_node = DoubleNode(val, prev=tail)
    tail.next = new_node
    return head, new_node


head, tail = insert_at_end(head, tail, 7)
head, tail = insert_at_end(head, tail, 9)

display(head)
