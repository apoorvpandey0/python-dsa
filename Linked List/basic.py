from typing import List


class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value) + '->' + str(self.next)


class LinkedList:

    def __init__(self, values=None) -> None:
        if isinstance(values, Node):
            self.head = values
        elif isinstance(values, list):
            self._fromList(values)

    def __str__(self) -> str:
        tmp = []
        node = self.head
        while node is not None:
            tmp.append((node.value))
            node = node.next
        return str(tmp)

    def _fromList(self, values) -> None:
        if not values:
            raise Exception('Empty List not allowed')
        self.head = Node(values.pop(0))
        prev = self.head
        for ele in values:
            curr = Node(value=ele)
            prev.next = curr
            prev = curr

    def reverse(self) -> None:
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def add_end(self, value) -> None:
        node = Node(value)
        tmp = self.head
        while tmp.next != None:
            tmp = tmp.next
        else:
            tmp.next = node

    def add_first(self, value) -> None:
        node = Node(value)
        node.next = self.head
        self.head = node

    def insert(self, value, index) -> None:
        node = Node(value)

        # Error handling
        if self.head is None:
            raise Exception("List is empty")

        # Case 1: Insertion at beginning
        if index == 0:
            self.add_first(value)
            return

        # Case 2:
        # Insertion in between
        counter = 1
        tmp = self.head
        while tmp:
            if counter == index:
                node.next = tmp.next
                tmp.next = node
                return
            tmp = tmp.next
            counter += 1

        # Case 3:
        # Insertion at end
        else:
            # If index is greater than length of List
            self.add_end(value)

    def pop(self, index):
        if self.head == None:
            raise Exception("Cannot pop empty linked list")

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

    def get(self, index: int) -> int:
        counter = 0
        curr = self.head
        while curr:
            if counter == index:
                return curr
            curr = curr.next
            counter += 1

    # Runtime: 76 ms, faster than 58.54% of Python3 online submissions for Remove Linked List Elements.
    def removeAll(self, val: int):
        if self.head == None:
            return None
        while self.head and self.head.value == val:
            self.head = self.head.next
        tmp = self.head
        prev = Node()
        while tmp is not None:
            if tmp.value == val and tmp != None:
                prev.next = tmp.next
            else:
                prev = tmp
            tmp = tmp.next
        return self.head


if __name__ == "__main__":
    # c = LinkedList(values=[6, 6, 6, 1, 2, 6, 6, 6, 3, 4, 5, 6, 6, 6])
    # c.removeAll(6)
    # print(c)
    c = LinkedList(values=[6, 6, 6])
    c.removeAll(6)
    print(c)
    # first = Node(value=100)
    # a = LinkedList(first)
    # a.add_end(300)
    # a.add_end(value=400)
    # a.insert(200, 1)
    # a.insert(0, 0)
    # a.insert(0, 4)
    # print(a)
    # b = LinkedList(values=[1, 2, 3, 4, 5])
    # b.insert(10, 2)
    # print(a)
    # b.reverse()
    # print(b)
    # b.pop(0)
    # b.pop(6)
    # b.pop(0)
    # print(b)
