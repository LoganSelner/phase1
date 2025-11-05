from coursera.covering_segments import Segment, optimal_points


def test_optimal_points():
    # Basic test case
    segments = [
        Segment(1, 3),
        Segment(2, 5),
        Segment(3, 6),
    ]
    assert optimal_points(segments) == [3]

    # Overlapping segments
    segments = [
        Segment(0, 2),
        Segment(1, 3),
        Segment(2, 4),
    ]
    assert optimal_points(segments) == [2]

    # Non-overlapping segments
    segments = [
        Segment(0, 1),
        Segment(2, 3),
        Segment(4, 5),
    ]
    assert optimal_points(segments) == [1, 3, 5]

    # Mixed segments
    segments = [
        Segment(1, 4),
        Segment(2, 3),
        Segment(5, 6),
    ]
    assert optimal_points(segments) == [3, 6]

    # Single segment
    segments = [Segment(0, 10)]
    assert optimal_points(segments) == [10]

    # Empty list of segments
    segments = []
    assert optimal_points(segments) == []
