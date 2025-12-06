class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def to_list(self):
        result = []
        n = self
        while n is not None:
            result.append(n.data)
            n = n.next
        return result


def sum_lists_reverse(l1, l2):
    """Sum two lists where digits stored in reverse order. O(n) time and space."""
    dummy = Node(0)
    current = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:
        val1 = l1.data if l1 else 0
        val2 = l2.data if l2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        current.next = Node(digit)
        current = current.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return dummy.next


def sum_lists_forward(l1, l2):
    """Sum two lists where digits stored in forward order. O(n) time and space."""
    # Get lengths
    len1 = get_length(l1)
    len2 = get_length(l2)

    # Pad shorter list
    if len1 < len2:
        l1 = pad_list(l1, len2 - len1)
    else:
        l2 = pad_list(l2, len1 - len2)

    # Add lists recursively
    result = add_lists_helper(l1, l2)

    # Handle carry at front
    if result.carry > 0:
        new_head = Node(result.carry)
        new_head.next = result.node
        return new_head
    return result.node


def get_length(head):
    """Get length of linked list."""
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def pad_list(head, padding):
    """Pad list with zeros at front."""
    for _ in range(padding):
        new_node = Node(0)
        new_node.next = head
        head = new_node
    return head


class PartialSum:
    def __init__(self, node=None, carry=0):
        self.node = node
        self.carry = carry


def add_lists_helper(l1, l2):
    """Recursively add two lists and return PartialSum."""
    if l1 is None and l2 is None:
        return PartialSum()

    # Recurse
    result = add_lists_helper(l1.next, l2.next)

    # Add current digits plus carry
    total = l1.data + l2.data + result.carry
    digit = total % 10
    carry = total // 10

    # Create new node with digit
    new_node = Node(digit)
    new_node.next = result.node

    return PartialSum(new_node, carry)


def create_list(digits):
    """Helper to create linked list from list of digits."""
    if not digits:
        return None
    head = Node(digits[0])
    current = head
    for digit in digits[1:]:
        current.next = Node(digit)
        current = current.next
    return head


if __name__ == "__main__":
    print("Testing sum_lists_reverse (digits in reverse order):")
    print("-" * 60)

    # Example: (7->1->6) + (5->9->2) = 617 + 295 = 912 = (2->1->9)
    l1 = create_list([7, 1, 6])
    l2 = create_list([5, 9, 2])
    print(f"List 1: {l1.to_list()} (represents 617)")
    print(f"List 2: {l2.to_list()} (represents 295)")
    result = sum_lists_reverse(l1, l2)
    print(f"Sum: {result.to_list()} (represents 912)")

    # Test with different lengths
    l1 = create_list([9, 9, 9])
    l2 = create_list([1])
    print(f"\nList 1: {l1.to_list()} (represents 999)")
    print(f"List 2: {l2.to_list()} (represents 1)")
    result = sum_lists_reverse(l1, l2)
    print(f"Sum: {result.to_list()} (represents 1000)")

    # Test with carry
    l1 = create_list([9, 9])
    l2 = create_list([9, 9])
    print(f"\nList 1: {l1.to_list()} (represents 99)")
    print(f"List 2: {l2.to_list()} (represents 99)")
    result = sum_lists_reverse(l1, l2)
    print(f"Sum: {result.to_list()} (represents 198)")

    print("\n" + "=" * 60)
    print("\nTesting sum_lists_forward (digits in forward order):")
    print("-" * 60)

    # Example: (6->1->7) + (2->9->5) = 617 + 295 = 912 = (9->1->2)
    l1 = create_list([6, 1, 7])
    l2 = create_list([2, 9, 5])
    print(f"List 1: {l1.to_list()} (represents 617)")
    print(f"List 2: {l2.to_list()} (represents 295)")
    result = sum_lists_forward(l1, l2)
    print(f"Sum: {result.to_list()} (represents 912)")

    # Test with different lengths
    l1 = create_list([9, 9, 9])
    l2 = create_list([1])
    print(f"\nList 1: {l1.to_list()} (represents 999)")
    print(f"List 2: {l2.to_list()} (represents 1)")
    result = sum_lists_forward(l1, l2)
    print(f"Sum: {result.to_list()} (represents 1000)")

    # Test with carry
    l1 = create_list([9, 9])
    l2 = create_list([9, 9])
    print(f"\nList 1: {l1.to_list()} (represents 99)")
    print(f"List 2: {l2.to_list()} (represents 99)")
    result = sum_lists_forward(l1, l2)
    print(f"Sum: {result.to_list()} (represents 198)")

    # Test with leading carry
    l1 = create_list([5, 0, 0])
    l2 = create_list([5, 0, 0])
    print(f"\nList 1: {l1.to_list()} (represents 500)")
    print(f"List 2: {l2.to_list()} (represents 500)")
    result = sum_lists_forward(l1, l2)
    print(f"Sum: {result.to_list()} (represents 1000)")
