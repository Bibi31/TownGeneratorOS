"""Geometry utility functions."""
import math
from typing import Optional
from ..utils.point import Point


def intersect_lines(x1: float, y1: float, dx1: float, dy1: float,
                   x2: float, y2: float, dx2: float, dy2: float) -> Optional[Point]:
    """Find intersection parameters of two lines."""
    d = dx1 * dy2 - dy1 * dx2
    if d == 0:
        return None
    
    t2 = (dy1 * (x2 - x1) - dx1 * (y2 - y1)) / d
    if dx1 != 0:
        t1 = (x2 - x1 + dx2 * t2) / dx1
    else:
        t1 = (y2 - y1 + dy2 * t2) / dy1
    
    return Point(t1, t2)


def interpolate(p1: Point, p2: Point, ratio: float = 0.5) -> Point:
    """Interpolate between two points."""
    d = p2.subtract(p1)
    return Point(p1.x + d.x * ratio, p1.y + d.y * ratio)


def scalar(x1: float, y1: float, x2: float, y2: float) -> float:
    """Compute scalar/dot product."""
    return x1 * x2 + y1 * y2


def cross(x1: float, y1: float, x2: float, y2: float) -> float:
    """Compute cross product."""
    return x1 * y2 - y1 * x2


def distance_to_line(x1: float, y1: float, dx1: float, dy1: float,
                     x0: float, y0: float) -> float:
    """Compute distance from a point to a line."""
    return ((dx1 * y0 - dy1 * x0 + (y1 + dy1) * x1 - (x1 + dx1) * y1) / 
            math.sqrt(dx1 * dx1 + dy1 * dy1))
