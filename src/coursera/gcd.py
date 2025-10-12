def gcd(a: int, b: int) -> int:
    """Compute the greatest common divisor of a and b using Euclid's algorithm.

    Args:
        a (int): First non-negative integer.
        b (int): Second non-negative integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    a, b = abs(a), abs(b)
    while b:
        a, b = b, a % b
    return a


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(gcd(a, b))
