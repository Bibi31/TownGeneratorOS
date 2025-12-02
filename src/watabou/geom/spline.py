"""Spline utilities for smooth curves."""
from typing import List
from ..utils.point import Point


class Spline:
    """Spline curve utilities."""
    
    curvature = 0.1
    
    @staticmethod
    def start_curve(p0: Point, p1: Point, p2: Point) -> List[Point]:
        """Create start curve control points."""
        tangent = p2.subtract(p0)
        control = p1.subtract(tangent.scale(Spline.curvature))
        return [control, p1]
    
    @staticmethod
    def end_curve(p0: Point, p1: Point, p2: Point) -> List[Point]:
        """Create end curve control points."""
        tangent = p2.subtract(p0)
        control = p1.add(tangent.scale(Spline.curvature))
        return [control, p2]
    
    @staticmethod
    def mid_curve(p0: Point, p1: Point, p2: Point, p3: Point) -> List[Point]:
        """Create middle curve control points."""
        dir_v = p2.subtract(p1)
        tangent1 = p2.subtract(p0)
        tangent2 = p3.subtract(p1)
        
        p1a = p1.add(tangent1.scale(Spline.curvature))
        p2a = p2.subtract(tangent2.scale(Spline.curvature))
        p12 = p1a.add(p2a).scale(0.5)
        
        return [p1a, p12, p2a, p2]
