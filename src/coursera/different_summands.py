# Represent a positive integer as the sum of the
# maximum number of pairwise distinct positive
# integers.
def optimal_summands(n: int) -> list[int]:
    # Google style docstring format
    """Find the maximum number of pairwise distinct positive integers that sum up to n.

    Args:
        n (int): A positive integer to be represented as the sum.

    Returns:
        list of int: A list of pairwise distinct positive integers that sum up to n.

    Raises:
        ValueError: If n is not a positive integer.
    """
    if n <= 0:
        raise ValueError("Input must be a positive integer.")

    summands = []
    current_sum = 0
    next_summand = 1
    while current_sum + next_summand <= n:
        summands.append(next_summand)
        current_sum += next_summand
        next_summand += 1
    if current_sum < n:
        summands[-1] += n - current_sum
    return summands


if __name__ == "__main__":
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
