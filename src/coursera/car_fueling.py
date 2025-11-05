from sys import stdin


# Compute the minimum number of gas tank refills to get from one city to another
def min_refills(distance: int, tank: int, stops: list[int]) -> int:
    """Calculate the minimum number of refills needed to reach the destination.

    Args:
        distance (int): The total distance to the destination.
        tank (int): The maximum distance the car can travel on a full tank.
        stops (list of int): The distances of the gas stations from the starting point.

    Returns:
        int: The minimum number of refills needed, or -1 if the destination cannot be reached.

    Raises:
        ValueError: If distance or tank is negative, or if any stop is out of bounds
    """
    if distance < 0 or tank < 0:
        raise ValueError("Distance and tank capacity must be non-negative.")
    if any(stop < 0 or stop > distance for stop in stops):
        raise ValueError("All stops must be within the range of the distance.")

    # Calculate the minimum number of refills needed
    num_refills = 0
    current_position = 0
    stops.append(distance)  # Add the final destination as a stop

    for i, stop in enumerate(stops):
        if stop - current_position > tank:
            # Need to refill
            prev_stop_unreachable = (i == 0) or (stops[i - 1] - current_position > tank)
            if prev_stop_unreachable:
                return -1  # Can't reach the next stop
            num_refills += 1
            current_position = stops[i - 1]

    if distance - current_position > tank:
        return -1  # Can't reach the destination

    return num_refills


if __name__ == "__main__":
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
