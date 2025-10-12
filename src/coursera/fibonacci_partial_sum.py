def fibonacci_partial_sum(from_: int, to: int) -> int:
    """Compute the last digit of the sum of Fibonacci numbers from F_from to F_to (inclusive).

    Args:
        from_ (int): The starting index of the Fibonacci sequence (0-based).
        to (int): The ending index of the Fibonacci sequence (0-based).

    Returns:
        int: The last digit of the sum of Fibonacci numbers from F_from to F_to.

    Raises:
        ValueError: If from_ or to are negative, or if from_ > to.
    """
    if from_ < 0 or to < 0 or from_ > to:
        raise ValueError("from_ and to must be non-negative integers with from_ <= to")
    if from_ == 0 and to == 0:
        return 0

    pisano_index1 = (from_ + 1) % 60

    a, b = 0, 1
    for _ in range(2, pisano_index1 + 1):
        a, b = b, (a + b) % 10
    last_digit_sum_from = (b - 1) % 10

    pisano_index2 = (to + 2) % 60
    a, b = 0, 1
    for _ in range(2, pisano_index2 + 1):
        a, b = b, (a + b) % 10
    last_digit_sum_to = (b - 1) % 10

    return (last_digit_sum_to - last_digit_sum_from) % 10


if __name__ == "__main__":
    from_, to = map(int, input().split())
    print(fibonacci_partial_sum(from_, to))
