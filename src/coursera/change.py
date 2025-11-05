def change(money: int) -> int:
    """Compute the minimum number of coins needed to change the given value.

    Args:
        money (int): The amount of money to change (non-negative integer).

    Returns:
        int: The minimum number of coins needed to make the change.

    Raises:
        ValueError: If money is negative.
    """

    if money < 0:
        raise ValueError("Money must be a non-negative integer.")

    coins = [10, 5, 1]
    count = 0
    for coin in coins:
        count += money // coin
        money %= coin
    return count


if __name__ == "__main__":
    m = int(input())
    print(change(m))
