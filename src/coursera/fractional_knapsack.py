from sys import stdin


def optimal_value(capacity: int, weights: list[int], values: list[int]) -> float:
    """Compute the optimal value of items that fit into the backpack.

    Args:
        capacity (int): The maximum weight capacity of the backpack.
        weights (list of int): The weights of the items.
        values (list of int): The values of the items.

    Returns:
        float: The maximum value of items that fit into the backpack.

    Raises:
        ValueError: If capacity is negative or if weights and values lists have different lengths.
    """
    if capacity < 0:
        raise ValueError("Capacity must be non-negative.")
    if len(weights) != len(values):
        raise ValueError("Weights and values lists must have the same length.")

    index = list(range(len(values)))
    ratio = [v / w for v, w in zip(values, weights, strict=True)]
    index.sort(key=lambda i: ratio[i], reverse=True)

    total_value = 0.0
    for i in index:
        if weights[i] <= capacity:
            total_value += values[i]
            capacity -= weights[i]
        else:
            total_value += values[i] * capacity / weights[i]
            break
    return total_value


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2 : (2 * n + 2) : 2]
    weights = data[3 : (2 * n + 2) : 2]
    opt_value = optimal_value(capacity, weights, values)
    print(f"{opt_value:.10f}")
