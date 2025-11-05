def largest_number(numbers: list[str]) -> str:
    """Form the largest number by concatenating the given integers.

    Args:
        numbers (list of str): A list of non-negative integers represented as strings.

    Returns:
        str: The largest number formed by concatenating the integers.
    """
    from functools import cmp_to_key

    def compare(a: str, b: str) -> int:
        return (b + a > a + b) - (b + a < a + b)  # sort descending by a+b vs b+a

    sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
    result = "".join(sorted_numbers)
    return result


if __name__ == "__main__":
    _ = int(input())
    input_numbers = input().split()
    print(largest_number(input_numbers))
