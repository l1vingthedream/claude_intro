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

    def delete_node(self, data):
        """Delete first node with given data. Returns new head."""
        n = self

        # If head node contains the data
        if n.data == data:
            return n.next

        # Search for node to delete
        while n.next is not None:
            if n.next.data == data:
                n.next = n.next.next  # Skip the node (sets to None if last)
                return self
            n = n.next

        return self  # Data not found

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
    print("\nTesting delete_node:")
    print("-" * 60)

    # Delete middle node
    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    head.append_to_tail(4)
    print(f"Before delete: {head.to_list()}")
    head = head.delete_node(3)
    print(f"After delete 3: {head.to_list()}")

    # Delete last node
    head = head.delete_node(4)
    print(f"After delete 4 (last): {head.to_list()}")

    # Delete first node
    head = head.delete_node(1)
    print(f"After delete 1 (head): {head.to_list()}")

    # Delete non-existent
    head = head.delete_node(99)
    print(f"After delete 99 (not found): {head.to_list()}")

    # Delete only remaining node
    head = head.delete_node(2)
    print(f"After delete 2 (only node): {head}")

    print("\n" + "=" * 60)
    print("\nTest multiple deletes:")

    head = Node(10)
    head.append_to_tail(20)
    head.append_to_tail(30)
    head.append_to_tail(40)
    head.append_to_tail(50)
    print(f"Start: {head.to_list()}")
    head = head.delete_node(30)
    print(f"Delete 30: {head.to_list()}")
    head = head.delete_node(10)
    print(f"Delete 10: {head.to_list()}")
    head = head.delete_node(50)
    print(f"Delete 50: {head.to_list()}")
