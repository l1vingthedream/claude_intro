def check_permutation_sort(s1, s2):
    """
    Check if one string is a permutation of the other by sorting.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s1 is a permutation of s2, False otherwise

    Time Complexity: O(n log n)
    Space Complexity: O(n) for sorted copies
    """
    # Different lengths means they can't be permutations
    if len(s1) != len(s2):
        return False

    # Sort both strings and compare
    return sorted(s1) == sorted(s2)


def check_permutation_count(s1, s2):
    """
    Check if one string is a permutation of the other by counting characters.
    Uses a dictionary to count character occurrences.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s1 is a permutation of s2, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n) for character counts
    """
    # Different lengths means they can't be permutations
    if len(s1) != len(s2):
        return False

    # Count characters in first string
    char_count = {}
    for char in s1:
        char_count[char] = char_count.get(char, 0) + 1

    # Decrement counts for second string
    for char in s2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False

    return True


def check_permutation_array(s1, s2):
    """
    Check if one string is a permutation of the other using array for ASCII.
    Assumes ASCII character set (128 characters).

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if s1 is a permutation of s2, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1) - fixed size array of 128
    """
    # Different lengths means they can't be permutations
    if len(s1) != len(s2):
        return False

    # Character count array for ASCII
    char_count = [0] * 128

    # Count characters in first string
    for char in s1:
        char_count[ord(char)] += 1

    # Decrement counts for second string
    for char in s2:
        char_count[ord(char)] -= 1
        if char_count[ord(char)] < 0:
            return False

    return True


if __name__ == "__main__":
    # Test cases: (string1, string2, expected_result)
    test_cases = [
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        ("ab", "ba", True),
        ("abc", "bca", True),
        ("abc", "def", False),
        ("abc", "abcd", False),
        ("listen", "silent", True),
        ("hello", "world", False),
        ("god", "dog", True),
        ("python", "typhon", True),
        ("aabbcc", "abcabc", True),
        ("aabbcc", "abc", False),
        ("racecar", "carrace", True),
        ("test", "best", False),
    ]

    print("Testing check_permutation_sort function:")
    print("-" * 60)
    for s1, s2, expected in test_cases:
        result = check_permutation_sort(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} check_permutation_sort('{s1}', '{s2}'): {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nTesting check_permutation_count function:")
    print("-" * 60)
    for s1, s2, expected in test_cases:
        result = check_permutation_count(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} check_permutation_count('{s1}', '{s2}'): {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nTesting check_permutation_array function:")
    print("-" * 60)
    for s1, s2, expected in test_cases:
        result = check_permutation_array(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} check_permutation_array('{s1}', '{s2}'): {result} (expected: {expected})")
