def fibonacci_last_digit(n: int) -> int:
    """Return the last digit of the n-th Fibonacci number.
    Args:
        n (int): The index of the Fibonacci number.

    Returns:
        int: The last digit of the n-th Fibonacci number.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    n = n % 60  # Pisano period for modulo 10 is 60
    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % 10
    return b


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_last_digit(n))
