"""Polygon class for geometric operations."""
import math
from typing import List, Callable, Optional, Tuple
from ..utils.point import Point
from ..utils.math_utils import sign
from .geom_utils import cross as geom_cross, intersect_lines


class Rectangle:
    """Simple rectangle class."""
    
    def __init__(self, x: float = 0, y: float = 0, width: float = 0, height: float = 0):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    
    @property
    def left(self) -> float:
        return self.x
    
    @left.setter
    def left(self, value: float):
        self.width = self.x + self.width - value
        self.x = value
    
    @property
    def right(self) -> float:
        return self.x + self.width
    
    @right.setter
    def right(self, value: float):
        self.width = value - self.x
    
    @property
    def top(self) -> float:
        return self.y
    
    @top.setter
    def top(self, value: float):
        self.height = self.y + self.height - value
        self.y = value
    
    @property
    def bottom(self) -> float:
        return self.y + self.height
    
    @bottom.setter
    def bottom(self, value: float):
        self.height = value - self.y


class Polygon:
    """Polygon class represented as a list of vertices."""
    
    DELTA = 0.000001
    
    def __init__(self, vertices: Optional[List[Point]] = None):
        """Initialize a polygon."""
        if vertices is not None:
            self.vertices = [p.clone() for p in vertices]
        else:
            self.vertices = []
    
    def __len__(self) -> int:
        """Get number of vertices."""
        return len(self.vertices)
    
    def __getitem__(self, index: int) -> Point:
        """Get vertex at index."""
        return self.vertices[index]
    
    def __setitem__(self, index: int, value: Point):
        """Set vertex at index."""
        self.vertices[index] = value
    
    def __iter__(self):
        """Iterate over vertices."""
        return iter(self.vertices)
    
    def set(self, p: 'Polygon') -> None:
        """Set vertices from another polygon."""
        for i in range(len(p)):
            self.vertices[i].set(p[i])
    
    @property
    def square(self) -> float:
        """Calculate area of polygon."""
        v1 = self.last()
        v2 = self.vertices[0]
        s = v1.x * v2.y - v2.x * v1.y
        for i in range(1, len(self.vertices)):
            v1 = v2
            v2 = self.vertices[i]
            s += (v1.x * v2.y - v2.x * v1.y)
        return s * 0.5
    
    @property
    def perimeter(self) -> float:
        """Calculate perimeter of polygon."""
        length = 0.0
        
        def add_length(v0: Point, v1: Point):
            nonlocal length
            length += Point.distance(v0, v1)
        
        self.for_edge(add_length)
        return length
    
    @property
    def compactness(self) -> float:
        """Calculate compactness (circle=1.0, square=0.79, triangle=0.60)."""
        p = self.perimeter
        return 4 * math.pi * self.square / (p * p)
    
    @property
    def center(self) -> Point:
        """Get approximate center (faster than centroid)."""
        c = Point()
        for v in self.vertices:
            c.add_eq(v)
        c.scale_eq(1 / len(self.vertices))
        return c
    
    @property
    def centroid(self) -> Point:
        """Get true centroid of polygon."""
        x = 0.0
        y = 0.0
        a = 0.0
        
        def accumulate(v0: Point, v1: Point):
            nonlocal x, y, a
            f = geom_cross(v0.x, v0.y, v1.x, v1.y)
            a += f
            x += (v0.x + v1.x) * f
            y += (v0.y + v1.y) * f
        
        self.for_edge(accumulate)
        s6 = 1 / (3 * a)
        return Point(s6 * x, s6 * y)
    
    def contains(self, v: Point) -> bool:
        """Check if polygon contains a vertex."""
        return v in self.vertices
    
    def for_edge(self, f: Callable[[Point, Point], None]) -> None:
        """Iterate over all edges (including last-to-first)."""
        length = len(self.vertices)
        for i in range(length):
            f(self.vertices[i], self.vertices[(i + 1) % length])
    
    def for_segment(self, f: Callable[[Point, Point], None]) -> None:
        """Iterate over segments (excluding last-to-first)."""
        for i in range(len(self.vertices) - 1):
            f(self.vertices[i], self.vertices[i + 1])
    
    def offset(self, p: Point) -> None:
        """Offset all vertices by a point."""
        dx = p.x
        dy = p.y
        for v in self.vertices:
            v.offset(dx, dy)
    
    def rotate(self, a: float) -> None:
        """Rotate polygon by angle."""
        cos_a = math.cos(a)
        sin_a = math.sin(a)
        for v in self.vertices:
            vx = v.x * cos_a - v.y * sin_a
            vy = v.y * cos_a + v.x * sin_a
            v.set_to(vx, vy)
    
    def is_convex_vertexi(self, i: int) -> bool:
        """Check if vertex at index i is convex."""
        length = len(self.vertices)
        v0 = self.vertices[(i + length - 1) % length]
        v1 = self.vertices[i]
        v2 = self.vertices[(i + 1) % length]
        return geom_cross(v1.x - v0.x, v1.y - v0.y, v2.x - v1.x, v2.y - v1.y) > 0
    
    def is_convex_vertex(self, v1: Point) -> bool:
        """Check if a vertex is convex."""
        v0 = self.prev(v1)
        v2 = self.next(v1)
        return geom_cross(v1.x - v0.x, v1.y - v0.y, v2.x - v1.x, v2.y - v1.y) > 0
    
    def is_convex(self) -> bool:
        """Check if polygon is convex."""
        for v in self.vertices:
            if not self.is_convex_vertex(v):
                return False
        return True
    
    def smooth_vertexi(self, i: int, f: float = 1.0) -> Point:
        """Smooth vertex at index i."""
        v = self.vertices[i]
        length = len(self.vertices)
        prev = self.vertices[(i + length - 1) % length]
        next_v = self.vertices[(i + 1) % length]
        result = Point(
            (prev.x + v.x * f + next_v.x) / (2 + f),
            (prev.y + v.y * f + next_v.y) / (2 + f)
        )
        return result
    
    def smooth_vertex(self, v: Point, f: float = 1.0) -> Point:
        """Smooth a specific vertex."""
        prev = self.prev(v)
        next_v = self.next(v)
        return Point(
            prev.x + v.x * f + next_v.x,
            prev.y + v.y * f + next_v.y
        ).scale(1 / (2 + f))
    
    def distance(self, p: Point) -> float:
        """Get minimum distance from vertices to point."""
        v0 = self.vertices[0]
        d = Point.distance(v0, p)
        for i in range(1, len(self.vertices)):
            v1 = self.vertices[i]
            d1 = Point.distance(v1, p)
            if d1 < d:
                v0 = v1
                d = d1
        return d
    
    def smooth_vertex_eq(self, f: float = 1.0) -> 'Polygon':
        """Smooth all vertices equally."""
        length = len(self.vertices)
        v1 = self.vertices[length - 1]
        v2 = self.vertices[0]
        result = []
        for i in range(length):
            v0 = v1
            v1 = v2
            v2 = self.vertices[(i + 1) % length]
            result.append(Point(
                (v0.x + v1.x * f + v2.x) / (2 + f),
                (v0.y + v1.y * f + v2.y) / (2 + f)
            ))
        return Polygon(result)
    
    def filter_short(self, threshold: float) -> 'Polygon':
        """Filter out short segments."""
        if len(self.vertices) < 2:
            return Polygon(self.vertices)
        
        i = 1
        v0 = self.vertices[0]
        v1 = self.vertices[1]
        result = [v0]
        
        while i < len(self.vertices):
            while Point.distance(v0, v1) < threshold and i < len(self.vertices):
                i += 1
                if i < len(self.vertices):
                    v1 = self.vertices[i]
            result.append(v1)
            v0 = v1
            i += 1
            if i < len(self.vertices):
                v1 = self.vertices[i]
        
        return Polygon(result)
    
    def inset(self, p1: Point, d: float) -> None:
        """Inset an edge starting at vertex p1."""
        i1 = self.vertices.index(p1)
        i0 = i1 - 1 if i1 > 0 else len(self.vertices) - 1
        p0 = self.vertices[i0]
        i2 = i1 + 1 if i1 < len(self.vertices) - 1 else 0
        p2 = self.vertices[i2]
        i3 = i2 + 1 if i2 < len(self.vertices) - 1 else 0
        p3 = self.vertices[i3]
        
        v0 = p1.subtract(p0)
        v1 = p2.subtract(p1)
        v2 = p3.subtract(p2)
        
        # Avoid division by zero
        len0 = v0.length
        len1 = v1.length
        if len0 == 0 or len1 == 0:
            return
        
        cos = v0.dot(v1) / len0 / len1
        z = v0.x * v1.y - v0.y * v1.x
        
        # Avoid sqrt of negative and division by zero
        sin_sq = 1 - cos * cos
        if sin_sq <= 0:
            return
        
        t = d / math.sqrt(sin_sq)
        if z > 0:
            t = min(t, v0.length * 0.99)
        else:
            t = min(t, v1.length * 0.5)
        t *= sign(z)
        self.vertices[i1] = p1.subtract(v0.norm(t))
        
        # Avoid division by zero for second calculation
        len2 = v2.length
        if len1 == 0 or len2 == 0:
            return
        
        cos = v1.dot(v2) / len1 / len2
        z = v1.x * v2.y - v1.y * v2.x
        
        sin_sq = 1 - cos * cos
        if sin_sq <= 0:
            return
        
        t = d / math.sqrt(sin_sq)
        if z > 0:
            t = min(t, v2.length * 0.99)
        else:
            t = min(t, v1.length * 0.5)
        self.vertices[i2] = p2.add(v2.norm(t))
    
    def inset_all(self, d: List[float]) -> 'Polygon':
        """Inset all edges by specified distances."""
        p = Polygon(self.vertices)
        for i in range(len(p)):
            if d[i] != 0:
                p.inset(p[i], d[i])
        return p
    
    def inset_eq(self, d: float) -> None:
        """Inset all edges by same distance."""
        for i in range(len(self.vertices)):
            self.inset(self.vertices[i], d)
    
    def push(self, v: Point) -> None:
        """Add a vertex to the polygon."""
        self.vertices.append(v)
    
    def insert(self, index: int, v: Point) -> None:
        """Insert a vertex at index."""
        self.vertices.insert(index, v)
    
    def unshift(self, v: Point) -> None:
        """Add a vertex at the beginning."""
        self.vertices.insert(0, v)
    
    def last(self) -> Point:
        """Get the last vertex."""
        return self.vertices[-1]
    
    def index_of(self, v: Point) -> int:
        """Get index of a vertex."""
        try:
            return self.vertices.index(v)
        except ValueError:
            return -1
    
    def find_edge(self, a: Point, b: Point) -> int:
        """Find edge index from vertex a to vertex b."""
        index = self.index_of(a)
        if index != -1 and self.vertices[(index + 1) % len(self.vertices)] == b:
            return index
        return -1
    
    def next(self, a: Point) -> Point:
        """Get next vertex after a."""
        return self.vertices[(self.vertices.index(a) + 1) % len(self.vertices)]
    
    def prev(self, a: Point) -> Point:
        """Get previous vertex before a."""
        return self.vertices[(self.vertices.index(a) + len(self.vertices) - 1) % len(self.vertices)]
    
    def vector(self, v: Point) -> Point:
        """Get edge vector starting at v."""
        return self.next(v).subtract(v)
    
    def vectori(self, i: int) -> Point:
        """Get edge vector at index i."""
        next_i = 0 if i == len(self.vertices) - 1 else i + 1
        return self.vertices[next_i].subtract(self.vertices[i])
    
    def borders(self, another: 'Polygon') -> bool:
        """Check if this polygon shares an edge with another."""
        len1 = len(self.vertices)
        len2 = len(another.vertices)
        for i in range(len1):
            j = another.index_of(self.vertices[i])
            if j != -1:
                next_v = self.vertices[(i + 1) % len1]
                if (next_v == another.vertices[(j + 1) % len2] or
                    next_v == another.vertices[(j + len2 - 1) % len2]):
                    return True
        return False
    
    def get_bounds(self) -> Rectangle:
        """Get bounding rectangle."""
        rect = Rectangle(self.vertices[0].x, self.vertices[0].y)
        for v in self.vertices:
            rect.left = min(rect.left, v.x)
            rect.right = max(rect.right, v.x)
            rect.top = min(rect.top, v.y)
            rect.bottom = max(rect.bottom, v.y)
        return rect
    
    def split(self, p1: Point, p2: Point) -> List['Polygon']:
        """Split polygon at two vertices."""
        return self.spliti(self.vertices.index(p1), self.vertices.index(p2))
    
    def spliti(self, i1: int, i2: int) -> List['Polygon']:
        """Split polygon at two indices."""
        if i1 > i2:
            i1, i2 = i2, i1
        
        return [
            Polygon(self.vertices[i1:i2 + 1]),
            Polygon(self.vertices[i2:] + self.vertices[:i1 + 1])
        ]
    
    @staticmethod
    def rect(w: float = 1.0, h: float = 1.0) -> 'Polygon':
        """Create a rectangle polygon."""
        return Polygon([
            Point(-w/2, -h/2),
            Point(w/2, -h/2),
            Point(w/2, h/2),
            Point(-w/2, h/2)
        ])
    
    @staticmethod
    def regular(n: int = 8, r: float = 1.0) -> 'Polygon':
        """Create a regular polygon."""
        vertices = []
        for i in range(n):
            a = i / n * math.pi * 2
            vertices.append(Point(r * math.cos(a), r * math.sin(a)))
        return Polygon(vertices)
    
    @staticmethod
    def circle(r: float = 1.0) -> 'Polygon':
        """Create a circle-like polygon."""
        return Polygon.regular(16, r)
