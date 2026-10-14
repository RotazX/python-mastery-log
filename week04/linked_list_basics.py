
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = Node(value)

    def traverse(self):
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