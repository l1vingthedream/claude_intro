class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_intersection_hash(head1, head2):
    """Find intersection using hash set. O(m+n) time, O(m) space."""
    if not head1 or not head2:
        return None

    visited = set()
    current = head1

    # Add all nodes from first list to set
    while current:
        visited.add(current)
        current = current.next

    # Check second list for intersection
    current = head2
    while current:
        if current in visited:
            return current
        current = current.next

    return None


def find_intersection_aligned(head1, head2):
    """Find intersection by aligning lists. O(m+n) time, O(1) space."""
    if not head1 or not head2:
        return None

    # Get lengths and tail nodes
    len1, tail1 = get_length_and_tail(head1)
    len2, tail2 = get_length_and_tail(head2)

    # If tails differ, no intersection
    if tail1 != tail2:
        return None

    # Align lists to same starting position
    shorter = head1 if len1 < len2 else head2
    longer = head2 if len1 < len2 else head1
    diff = abs(len1 - len2)

    # Advance longer list
    for _ in range(diff):
        longer = longer.next

    # Move both until intersection
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next

    return shorter


def get_length_and_tail(head):
    """Get length and tail node of list."""
    if not head:
        return 0, None

    length = 0
    current = head
    while current:
        length += 1
        if not current.next:
            return length, current
        current = current.next

    return length, None


def get_values(head, max_nodes=15):
    """Helper to get values from list (for display)."""
    values = []
    current = head
    count = 0

    while current and count < max_nodes:
        values.append(current.data)
        current = current.next
        count += 1

    if current:
        values.append('...')
    return values


if __name__ == "__main__":
    print("Testing find_intersection_hash:")
    print("-" * 60)

    # Test 1: Lists intersect at node with value 3
    # List 1: 1 -> 2 -> 3 -> 4 -> 5
    # List 2: 9 -> 8 -> 3 -> 4 -> 5 (same 3, 4, 5 nodes)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node3.next = node4
    node4.next = node5

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = node3

    head2 = Node(9)
    head2.next = Node(8)
    head2.next.next = node3

    print(f"List 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_hash(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: 3")

    # Test 2: No intersection
    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)

    head2 = Node(4)
    head2.next = Node(5)

    print(f"\nList 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_hash(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: None")

    # Test 3: Intersection at head of shorter list
    shared = Node(7)
    shared.next = Node(8)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = shared

    head2 = shared

    print(f"\nList 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_hash(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: 7")

    print("\n" + "=" * 60)
    print("\nTesting find_intersection_aligned:")
    print("-" * 60)

    # Test 1: Lists intersect at node with value 3
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node3.next = node4
    node4.next = node5

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = node3

    head2 = Node(9)
    head2.next = Node(8)
    head2.next.next = node3

    print(f"List 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_aligned(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: 3")

    # Test 2: Different lengths, intersect near end
    nodeX = Node('X')
    nodeY = Node('Y')
    nodeZ = Node('Z')
    nodeX.next = nodeY
    nodeY.next = nodeZ

    head1 = Node('A')
    head1.next = Node('B')
    head1.next.next = Node('C')
    head1.next.next.next = Node('D')
    head1.next.next.next.next = nodeX

    head2 = Node('E')
    head2.next = nodeX

    print(f"\nList 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_aligned(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: X")

    # Test 3: No intersection
    head1 = Node(10)
    head1.next = Node(20)

    head2 = Node(30)
    head2.next = Node(40)

    print(f"\nList 1: {get_values(head1)}")
    print(f"List 2: {get_values(head2)}")
    result = find_intersection_aligned(head1, head2)
    print(f"Intersection: {result.data if result else None}")
    print(f"Expected: None")

    print("\n" + "=" * 60)
    print("\nComparison test:")
    print("-" * 60)

    # Create intersection at node 100
    shared = Node(100)
    shared.next = Node(200)
    shared.next.next = Node(300)

    head1 = Node(1)
    head1.next = Node(2)
    head1.next.next = Node(3)
    head1.next.next.next = shared

    head2 = Node(50)
    head2.next = shared

    result_hash = find_intersection_hash(head1, head2)
    result_aligned = find_intersection_aligned(head1, head2)

    match = "✓" if result_hash == result_aligned else "✗"
    print(f"{match} Hash result: {result_hash.data if result_hash else None}")
    print(f"{match} Aligned result: {result_aligned.data if result_aligned else None}")
    print(f"Both methods agree: {result_hash == result_aligned}")
