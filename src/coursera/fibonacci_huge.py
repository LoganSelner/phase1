def get_pisano_period(m: int) -> int:
    """Compute the Pisano period for modulus m.

    Args:
        m (int): The modulus.

    Returns:
        int: The length of the Pisano period for modulus m.

    Raises:
        ValueError: If m is not a positive integer.
    """
    if m <= 0:
        raise ValueError("Modulus m must be a positive integer")

    prev, curr = 0, 1
    for i in range(0, m * m):
        prev, curr = curr, (prev + curr) % m
        if prev == 0 and curr == 1:
            return i + 1
    return m * m  # Fallback, should not happen


def fibonacci_huge(n: int, m: int) -> int:
    """Compute the n-th Fibonacci number modulo m.

    Args:
        n (int): The index of the Fibonacci number to compute.
        m (int): The modulus.

    Returns:
        int: The n-th Fibonacci number modulo m.

    Raises:
        ValueError: If n is negative or m is not positive.
    """
    if n < 0 or m <= 0:
        raise ValueError(
            "n must be a non-negative integer and m must be a positive integer"
        )

    pisano_period = get_pisano_period(m)
    n = n % pisano_period
    if n <= 1:
        return n % m

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, (a + b) % m
    return b


if __name__ == "__main__":
    n, m = map(int, input().split())
    print(fibonacci_huge(n, m))
