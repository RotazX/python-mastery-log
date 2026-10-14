
class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None

    def insert(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

    def traverse(self) -> list[int]:
        result = []
        current = self.head
        while current is not None:
            result.append(current.value)
            current = current.next
        return result

if __name__ == "__main__":
    ll = LinkedList()
    print("Empty list:", ll.traverse())

    ll.insert(3)
    ll.insert(5)
    ll.insert(7)
    print("After inserting 3, 5, 7:", ll.traverse())