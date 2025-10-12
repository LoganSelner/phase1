def fibonacci_sum_squares(n: int) -> int:
    """Compute the last digit of the sum of the squares of the first n Fibonacci numbers.

    Args:
        n (int): A non-negative integer representing the index of the last Fibonacci number.

    Returns:
        int: The last digit of the sum of the squares of the first n Fibonacci numbers.

    Raises:
        ValueError: If n is a negative integer.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")

    if n <= 1:
        return n

    # Using the property: F(0)^2 + F(1)^2 + ... + F(n)^2 = F(n) * F(n + 1)
    pisano_index1 = n % 60  # Pisano period for modulus 10 is 60
    pisano_index2 = (n + 1) % 60

    a, b = 0, 1
    for _ in range(2, pisano_index1 + 1):
        a, b = b, (a + b) % 10
    last_digit_fn = b
    if pisano_index1 == 0:
        last_digit_fn = 0

    a, b = b, (a + b) % 10
    last_digit_fn_plus_1 = b
    if pisano_index2 == 0:
        last_digit_fn_plus_1 = 0

    return (last_digit_fn * last_digit_fn_plus_1) % 10


if __name__ == "__main__":
    n = int(input())
    print(fibonacci_sum_squares(n))
