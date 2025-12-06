def is_palindrome_permutation_dict(s):
    """
    Check if string is a permutation of a palindrome using dictionary.

    A string can form a palindrome if at most one character has an odd count.
    Ignores spaces and case.

    Args:
        s: String to check

    Returns:
        True if string is a permutation of a palindrome, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    # Count character frequencies (ignoring spaces and case)
    char_count = {}
    for char in s.lower():
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1

    # Count how many characters have odd frequencies
    odd_count = 0
    for count in char_count.values():
        if count % 2 == 1:
            odd_count += 1

    # At most one character can have an odd count
    return odd_count <= 1


def is_palindrome_permutation_optimized(s):
    """
    Optimized version - count odd occurrences on the fly.

    Args:
        s: String to check

    Returns:
        True if string is a permutation of a palindrome, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    char_count = {}
    odd_count = 0

    for char in s.lower():
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1
            # If count just became odd, increment odd_count
            # If count just became even, decrement odd_count
            if char_count[char] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1

    return odd_count <= 1


def is_palindrome_permutation_bitvector(s):
    """
    Check using bit vector for lowercase letters only.
    Uses a bit vector to toggle character occurrences.

    Args:
        s: String to check (lowercase letters only, spaces ignored)

    Returns:
        True if string is a permutation of a palindrome, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    bit_vector = 0

    for char in s.lower():
        if char != ' ' and char.isalpha():
            # Get position for this character (a=0, b=1, etc.)
            char_index = ord(char) - ord('a')
            # Toggle the bit at this position
            bit_vector ^= (1 << char_index)

    # Check if at most one bit is set
    # A number with at most one bit set satisfies: n & (n-1) == 0
    # Examples: 0 & -1 = 0, 1 & 0 = 0, 2 & 1 = 0, 4 & 3 = 0
    # But 3 & 2 = 2 (not 0), 5 & 4 = 4 (not 0)
    return bit_vector == 0 or (bit_vector & (bit_vector - 1)) == 0


def is_palindrome_permutation(s):
    """
    Main function to check if string is a permutation of a palindrome.

    Args:
        s: String to check

    Returns:
        True if string is a permutation of a palindrome, False otherwise
    """
    return is_palindrome_permutation_optimized(s)


if __name__ == "__main__":
    # Test cases: (input_string, expected_output)
    test_cases = [
        ("Tact Coa", True),           # "taco cat"
        ("taco cat", True),            # Already a palindrome
        ("atco cta", True),            # "tacocat"
        ("abc", False),                # Can't form palindrome
        ("aab", True),                 # "aba"
        ("carerac", True),             # "racecar"
        ("code", False),               # Can't form palindrome
        ("", True),                    # Empty string
        ("a", True),                   # Single character
        ("aa", True),                  # Two same characters
        ("ab", False),                 # Two different characters
        ("aabbcc", True),              # "abccba"
        ("aabbc", True),               # "abcba"
        ("aabbcd", False),             # Two odd counts (c and d)
        ("civic", True),               # Already palindrome
        ("ivicc", True),               # Permutation of "civic"
        ("A man a plan a canal Panama", True),  # Famous palindrome
        ("hello", False),              # Can't form palindrome
        ("aaabbb", False),             # Two characters with odd counts
        ("aaabbbc", False),            # Three odd counts (a=3, b=3, c=1) - can't form palindrome
        ("aaabbbbcc", True),           # One odd count: a=3 (odd), b=4 (even), c=2 (even)
    ]

    print("Testing is_palindrome_permutation_dict function:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = is_palindrome_permutation_dict(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_permutation_dict('{input_str}'): {result} (expected: {expected})")

    print("\n" + "=" * 70)
    print("\nTesting is_palindrome_permutation_optimized function:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = is_palindrome_permutation_optimized(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_permutation_optimized('{input_str}'): {result} (expected: {expected})")

    print("\n" + "=" * 70)
    print("\nTesting is_palindrome_permutation_bitvector function:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = is_palindrome_permutation_bitvector(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_palindrome_permutation_bitvector('{input_str}'): {result} (expected: {expected})")

    # Interactive example
    print("\n" + "=" * 70)
    print("\nInteractive example:")
    print("-" * 70)
    test_input = "Tact Coa"
    result = is_palindrome_permutation(test_input)

    # Count characters for demonstration
    char_count = {}
    for char in test_input.lower():
        if char != ' ':
            char_count[char] = char_count.get(char, 0) + 1

    print(f"Input: '{test_input}'")
    print(f"Character counts: {dict(sorted(char_count.items()))}")
    print(f"Characters with odd counts: {sum(1 for c in char_count.values() if c % 2 == 1)}")
    print(f"Is palindrome permutation: {result}")
    print(f"\nExample palindromes: 'taco cat', 'atco cta'")
