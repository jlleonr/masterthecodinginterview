"""
Zip two linked lists together
"""


from typing import List


class LinkedList:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

def insertNodes(nodes: List[int], head: LinkedList) -> LinkedList:

    if nodes is None:
        return None

    for node in nodes:
        head.next = LinkedList(node)
        head = head.next

    return head


def printNodes(head: LinkedList) -> None:
     while head:
         print(head.data)
         head = head.next


def zipLinkedList(head1: LinkedList, head2: LinkedList) -> None:

    tail: LinkedList = head1
    current1: LinkedList = head1.next
    current2: LinkedList = head2
    count: int = 0

    while current1 and current2:

        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next

        tail = tail.next
        count += 1

    if current1 is not None:
        tail.next = current1
    if current2 is not None:
        tail.next = current2

    return head1


"""Tests"""
head1: LinkedList = LinkedList(1)
nodes: List[int] = [2,3,4,5]

head2: LinkedList = LinkedList(6)
head2.next = LinkedList(7)

insertNodes(nodes=nodes, head=head1)
head: LinkedList = zipLinkedList(head1, head2)
printNodes(head=head)


