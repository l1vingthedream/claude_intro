def zero_matrix_extra_space(matrix):
    """Zero rows/cols if element is 0. O(mn) time, O(m+n) space."""
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    zero_rows = set()
    zero_cols = set()

    # Find zeros
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zero_rows.add(i)
                zero_cols.add(j)

    # Zero rows
    for row in zero_rows:
        for j in range(cols):
            matrix[row][j] = 0

    # Zero cols
    for col in zero_cols:
        for i in range(rows):
            matrix[i][col] = 0


def zero_matrix_inplace(matrix):
    """Zero rows/cols if element is 0. O(mn) time, O(1) space."""
    if not matrix:
        return

    rows = len(matrix)
    cols = len(matrix[0])
    first_row_zero = False
    first_col_zero = False

    # Check if first row has zero
    for j in range(cols):
        if matrix[0][j] == 0:
            first_row_zero = True
            break

    # Check if first col has zero
    for i in range(rows):
        if matrix[i][0] == 0:
            first_col_zero = True
            break

    # Use first row/col as markers
    for i in range(1, rows):
        for j in range(1, cols):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Zero rows based on first col markers
    for i in range(1, rows):
        if matrix[i][0] == 0:
            for j in range(1, cols):
                matrix[i][j] = 0

    # Zero cols based on first row markers
    for j in range(1, cols):
        if matrix[0][j] == 0:
            for i in range(1, rows):
                matrix[i][j] = 0

    # Zero first row if needed
    if first_row_zero:
        for j in range(cols):
            matrix[0][j] = 0

    # Zero first col if needed
    if first_col_zero:
        for i in range(rows):
            matrix[i][0] = 0


def zero_matrix(matrix):
    """Main function - zeros rows/cols containing zero elements."""
    zero_matrix_inplace(matrix)


if __name__ == "__main__":
    test_cases = [
        # Basic cases
        ([[1, 2, 3],
          [4, 0, 6],
          [7, 8, 9]],
         [[1, 0, 3],
          [0, 0, 0],
          [7, 0, 9]]),

        # Multiple zeros
        ([[1, 0, 3],
          [4, 5, 6],
          [0, 8, 9]],
         [[0, 0, 0],
          [0, 0, 6],
          [0, 0, 0]]),

        # No zeros
        ([[1, 2],
          [3, 4]],
         [[1, 2],
          [3, 4]]),

        # All zeros
        ([[0, 0],
          [0, 0]],
         [[0, 0],
          [0, 0]]),

        # Single element
        ([[5]], [[5]]),
        ([[0]], [[0]]),

        # First row zero
        ([[0, 2, 3],
          [4, 5, 6],
          [7, 8, 9]],
         [[0, 0, 0],
          [0, 5, 6],
          [0, 8, 9]]),

        # First col zero
        ([[1, 2, 3],
          [0, 5, 6],
          [7, 8, 9]],
         [[0, 2, 3],
          [0, 0, 0],
          [0, 8, 9]]),

        # 4x5 matrix
        ([[1, 2, 3, 4, 5],
          [6, 0, 8, 9, 10],
          [11, 12, 0, 14, 15],
          [16, 17, 18, 19, 20]],
         [[1, 0, 0, 4, 5],
          [0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0],
          [16, 0, 0, 19, 20]]),
    ]

    print("Testing zero_matrix_extra_space:")
    print("-" * 60)
    for original, expected in test_cases:
        matrix = [row[:] for row in original]
        zero_matrix_extra_space(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"{status} {len(matrix)}x{len(matrix[0])} matrix")
        if matrix != expected:
            print(f"   Expected: {expected}")
            print(f"   Got:      {matrix}")

    print("\n" + "=" * 60)
    print("\nTesting zero_matrix_inplace:")
    print("-" * 60)
    for original, expected in test_cases:
        matrix = [row[:] for row in original]
        zero_matrix_inplace(matrix)
        status = "✓" if matrix == expected else "✗"
        print(f"{status} {len(matrix)}x{len(matrix[0])} matrix")
        if matrix != expected:
            print(f"   Expected: {expected}")
            print(f"   Got:      {matrix}")

    print("\n" + "=" * 60)
    print("\nExample:")
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print("Before:")
    for row in matrix:
        print(f"  {row}")

    zero_matrix(matrix)
    print("\nAfter:")
    for row in matrix:
        print(f"  {row}")
