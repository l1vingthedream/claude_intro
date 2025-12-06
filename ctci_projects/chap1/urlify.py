def urlify_simple(s, true_length):
    """
    Simple approach using Python string replace.
    Not in-place, but straightforward.

    Args:
        s: String with extra space at the end
        true_length: The actual length of the string content

    Returns:
        URLified string

    Time Complexity: O(n)
    Space Complexity: O(n) - creates new string
    """
    # Take only the true length portion and replace spaces
    return s[:true_length].replace(' ', '%20')


def urlify_inplace(s, true_length):
    """
    In-place approach using list (character array simulation).
    Works backwards to avoid overwriting characters.

    Args:
        s: String with extra space at the end
        true_length: The actual length of the string content

    Returns:
        URLified string

    Time Complexity: O(n)
    Space Complexity: O(n) - for the character list
    """
    # Convert string to list for in-place modification
    char_list = list(s)

    # Count spaces in the true length portion
    space_count = 0
    for i in range(true_length):
        if char_list[i] == ' ':
            space_count += 1

    # Calculate the final index position
    # Each space becomes '%20' (1 char -> 3 chars, so +2 per space)
    final_index = true_length + space_count * 2 - 1

    # Work backwards from true_length
    for i in range(true_length - 1, -1, -1):
        if char_list[i] == ' ':
            char_list[final_index] = '0'
            char_list[final_index - 1] = '2'
            char_list[final_index - 2] = '%'
            final_index -= 3
        else:
            char_list[final_index] = char_list[i]
            final_index -= 1

    return ''.join(char_list)


def urlify(s, true_length):
    """
    Main URLify function using the in-place approach.

    Args:
        s: String with extra space at the end
        true_length: The actual length of the string content

    Returns:
        URLified string with spaces replaced by '%20'

    Time Complexity: O(n)
    Space Complexity: O(n) - for the character list in Python
    """
    return urlify_inplace(s, true_length)


if __name__ == "__main__":
    # Test cases: (input_string, true_length, expected_output)
    test_cases = [
        ("Mr John Smith    ", 13, "Mr%20John%20Smith"),
        ("hello world  ", 11, "hello%20world"),
        ("a b c      ", 5, "a%20b%20c"),
        ("test  ", 4, "test"),
        ("   ", 1, "%20"),
        ("x    ", 1, "x"),
        ("a b      ", 3, "a%20b"),
        ("single", 6, "single"),
        ("  leading      ", 9, "%20%20leading"),
        ("trailing    ", 8, "trailing"),
    ]

    print("Testing urlify_simple function:")
    print("-" * 70)
    for input_str, length, expected in test_cases:
        result = urlify_simple(input_str, length)
        status = "✓" if result == expected else "✗"
        print(f"{status} urlify_simple('{input_str}', {length})")
        print(f"   Result:   '{result}'")
        print(f"   Expected: '{expected}'")
        if result != expected:
            print(f"   MISMATCH!")
        print()

    print("=" * 70)
    print("\nTesting urlify_inplace function:")
    print("-" * 70)
    for input_str, length, expected in test_cases:
        result = urlify_inplace(input_str, length)
        # Trim to expected length for comparison
        result_trimmed = result[:len(expected)]
        status = "✓" if result_trimmed == expected else "✗"
        print(f"{status} urlify_inplace('{input_str}', {length})")
        print(f"   Result:   '{result_trimmed}'")
        print(f"   Expected: '{expected}'")
        if result_trimmed != expected:
            print(f"   MISMATCH!")
        print()

    # Interactive test
    print("=" * 70)
    print("\nInteractive example:")
    print("-" * 70)
    test_string = "Mr John Smith    "
    true_len = 13
    result = urlify(test_string, true_len)
    print(f"Input:  '{test_string}' (true length: {true_len})")
    print(f"Output: '{result}'")
    print(f"\nOriginal length: {len(test_string)}")
    print(f"True length: {true_len}")
    print(f"Spaces in true portion: {test_string[:true_len].count(' ')}")
    print(f"Expected final length: {true_len + test_string[:true_len].count(' ') * 2}")
