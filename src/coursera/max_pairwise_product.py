def max_pairwise_product(numbers: list[float]) -> float:
    """
    Find the maximum pairwise product in a list of numbers.

    Args:
        numbers (list of float): A list of numbers.

    Returns:
        float: The maximum pairwise product.

    Raises:
        ValueError: If the list has fewer than two numbers.
    """
    n = len(numbers)
    if n < 2:
        raise ValueError("At least two numbers are required")

    # Initialize the two largest numbers to negative infinity
    first_max = second_max = float("-inf")
    # Initialize the two smallest numbers to positive infinity
    first_min = second_min = float("inf")

    for number in numbers:
        # Update the two largest numbers
        if number > first_max:
            second_max = first_max
            first_max = number
        elif number > second_max:
            second_max = number
        # Update the two smallest numbers
        if number < first_min:
            second_min = first_min
            first_min = number
        elif number < second_min:
            second_min = number

    return max(first_max * second_max, first_min * second_min)


if __name__ == "__main__":
    n = int(input())
    numbers = list(map(float, input().split()))
    if len(numbers) != n:
        raise ValueError("The number of numbers provided does not match n")
    print(int(max_pairwise_product(numbers)))
