def string_compress_simple(s):
    """
    Simple approach using string concatenation.

    Args:
        s: String to compress

    Returns:
        Compressed string if smaller, otherwise original string

    Time Complexity: O(n + k^2) where k is number of character sequences
                     (string concatenation is O(k) each time)
    Space Complexity: O(n)
    """
    if not s:
        return s

    compressed = ""
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed += s[i - 1] + str(count)
            count = 1

    # Add the last character and its count
    compressed += s[-1] + str(count)

    # Return original if compressed is not smaller
    return compressed if len(compressed) < len(s) else s


def string_compress_optimized(s):
    """
    Optimized approach using list and join.
    Better performance for string building.

    Args:
        s: String to compress

    Returns:
        Compressed string if smaller, otherwise original string

    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not s:
        return s

    # Check if compression would be beneficial before building
    compressed_length = count_compressed_length(s)
    if compressed_length >= len(s):
        return s

    compressed = []
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1])
            compressed.append(str(count))
            count = 1

    # Add the last character and its count
    compressed.append(s[-1])
    compressed.append(str(count))

    return ''.join(compressed)


def count_compressed_length(s):
    """
    Calculate the length of compressed string without building it.

    Args:
        s: String to check

    Returns:
        Length that compressed string would be
    """
    if not s:
        return 0

    compressed_length = 0
    count = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            compressed_length += 1 + len(str(count))
            count = 1

    # Add the last character and its count
    compressed_length += 1 + len(str(count))

    return compressed_length


def string_compress(s):
    """
    Main function to compress a string.

    Args:
        s: String with only uppercase and lowercase letters (a-z)

    Returns:
        Compressed string if smaller than original, otherwise original string

    Examples:
        "aabcccccaaa" -> "a2b1c5a3"
        "abcdef" -> "abcdef" (no compression benefit)
        "aaa" -> "a3"
        "ab" -> "ab" (compressed would be "a1b1" which is longer)
    """
    return string_compress_optimized(s)


if __name__ == "__main__":
    # Test cases: (input_string, expected_output)
    test_cases = [
        # Given example
        ("aabcccccaaa", "a2b1c5a3"),

        # No compression benefit
        ("abcdef", "abcdef"),           # Each char appears once
        ("ab", "ab"),                    # Would become "a1b1" (longer)
        ("abc", "abc"),                  # Would become "a1b1c1" (longer)

        # Clear compression benefit
        ("aaa", "a3"),
        ("aaaa", "a4"),
        ("aaaaa", "a5"),
        ("aabbcc", "aabbcc"),            # Same length, return original
        ("aaabbb", "a3b3"),              # Shorter
        ("aaabbbbcccc", "a3b4c4"),

        # Edge cases
        ("", ""),                        # Empty string
        ("a", "a"),                      # Single character
        ("aa", "aa"),                    # Would become "a2" (same length)

        # Mixed cases
        ("AAAaaa", "A3a3"),
        ("aAbBcC", "aAbBcC"),            # No compression
        ("AAaaBBbb", "AAaaBBbb"),        # Same length, return original

        # Long sequences
        ("aaaaaaaaaaaa", "a12"),         # 12 a's
        ("aaaaaaaaaa", "a10"),           # 10 a's

        # Alternating (worst case for compression)
        ("ababab", "ababab"),            # Would become "a1b1a1b1a1b1" (longer)

        # Real-world-ish examples
        ("wwwwaaadexxxxxx", "w4a3d1e1x6"),
        ("Mississippi", "Mississippi"),  # Would be longer compressed
    ]

    print("Testing string_compress_simple function:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = string_compress_simple(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} string_compress_simple('{input_str}')")
        print(f"   Result:   '{result}'")
        print(f"   Expected: '{expected}'")
        if result != expected:
            print(f"   MISMATCH!")
        print()

    print("=" * 70)
    print("\nTesting string_compress_optimized function:")
    print("-" * 70)
    for input_str, expected in test_cases:
        result = string_compress_optimized(input_str)
        status = "✓" if result == expected else "✗"
        print(f"{status} string_compress_optimized('{input_str}')")
        print(f"   Result:   '{result}'")
        print(f"   Expected: '{expected}'")
        if result != expected:
            print(f"   MISMATCH!")
        print()

    # Interactive examples
    print("=" * 70)
    print("\nInteractive examples:")
    print("-" * 70)
    examples = [
        ("aabcccccaaa", "5 unique sequences, compression beneficial"),
        ("abcdef", "6 sequences of 1 char each, no compression benefit"),
        ("aaabbbbcccc", "3 sequences with counts 3,4,4 - worth compressing"),
        ("ab", "2 sequences, would become 'a1b1' which is longer"),
    ]

    for input_str, explanation in examples:
        result = string_compress(input_str)
        original_len = len(input_str)
        compressed_len = count_compressed_length(input_str)

        print(f"Input: '{input_str}'")
        print(f"  Original length: {original_len}")
        print(f"  Compressed length would be: {compressed_len}")
        print(f"  Result: '{result}'")
        print(f"  Explanation: {explanation}")
        print()
