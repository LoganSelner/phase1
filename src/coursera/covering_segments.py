from collections import namedtuple
from sys import stdin

Segment = namedtuple("Segment", "start end")


def optimal_points(segments: list[Segment]) -> list[int]:
    """Find the minimum number of points to cover all segments.

    Args:
        segments (list of Segment): A list of segments defined by their start and end points.

    Returns:
        list of int: A list of points that cover all segments.
    """
    # Sort segments by their end points
    segments.sort(key=lambda segment: segment.end)
    points = []
    current_point = -float("inf")
    for s in segments:
        if s.start > current_point:
            current_point = s.end
            points.append(current_point)
    return points


if __name__ == "__main__":
    input = stdin.read()
    n, *data = map(int, input.split())
    segments = list(
        map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2], strict=True))
    )
    points = optimal_points(segments)
    print(len(points))
    print(*points)
