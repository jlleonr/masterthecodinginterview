"""
Input = 1 - 2 - 3 - 4 - 5 - null
Output = 5 - 4 - 3 - 2 - 1 - null
"""


class LinkedNode:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None


def reverseLinkedList(node: LinkedNode) -> LinkedNode:

    currentNode: LinkedNode = node
    prev: LinkedNode = None

    while currentNode:
        next: LinkedNode = currentNode.next
        currentNode.next = prev
        prev = currentNode
        currentNode = next

    return prev


def reverseLinkedListRecursive(head: LinkedNode,
                               prev: LinkedNode = None) -> LinkedNode:

    if head is None:
        return prev

    next: LinkedNode = head.next
    head.next = prev
    return reverseLinkedListRecursive(next, head)


def printLinkedNode(head: LinkedNode) -> None:

    while head:
        print(head.data)
        head = head.next


root: LinkedNode = LinkedNode(1)
root.next = LinkedNode(2)
root.next.next = LinkedNode(3)
root.next.next.next = LinkedNode(4)
root.next.next.next.next = None

res = reverseLinkedListRecursive(root)
printLinkedNode(res)
# printLinkedNode(root)
