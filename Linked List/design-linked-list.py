"""
    707. Design Linked List
    Link: https://leetcode.com/problems/design-linked-list/
"""


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return self.value


# Runtime: 249 ms, faster than 72.10% of Python3 online submissions for Design Linked List.
class MyLinkedList:

    def __str__(self) -> str:
        tmp = []
        node = self.head
        while node is not None:
            tmp.append((node.value))
            node = node.next
        return str(tmp)

    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        counter = 0
        curr = self.head
        while curr:
            if counter == index:
                return curr.value
            curr = curr.next
            counter += 1
        else:
            return -1

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head)
        self.head = node

    def addAtTail(self, val: int) -> None:
        if self.head == None:
            self.head = Node(val)
            return None
        prev = None
        curr = self.head
        while curr:
            prev = curr
            curr = curr.next
        prev.next = Node(val)

    def addAtIndex(self, index: int, value: int) -> None:
        # if self.head == None:
        #     self.head = Node(value)
        #     return
        node = Node(value)

        # Case 1: Insertion at beginning
        if index == 0:
            self.addAtHead(value)
            return None

        # Case 2:
        # Insertion in between
        counter = 1
        tmp = self.head
        while tmp:
            if counter == index:
                node.next = tmp.next
                tmp.next = node
                return None
            tmp = tmp.next
            counter += 1

        # Case 3:
        # Insertion at end
        # else:
        #     # If index is greater than length of List
        #     self.addAtTail(value)

    def deleteAtIndex(self, index: int) -> None:
        if self.head == None:
            return

        # Case 1: Deletion at beginning
        if index == 0:
            self.head = self.head.next
            return

        # Case 2: Deletion after index == 0
        counter = 1
        curr = self.head.next
        prev = self.head
        while curr:
            if counter == index:
                prev.next = curr.next
                return
            else:
                prev = curr
                curr = curr.next
            counter += 1


# ["MyLinkedList","addAtHead","get","addAtHead","addAtHead","deleteAtIndex","addAtHead","get","get","get","addAtHead","deleteAtIndex"]
# [[],[4],[1],[1],[5],[3],[7],[3],[3],[3],[1],[4]]
obj = MyLinkedList()
print(obj.addAtHead(4))
print(obj.get(1))
print(obj.addAtHead(1))
print(obj.addAtHead(5))
print(obj.deleteAtIndex(3))
print(obj.addAtHead(7))
print(obj.get(3))
print(obj.get(3))
print(obj.get(3))
print(obj.addAtHead(3))
print(obj.deleteAtIndex(4))
# print(obj)