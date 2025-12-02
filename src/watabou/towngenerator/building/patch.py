"""Patch class representing a city block or region."""
from typing import List, Optional, TYPE_CHECKING
from ...geom.polygon import Polygon
from ...utils.point import Point

if TYPE_CHECKING:
    from ..wards.ward import Ward


class Patch:
    """Represents a patch/region in the city."""
    
    def __init__(self, vertices: List[Point]):
        """Initialize a patch with vertices."""
        self.shape = Polygon(vertices)
        self.ward: Optional['Ward'] = None
        self.within_walls = False
        self.within_city = False
    
    @staticmethod
    def from_region(r) -> 'Patch':
        """Create patch from a Voronoi region."""
        # Note: This requires Voronoi implementation
        vertices = [tr.c for tr in r.vertices]
        return Patch(vertices)
