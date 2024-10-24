class SinglyNode:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return str(self.val)


head = SinglyNode(1)
a = SinglyNode(3)
b = SinglyNode(5)
c = SinglyNode(7)

# print(head)

head.next = a
a.next = b
b.next = c

'''
Traversing through a linked list
'''

# curr = head
# while curr:
#     print(curr)
#     curr = curr.next

"""
Displaying the elements in the linked list
"""

# def Display(head):
#     l = []
#     curr = head
#     while curr:
#         l.append(str(curr.val))
#         curr = curr.next
#     print(' -> '.join(l))


# Display((head))

"""
Searching an elements in a linked list
"""


def search(head, value):
    curr = head
    while curr:
        if value == curr.val:
            return True
        curr = curr.next
    return False


print(search(head, 1))
