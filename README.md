# magic-squares.
## enerate_magic_square(n: int)

This function generates a magic square of size n. A magic square is an n x n grid filled with distinct positive integers in the range [1, n^2], such that the sum of each row, column, and diagonal is the same. The function takes an integer n as input and returns a list of lists representing the magic square.

### Parameters:

n (int): the size of the magic square to be generated
Raises:

ValueError: if n is not an odd number
Returns:

list[list[int]]: a list of lists representing the magic square
Algorithm:

If n is even, raise a ValueError because a magic square cannot be generated for even n.
Initialize an n x n matrix (list of lists) with zeros.
Set the starting position for the first number to be placed in the center column of the last row.
Fill the matrix with the integers in the range [1, n^2] such that the sum of each row, column, and diagonal is the same.
Return the magic square.
Documentation for print_magic_square(magic_square: list[list[int]])

This function prints out the magic square in a legible format. The function takes a list of lists representing the magic square as input and prints it to the console.

### Parameters:

magic_square (list[list[int]]): a list of lists representing the magic square
Returns:

None
Algorithm:

Iterate over each row in the magic square.
Convert each integer in the row to a string and join them with a space.
Print the resulting string.
Documentation for verify_magic_square(magic_square: list[list[int]]) -> bool

This function verifies that the given square is a magic square. The function takes a list of lists representing the magic square as input and returns a boolean indicating whether or not it is a magic square.

### Parameters:

magic_square (list[list[int]]): a list of lists representing the magic square
Returns:

bool: True if the magic square is valid, False otherwise
Algorithm:

Calculate the magic sum, which is the sum of each row, column, and diagonal in the magic square.
Check that each row and column sum to the magic sum.
Check that each diagonal sum to the magic sum.
If the magic square passes all checks, return True. Otherwise, return False.
Documentation for main program:

The main program prompts the user to enter the size of the magic square, generates the magic square, prints it to the console, and verifies that it is a valid magic square.

Algorithm:

Prompt the user to enter the size of the magic square.
If the input is not a positive odd integer, print an error message and ask for input again.
Generate the magic square using the generate_magic_square function.
Print the magic square to the console using the print_magic_square function.
Verify that the magic square is valid using the verify_magic_square function.
Print "Correct" if the magic square is valid, or "Incorrect" otherwise.
