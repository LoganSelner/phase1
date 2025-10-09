def sum_of_digits(a: int, b: int) -> int:
    """
    Returns the sum of the digits of the integers a and b.

    :param a: First integer
    :param b: Second integer
    :return: Sum of the digits of a and b
    """
    return a + b


if __name__ == "__main__":
    a, b = map(int, input("Enter two integers: ").split())
    print(f"Sum: {sum_of_digits(a, b)}")
