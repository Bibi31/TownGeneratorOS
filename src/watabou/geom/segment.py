"""Segment class for line segments."""
from ..utils.point import Point


class Segment:
    """Line segment defined by start and end points."""
    
    def __init__(self, start: Point, end: Point):
        """Initialize a segment."""
        self.start = start
        self.end = end
    
    @property
    def dx(self) -> float:
        """Get x difference."""
        return self.end.x - self.start.x
    
    @property
    def dy(self) -> float:
        """Get y difference."""
        return self.end.y - self.start.y
    
    @property
    def vector(self) -> Point:
        """Get vector from start to end."""
        return self.end.subtract(self.start)
    
    @property
    def length(self) -> float:
        """Get length of segment."""
        return Point.distance(self.start, self.end)
