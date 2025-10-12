def fibonacci_sum(n: int) -> int:
    """Compute the last digit of the sum of the first n Fibonacci numbers.

    Args:
        n (int): The index of the last Fibonacci number to include in the sum.

    Returns:
        int: The last digit of the sum of the first n Fibonacci numbers.

    Raises:
        ValueError: If n is negative.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    # The last digit of the sum of the first n Fibonacci numbers is equal to
    # the last digit of F(n+2) - 1, where F(n) is the n-th Fibonacci number.
    fibonacci_index = (n + 2) % 60  # Pisano period for modulus 10 is 60
    if fibonacci_index <= 1:
        return (fibonacci_index - 1) % 10
    a, b = 0, 1
    for _ in range(2, fibonacci_index + 1):
        a, b = b, (a + b) % 10
    return (b - 1) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum(n))
