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


def is_palindrome_stack(head):
    """Check if palindrome using stack. O(n) time and space."""
    if not head:
        return True

    # Find length
    length = 0
    n = head
    while n:
        length += 1
        n = n.next

    # Push first half onto stack
    stack = []
    n = head
    for i in range(length // 2):
        stack.append(n.data)
        n = n.next

    # Skip middle element if odd length
    if length % 2 == 1:
        n = n.next

    # Compare second half with stack
    while n:
        if n.data != stack.pop():
            return False
        n = n.next

    return True


def is_palindrome_reverse(head):
    """Check if palindrome by reversing list. O(n) time, O(n) space."""
    if not head:
        return True

    # Copy list
    values = []
    n = head
    while n:
        values.append(n.data)
        n = n.next

    # Compare with reverse
    return values == values[::-1]


def is_palindrome_runner(head):
    """Check if palindrome using slow/fast runner. O(n) time, O(n) space."""
    if not head:
        return True

    slow = fast = head
    stack = []

    # Push first half onto stack while finding middle
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    # Skip middle if odd length
    if fast:
        slow = slow.next

    # Compare second half with stack
    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True


class Result:
    def __init__(self, node, is_palindrome):
        self.node = node
        self.is_palindrome = is_palindrome


def is_palindrome_recursive(head):
    """Check if palindrome recursively. O(n) time and space."""
    length = get_length(head)
    result = check_palindrome(head, length)
    return result.is_palindrome


def get_length(head):
    length = 0
    while head:
        length += 1
        head = head.next
    return length


def check_palindrome(head, length):
    """Returns Result with corresponding node and palindrome status."""
    if length == 0:
        return Result(head, True)
    if length == 1:
        return Result(head.next, True)

    # Recurse on sublist
    result = check_palindrome(head.next, length - 2)

    # Check if still palindrome and compare nodes
    if not result.is_palindrome or result.node is None:
        return result

    # Compare head with corresponding node from end
    is_equal = head.data == result.node.data

    # Return next node and updated palindrome status
    return Result(result.node.next, is_equal)


def create_list(values):
    """Helper to create linked list from list of values."""
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head


if __name__ == "__main__":
    test_cases = [
        (['A', 'B', 'C', 'B', 'A'], True),
        (['A', 'B', 'C'], False),
        (['A'], True),
        (['A', 'A'], True),
        (['A', 'B'], False),
        ([1, 2, 3, 2, 1], True),
        ([1, 2, 2, 1], True),
        ([1, 2, 3, 4], False),
        ([], True),
        (['R', 'A', 'C', 'E', 'C', 'A', 'R'], True),
        ([1, 2, 1, 2], False),
    ]

    print("Testing is_palindrome_stack:")
    print("-" * 60)
    for values, expected in test_cases:
        head = create_list(values)
        result = is_palindrome_stack(head)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values}: {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nTesting is_palindrome_reverse:")
    print("-" * 60)
    for values, expected in test_cases:
        head = create_list(values)
        result = is_palindrome_reverse(head)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values}: {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nTesting is_palindrome_runner:")
    print("-" * 60)
    for values, expected in test_cases:
        head = create_list(values)
        result = is_palindrome_runner(head)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values}: {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nTesting is_palindrome_recursive:")
    print("-" * 60)
    for values, expected in test_cases:
        head = create_list(values)
        result = is_palindrome_recursive(head)
        status = "✓" if result == expected else "✗"
        print(f"{status} {values}: {result} (expected: {expected})")
