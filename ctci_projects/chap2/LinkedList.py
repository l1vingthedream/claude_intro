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

    def remove_dupes(self):
        """Remove duplicates using hash set. O(n) time, O(n) space."""
        seen = set()
        n = self
        seen.add(n.data)

        while n.next is not None:
            if n.next.data in seen:
                n.next = n.next.next
            else:
                seen.add(n.next.data)
                n = n.next

    def remove_dupes_no_buffer(self):
        """Remove duplicates without buffer. O(n²) time, O(1) space."""
        current = self

        while current is not None:
            runner = current
            while runner.next is not None:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            current = current.next

    def return_kth_to_last(self, k):
        """Find kth to last element using two pointers. O(n) time, O(1) space."""
        p1 = self
        p2 = self

        # Move p1 k nodes ahead
        for i in range(k):
            if p1 is None:
                return None
            p1 = p1.next

        # Move both pointers until p1 reaches end
        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2

    def return_kth_to_last_recursive(self, k):
        """Find kth to last element recursively. O(n) time, O(n) space."""
        return self._kth_helper(k)[1]

    def _kth_helper(self, k):
        """Helper: returns (index from end, node)."""
        if self.next is None:
            return (1, None if k != 1 else self)

        idx, node = self.next._kth_helper(k)
        idx += 1

        if idx == k:
            return (idx, self)
        return (idx, node)

    def delete_middle_node(self):
        """Delete this node (must not be first or last). O(1) time and space."""
        if self.next is None:
            return False

        # Copy next node's data into current node
        self.data = self.next.data
        # Skip next node
        self.next = self.next.next
        return True

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

    print("\n" + "=" * 60)
    print("\nTesting remove_dupes:")
    print("-" * 60)

    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    head.append_to_tail(2)
    head.append_to_tail(1)
    head.append_to_tail(4)
    print(f"Before: {head.to_list()}")
    head.remove_dupes()
    print(f"After remove_dupes: {head.to_list()}")

    head = Node(5)
    head.append_to_tail(5)
    head.append_to_tail(5)
    head.append_to_tail(5)
    print(f"\nBefore: {head.to_list()}")
    head.remove_dupes()
    print(f"After remove_dupes: {head.to_list()}")

    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    print(f"\nBefore (no dupes): {head.to_list()}")
    head.remove_dupes()
    print(f"After remove_dupes: {head.to_list()}")

    print("\n" + "=" * 60)
    print("\nTesting remove_dupes_no_buffer:")
    print("-" * 60)

    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    head.append_to_tail(2)
    head.append_to_tail(1)
    head.append_to_tail(4)
    print(f"Before: {head.to_list()}")
    head.remove_dupes_no_buffer()
    print(f"After remove_dupes_no_buffer: {head.to_list()}")

    head = Node(5)
    head.append_to_tail(5)
    head.append_to_tail(5)
    head.append_to_tail(5)
    print(f"\nBefore: {head.to_list()}")
    head.remove_dupes_no_buffer()
    print(f"After remove_dupes_no_buffer: {head.to_list()}")

    head = Node(7)
    head.append_to_tail(8)
    head.append_to_tail(7)
    head.append_to_tail(9)
    head.append_to_tail(8)
    head.append_to_tail(7)
    print(f"\nBefore: {head.to_list()}")
    head.remove_dupes_no_buffer()
    print(f"After remove_dupes_no_buffer: {head.to_list()}")

    print("\n" + "=" * 60)
    print("\nTesting return_kth_to_last:")
    print("-" * 60)

    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    head.append_to_tail(4)
    head.append_to_tail(5)
    print(f"List: {head.to_list()}")

    for k in range(6):
        result = head.return_kth_to_last(k)
        print(f"k={k}: {result.data if result else None}")

    print("\n" + "=" * 60)
    print("\nTesting return_kth_to_last_recursive:")
    print("-" * 60)

    head = Node(10)
    head.append_to_tail(20)
    head.append_to_tail(30)
    head.append_to_tail(40)
    head.append_to_tail(50)
    print(f"List: {head.to_list()}")

    for k in range(6):
        result = head.return_kth_to_last_recursive(k)
        print(f"k={k}: {result.data if result else None}")

    print("\n" + "=" * 60)
    print("\nTesting delete_middle_node:")
    print("-" * 60)

    # Create list a->b->c->d->e->f
    head = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')
    head.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = f

    print(f"Before: {head.to_list()}")
    c.delete_middle_node()
    print(f"After delete_middle_node on 'c': {head.to_list()}")

    # Delete another middle node (get fresh reference)
    middle = b.next  # This is now the node with 'd' data
    print(f"\nBefore: {head.to_list()}")
    middle.delete_middle_node()
    print(f"After delete_middle_node on node with 'd': {head.to_list()}")

    # Test with numbers
    head = Node(1)
    head.append_to_tail(2)
    head.append_to_tail(3)
    head.append_to_tail(4)
    head.append_to_tail(5)

    # Get reference to node with value 3
    node_3 = head.next.next
    print(f"\nBefore: {head.to_list()}")
    node_3.delete_middle_node()
    print(f"After delete_middle_node on node with value 3: {head.to_list()}")
