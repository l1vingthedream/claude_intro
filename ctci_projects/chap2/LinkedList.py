class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append_to_tail(self, data):
        """Append node with given data to end of list."""
        end = Node(data)
        n = self
        while n.next is not None:
            n = n.next
        n.next = end

    def print_list(self):
        """Print all nodes in the list."""
        values = []
        n = self
        while n is not None:
            values.append(str(n.data))
            n = n.next
        print(" -> ".join(values))

    def to_list(self):
        """Convert linked list to Python list."""
        result = []
        n = self
        while n is not None:
            result.append(n.data)
            n = n.next
        return result


if __name__ == "__main__":
    print("Testing LinkedList Node class:")
    print("-" * 60)

    # Create list: 1
    head = Node(1)
    print(f"Created: {head.to_list()}")

    # Append 2, 3, 4
    head.append_to_tail(2)
    print(f"After append 2: {head.to_list()}")

    head.append_to_tail(3)
    print(f"After append 3: {head.to_list()}")

    head.append_to_tail(4)
    print(f"After append 4: {head.to_list()}")

    print("\nFinal list:")
    head.print_list()

    print("\n" + "=" * 60)
    print("\nTest multiple lists:")

    list1 = Node(5)
    list1.append_to_tail(10)
    list1.append_to_tail(15)
    print(f"List 1: {list1.to_list()}")

    list2 = Node(100)
    list2.append_to_tail(200)
    print(f"List 2: {list2.to_list()}")
