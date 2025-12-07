class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_loop_start(head):
    """Find start of loop using Floyd's algorithm. O(n) time, O(1) space."""
    if not head:
        return None

    slow = fast = head

    # Find meeting point
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    # No loop
    if not fast or not fast.next:
        return None

    # Move slow to head, advance both at same pace
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next

    return fast


def find_loop_start_hash(head):
    """Find loop start using hash set. O(n) time, O(n) space."""
    seen = set()
    current = head

    while current:
        if current in seen:
            return current
        seen.add(current)
        current = current.next

    return None


def create_loop_list(values, loop_index):
    """Helper to create linked list with loop at given index."""
    if not values:
        return None

    nodes = [Node(val) for val in values]

    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    # Create loop
    if loop_index is not None and 0 <= loop_index < len(nodes):
        nodes[-1].next = nodes[loop_index]

    return nodes[0]


def get_loop_sequence(head, max_nodes=20):
    """Helper to show list structure including loop."""
    if not head:
        return []

    visited = {}
    result = []
    current = head
    index = 0

    while current and index < max_nodes:
        if current in visited:
            result.append(f"{current.data}(loop to index {visited[current]})")
            break
        visited[current] = index
        result.append(current.data)
        current = current.next
        index += 1

    return result


if __name__ == "__main__":
    print("Testing find_loop_start (Floyd's algorithm):")
    print("-" * 60)

    # Example: A -> B -> C -> D -> E -> C
    head = create_loop_list(['A', 'B', 'C', 'D', 'E'], 2)
    print(f"List: {get_loop_sequence(head)}")
    result = find_loop_start(head)
    print(f"Loop start: {result.data if result else None}")

    # Loop at head
    head = create_loop_list([1, 2, 3, 4], 0)
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start(head)
    print(f"Loop start: {result.data if result else None}")

    # Loop at end (self-loop)
    head = create_loop_list([5, 6, 7], 2)
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start(head)
    print(f"Loop start: {result.data if result else None}")

    # No loop
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start(head)
    print(f"Loop start: {result.data if result else None}")

    # Single node with self-loop
    head = Node(9)
    head.next = head
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start(head)
    print(f"Loop start: {result.data if result else None}")

    print("\n" + "=" * 60)
    print("\nTesting find_loop_start_hash:")
    print("-" * 60)

    # Example: A -> B -> C -> D -> E -> C
    head = create_loop_list(['A', 'B', 'C', 'D', 'E'], 2)
    print(f"List: {get_loop_sequence(head)}")
    result = find_loop_start_hash(head)
    print(f"Loop start: {result.data if result else None}")

    # Loop in middle
    head = create_loop_list([10, 20, 30, 40, 50], 3)
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start_hash(head)
    print(f"Loop start: {result.data if result else None}")

    # No loop
    head = Node(100)
    head.next = Node(200)
    print(f"\nList: {get_loop_sequence(head)}")
    result = find_loop_start_hash(head)
    print(f"Loop start: {result.data if result else None}")

    print("\n" + "=" * 60)
    print("\nTest cases comparison:")
    print("-" * 60)

    test_cases = [
        (['A', 'B', 'C', 'D', 'E'], 2, 'C'),
        ([1, 2, 3, 4, 5], 0, 1),
        ([7, 8, 9], 2, 9),
        ([5], 0, 5),
    ]

    for values, loop_idx, expected in test_cases:
        head = create_loop_list(values, loop_idx)
        result1 = find_loop_start(head)
        result2 = find_loop_start_hash(head)

        match1 = "✓" if (result1 and result1.data == expected) else "✗"
        match2 = "✓" if (result2 and result2.data == expected) else "✗"

        print(f"{match1} Floyd: {values} loop at {loop_idx} -> {result1.data if result1 else None}")
        print(f"{match2} Hash:  {values} loop at {loop_idx} -> {result2.data if result2 else None}")
