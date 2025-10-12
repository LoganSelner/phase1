def lcm(a: int, b: int) -> int:
    """Compute the least common multiple of a and b.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The least common multiple of a and b.
    """
    a, b = abs(a), abs(b)
    if a == 0 or b == 0:
        return 0
    orig_a, orig_b = a, b
    # Compute the greatest common divisor (GCD) using the Euclidean algorithm
    while b:
        a, b = b, a % b
    gcd = a  # GCD of orig_a and orig_b

    return orig_a * orig_b // gcd


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(lcm(a, b))
