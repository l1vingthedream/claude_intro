def rotate_matrix_inplace(matrix):
    """Rotate NxN matrix 90 degrees clockwise in-place. O(n²) time, O(1) space."""
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    # Rotate layer by layer
    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first

            # Save top
            top = matrix[first][i]

            # left -> top
            matrix[first][i] = matrix[last - offset][first]

            # bottom -> left
            matrix[last - offset][first] = matrix[last][last - offset]

            # right -> bottom
            matrix[last][last - offset] = matrix[i][last]

            # top -> right
            matrix[i][last] = top

    return True


def rotate_matrix_transpose(matrix):
    """Rotate via transpose + reverse rows. O(n²) time, O(1) space."""
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    # Transpose
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    for i in range(n):
        matrix[i].reverse()

    return True


def rotate_matrix_fast(matrix):
    """Optimized transpose + reverse. Better cache locality and fewer ops."""
    if not matrix or len(matrix) != len(matrix[0]):
        return False

    n = len(matrix)

    # Transpose with manual swap (faster than tuple unpacking)
    for i in range(n):
        for j in range(i + 1, n):
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp

    # Reverse using slicing (faster than reverse())
    for i in range(n):
        matrix[i] = matrix[i][::-1]

    return True


def rotate_matrix(matrix):
    """Main function - rotates NxN matrix 90 degrees clockwise in-place."""
    return rotate_matrix_fast(matrix)


if __name__ == "__main__":
    test_cases = [
        # 1x1
        ([[1]], [[1]]),

        # 2x2
        ([[1, 2],
          [3, 4]],
         [[3, 1],
          [4, 2]]),

        # 3x3
        ([[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]],
         [[7, 4, 1],
          [8, 5, 2],
          [9, 6, 3]]),

        # 4x4
        ([[ 1,  2,  3,  4],
          [ 5,  6,  7,  8],
          [ 9, 10, 11, 12],
          [13, 14, 15, 16]],
         [[13,  9, 5, 1],
          [14, 10, 6, 2],
          [15, 11, 7, 3],
          [16, 12, 8, 4]]),

        # 5x5
        ([[ 1,  2,  3,  4,  5],
          [ 6,  7,  8,  9, 10],
          [11, 12, 13, 14, 15],
          [16, 17, 18, 19, 20],
          [21, 22, 23, 24, 25]],
         [[21, 16, 11,  6,  1],
          [22, 17, 12,  7,  2],
          [23, 18, 13,  8,  3],
          [24, 19, 14,  9,  4],
          [25, 20, 15, 10,  5]]),
    ]

    print("Testing rotate_matrix_inplace:")
    print("-" * 60)
    for original, expected in test_cases:
        matrix = [row[:] for row in original]  # Deep copy
        result = rotate_matrix_inplace(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"{status} {len(matrix)}x{len(matrix)} matrix")
        if matrix != expected:
            print(f"   Expected: {expected}")
            print(f"   Got:      {matrix}")

    print("\n" + "=" * 60)
    print("\nTesting rotate_matrix_transpose:")
    print("-" * 60)
    for original, expected in test_cases:
        matrix = [row[:] for row in original]
        result = rotate_matrix_transpose(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"{status} {len(matrix)}x{len(matrix)} matrix")
        if matrix != expected:
            print(f"   Expected: {expected}")
            print(f"   Got:      {matrix}")

    print("\n" + "=" * 60)
    print("\nTesting rotate_matrix_fast:")
    print("-" * 60)
    for original, expected in test_cases:
        matrix = [row[:] for row in original]
        result = rotate_matrix_fast(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"{status} {len(matrix)}x{len(matrix)} matrix")
        if matrix != expected:
            print(f"   Expected: {expected}")
            print(f"   Got:      {matrix}")

    print("\n" + "=" * 60)
    print("\nExample - 3x3 rotation:")
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Before:")
    for row in matrix:
        print(f"  {row}")

    rotate_matrix(matrix)
    print("\nAfter 90° clockwise rotation:")
    for row in matrix:
        print(f"  {row}")
