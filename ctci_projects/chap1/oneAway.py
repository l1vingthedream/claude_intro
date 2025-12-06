def one_away(s1, s2):
    """
    Check if two strings are one edit (or zero edits) away.
    Three types of edits: insert, remove, or replace a character.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are one edit away, False otherwise

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Check length difference
    len1, len2 = len(s1), len(s2)

    # If length difference is more than 1, can't be one edit away
    if abs(len1 - len2) > 1:
        return False

    # Get shorter and longer string
    shorter = s1 if len1 < len2 else s2
    longer = s2 if len1 < len2 else s1

    index1 = 0
    index2 = 0
    found_difference = False

    while index1 < len(shorter) and index2 < len(longer):
        if shorter[index1] != longer[index2]:
            # If we already found a difference, this is the second one
            if found_difference:
                return False
            found_difference = True

            # If lengths are same, move both pointers (replacement)
            # If lengths differ, only move pointer for longer string (insertion/deletion)
            if len(shorter) == len(longer):
                index1 += 1
        else:
            index1 += 1

        index2 += 1

    return True


def one_away_alternative(s1, s2):
    """
    Alternative implementation with separate functions for each case.

    Args:
        s1: First string
        s2: Second string

    Returns:
        True if strings are one edit away, False otherwise
    """
    len1, len2 = len(s1), len(s2)

    # Check length difference
    if abs(len1 - len2) > 1:
        return False

    # Same length: check for one replacement
    if len1 == len2:
        return one_replace_away(s1, s2)

    # Different length: check for one insertion
    return one_insert_away(s1, s2)


def one_replace_away(s1, s2):
    """Check if strings are one replacement away."""
    found_difference = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if found_difference:
                return False
            found_difference = True
    return True


def one_insert_away(s1, s2):
    """Check if strings are one insertion/deletion away."""
    # Make sure s1 is the shorter one
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    index1 = 0
    index2 = 0

    while index1 < len(s1) and index2 < len(s2):
        if s1[index1] != s2[index2]:
            # If indices are different, we already found an insertion
            if index1 != index2:
                return False
            # Move only the longer string's pointer
            index2 += 1
        else:
            index1 += 1
            index2 += 1

    return True


if __name__ == "__main__":
    # Test cases: (string1, string2, expected_result)
    test_cases = [
        # Given examples
        ("pale", "ple", True),           # Remove 'a'
        ("pales", "pale", True),         # Remove 's' or insert 's'
        ("pale", "bale", True),          # Replace 'p' with 'b'
        ("pale", "bake", False),         # Two replacements needed

        # Edge cases
        ("", "", True),                  # Empty strings
        ("", "a", True),                 # Insert one character
        ("a", "", True),                 # Remove one character
        ("a", "b", True),                # Replace one character
        ("ab", "abc", True),             # Insert at end
        ("abc", "ab", True),             # Remove from end
        ("abc", "adc", True),            # Replace in middle

        # Same strings
        ("test", "test", True),          # Zero edits

        # False cases
        ("pale", "bales", False),        # Insert and replace
        ("pale", "tale", True),          # Replace 'p' with 't'
        ("abc", "def", False),           # Three replacements
        ("", "ab", False),               # Two insertions
        ("ab", "", False),               # Two deletions
        ("hello", "billion", False),     # Too many differences

        # More true cases
        ("cat", "cats", True),           # Insert at end
        ("cats", "cat", True),           # Remove from end
        ("cat", "cut", True),            # Replace middle character
        ("intention", "execution", False), # Multiple edits needed
        ("park", "spake", False),        # Length diff > 1
    ]

    print("Testing one_away function:")
    print("-" * 75)
    for s1, s2, expected in test_cases:
        result = one_away(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} one_away('{s1}', '{s2}'): {result} (expected: {expected})")

    print("\n" + "=" * 75)
    print("\nTesting one_away_alternative function:")
    print("-" * 75)
    for s1, s2, expected in test_cases:
        result = one_away_alternative(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} one_away_alternative('{s1}', '{s2}'): {result} (expected: {expected})")

    # Interactive examples
    print("\n" + "=" * 75)
    print("\nInteractive examples:")
    print("-" * 75)
    examples = [
        ("pale", "ple", "remove 'a'"),
        ("pales", "pale", "remove 's'"),
        ("pale", "bale", "replace 'p' with 'b'"),
        ("pale", "bake", "replace 'p' with 'b' AND 'l' with 'k' (2 edits)"),
    ]

    for s1, s2, explanation in examples:
        result = one_away(s1, s2)
        print(f"one_away('{s1}', '{s2}') = {result}")
        print(f"  Explanation: {explanation}")
        print()
