def factorial(n):
    """
    This function calculates the factorial of a given integer n.
    Args:
        n (int): The integer to calculate the factorial of.
    Returns:
        int: The factorial of n.
    Raises:
        ValueError: If n is negative.
        TypeError: If n is not an integer.
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer.")
    if n < 0:
        raise ValueError("Input must be a non-negative integer.")
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)