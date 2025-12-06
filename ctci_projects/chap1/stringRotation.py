def is_substring(s1, s2):
    """Check if s2 is a substring of s1."""
    return s2 in s1


def is_rotation(s1, s2):
    """Check if s2 is a rotation of s1 using only one call to is_substring."""
    if len(s1) != len(s2) or len(s1) == 0:
        return False

    # Key insight: if s2 is a rotation of s1, then s2 is a substring of s1+s1
    # Example: s1="waterbottle", s2="erbottlewat"
    # s1+s1="waterbottlewaterbottle" contains "erbottlewat"
    return is_substring(s1 + s1, s2)


if __name__ == "__main__":
    test_cases = [
        # Basic rotations
        ("waterbottle", "erbottlewat", True),
        ("hello", "llohe", True),
        ("abc", "bca", True),
        ("abc", "cab", True),

        # Not rotations
        ("hello", "world", False),
        ("abc", "acb", False),
        ("waterbottle", "bottlewater", True),

        # Edge cases
        ("", "", False),
        ("a", "a", True),
        ("aa", "aa", True),
        ("ab", "ba", True),

        # Different lengths
        ("abc", "abcd", False),
        ("hello", "hi", False),

        # Same characters but not rotation
        ("abc", "bac", False),

        # Longer strings
        ("programming", "mingprogram", True),
        ("algorithm", "rithmalgo", True),
        ("python", "onpyth", True),
    ]

    print("Testing is_rotation function:")
    print("-" * 60)
    for s1, s2, expected in test_cases:
        result = is_rotation(s1, s2)
        status = "✓" if result == expected else "✗"
        print(f"{status} is_rotation('{s1}', '{s2}'): {result} (expected: {expected})")

    print("\n" + "=" * 60)
    print("\nExample explanation:")
    s1 = "waterbottle"
    s2 = "erbottlewat"
    print(f"s1 = '{s1}'")
    print(f"s2 = '{s2}'")
    print(f"s1 + s1 = '{s1 + s1}'")
    print(f"Is '{s2}' in '{s1 + s1}'? {s2 in (s1 + s1)}")
    print(f"Result: {is_rotation(s1, s2)}")
