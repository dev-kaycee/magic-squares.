def generate_magic_square(n: int):
    """
    Generates a magic square of size n.
    """
    if n % 2 == 0:
        raise ValueError("N must be an odd number.")

    # Initialize the magic square with zeros
    magic_square = [[0 for x in range(n)] for y in range(n)]

    # Set the starting position for the first number
    i = n // 2
    j = n - 1

    # Fill the magic square with numbers
    for num in range(1, n*n+1):
        if magic_square[i][j] != 0:
            j = (j - 2) % n
            i = (i + 1) % n

        # Place the number
        magic_square[i][j] = num

        # Move the cursor
        j = (j + 1) % n
        i = (i - 1) % n

    return magic_square


def print_magic_square(magic_square: list[list[int]]):
    """
    Prints out the magic square in a legible format.
    """
    for row in magic_square:
        print(" ".join(str(num) for num in row))


def verify_magic_square(magic_square: list[list[int]]) -> bool:
    """
    Verifies that the given square is a magic square.
    """
    n = len(magic_square)
    magic_sum = n * (n**2 + 1) // 2

    # Check the rows and columns
    for i in range(n):
        row_sum = 0
        col_sum = 0
        for j in range(n):
            row_sum += magic_square[i][j]
            col_sum += magic_square[j][i]
        if row_sum != magic_sum or col_sum != magic_sum:
            return False

    # Check the diagonals
    diag_sum1 = 0
    diag_sum2 = 0
    for i in range(n):
        diag_sum1 += magic_square[i][i]
        diag_sum2 += magic_square[i][n-i-1]
    if diag_sum1 != magic_sum or diag_sum2 != magic_sum:
        return False

    return True


if __name__ == '__main__':
    while True:
        try:
            n = int(input("Enter the value of N: "))
            if n % 2 == 0:
                raise ValueError("N must be an odd number.")
            break
        except ValueError:
            print("N must be a positive odd integer. Please try again.")

    magic_square = generate_magic_square(n)
    print_magic_square(magic_square)

    if verify_magic_square(magic_square):
        print("Correct")
    else:
        print("Incorrect")
