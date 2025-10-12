def fibonacci(n: int) -> int:
    """
    Compute the nth Fibonacci number

    Args:
        n (int): The index of the Fibonacci number to compute.

    Returns:
        int: The nth Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    elif n == 0:
        return 0
    elif n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


if __name__ == "__main__":
    n = int(input())
    print(fibonacci(n))
