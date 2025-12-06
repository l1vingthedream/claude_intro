def is_unique(s):
    """
    Determines if a string has all unique characters.
    Uses nested loops - no additional data structures.

    Args:
        s: String to check

    Returns:
        True if all characters are unique, False otherwise

    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    # Check each character against all subsequent characters
    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True


def is_unique_optimized(s):
    """
    Optimized version using bit manipulation for ASCII strings.
    Assumes lowercase letters a-z only.
    Uses an integer as a bit vector - technically not an "additional data structure".

    Args:
        s: String to check (lowercase letters only)

    Returns:
        True if all characters are unique, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        # Check if bit at position val is already set
        if (checker & (1 << val)) > 0:
            return False
        # Set bit at position val
        checker |= (1 << val)
    return True


if __name__ == "__main__":
    # Test cases
    test_strings = [
        ("", True),
        ("a", True),
        ("abc", True),
        ("abca", False),
        ("hello", False),
        ("world", True),
        ("python", True),
        ("aabbcc", False),
        ("unique", False),
        ("abcdefg", True)
    ]

    print("Testing is_unique function:")
    print("-" * 50)
    for string, expected in test_strings:
        result = is_unique(string)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_unique('{string}'): {result} (expected: {expected})")

    print("\n" + "=" * 50)
    print("\nTesting is_unique_optimized function (lowercase only):")
    print("-" * 50)
    lowercase_tests = [(s, e) for s, e in test_strings if s.islower() or s == ""]
    for string, expected in lowercase_tests:
        result = is_unique_optimized(string)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_unique_optimized('{string}'): {result} (expected: {expected})")
