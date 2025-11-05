def max_dot_product(first_sequence: list[int], second_sequence: list[int]) -> int:
    """Calculate the maximum dot product of two sequences.

    Args:
        first_sequence (list of int): The first sequence of numbers.
        second_sequence (list of int): The second sequence of numbers.

    Returns:
        int: The maximum dot product of the two sequences.

    Raises:
        ValueError: If the sequences are of different lengths.
    """
    if len(first_sequence) != len(second_sequence):
        raise ValueError("Sequences must be of the same length.")
    # Sort both sequences in descending order
    first_sequence.sort(reverse=True)
    second_sequence.sort(reverse=True)

    return sum(a * b for a, b in zip(first_sequence, second_sequence, strict=True))


if __name__ == "__main__":
    n = int(input())
    prices = list(map(int, input().split()))
    clicks = list(map(int, input().split()))
    assert len(prices) == len(clicks) == n
    print(max_dot_product(prices, clicks))
