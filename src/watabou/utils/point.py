"""Point class and utility functions."""
import math
from typing import Tuple


class Point:
    """2D point class."""
    
    def __init__(self, x: float = 0.0, y: float = 0.0):
        """Initialize a point."""
        self.x = x
        self.y = y
    
    def set(self, other: 'Point') -> None:
        """Set this point's coordinates from another point."""
        self.x = other.x
        self.y = other.y
    
    def set_to(self, x: float, y: float) -> None:
        """Set this point's coordinates."""
        self.x = x
        self.y = y
    
    def clone(self) -> 'Point':
        """Create a copy of this point."""
        return Point(self.x, self.y)
    
    def add(self, other: 'Point') -> 'Point':
        """Add another point and return new point."""
        return Point(self.x + other.x, self.y + other.y)
    
    def subtract(self, other: 'Point') -> 'Point':
        """Subtract another point and return new point."""
        return Point(self.x - other.x, self.y - other.y)
    
    def scale(self, f: float) -> 'Point':
        """Scale this point and return new point."""
        return Point(self.x * f, self.y * f)
    
    def add_eq(self, other: 'Point') -> None:
        """Add another point in-place."""
        self.x += other.x
        self.y += other.y
    
    def sub_eq(self, other: 'Point') -> None:
        """Subtract another point in-place."""
        self.x -= other.x
        self.y -= other.y
    
    def scale_eq(self, f: float) -> None:
        """Scale this point in-place."""
        self.x *= f
        self.y *= f
    
    def offset(self, dx: float, dy: float) -> None:
        """Offset this point."""
        self.x += dx
        self.y += dy
    
    @property
    def length(self) -> float:
        """Get the length/magnitude of this point."""
        return math.sqrt(self.x * self.x + self.y * self.y)
    
    def normalize(self, length: float = 1.0) -> None:
        """Normalize this point to given length."""
        l = self.length
        if l != 0:
            self.x = self.x / l * length
            self.y = self.y / l * length
    
    def norm(self, length: float = 1.0) -> 'Point':
        """Return a normalized copy of this point."""
        p = self.clone()
        p.normalize(length)
        return p
    
    def atan(self) -> float:
        """Get the angle of this point."""
        return math.atan2(self.y, self.x)
    
    def dot(self, other: 'Point') -> float:
        """Dot product with another point."""
        return self.x * other.x + self.y * other.y
    
    def rotate90(self) -> 'Point':
        """Rotate 90 degrees counter-clockwise."""
        return Point(-self.y, self.x)
    
    @staticmethod
    def distance(p1: 'Point', p2: 'Point') -> float:
        """Calculate distance between two points."""
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        return math.sqrt(dx * dx + dy * dy)
    
    def __eq__(self, other: object) -> bool:
        """Check if two points are equal."""
        if not isinstance(other, Point):
            return False
        return self.x == other.x and self.y == other.y
    
    def __hash__(self) -> int:
        """Hash function for point."""
        return hash((self.x, self.y))
    
    def __repr__(self) -> str:
        """String representation."""
        return f"Point({self.x}, {self.y})"
