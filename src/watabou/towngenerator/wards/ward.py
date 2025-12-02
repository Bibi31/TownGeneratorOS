"""Base Ward class for city districts."""
from typing import List, Optional, TYPE_CHECKING
from ...geom.polygon import Polygon
from ...utils.point import Point

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Ward:
    """Base class for city ward/district types."""
    
    # Street width constants
    MAIN_STREET = 2.0
    REGULAR_STREET = 1.0
    ALLEY = 0.6
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a ward."""
        self.model = model
        self.patch = patch
        self.geometry: List[Polygon] = []
    
    def create_geometry(self) -> None:
        """Create the geometric representation of this ward."""
        self.geometry = []
    
    def get_city_block(self) -> Polygon:
        """Get the city block polygon with streets inset."""
        inset_dist: List[float] = []
        
        inner_patch = self.model.wall is None or self.patch.within_walls
        
        def calculate_inset(v0: Point, v1: Point) -> None:
            if self.model.wall is not None and self.model.wall.borders_by(self.patch, v0, v1):
                # Not too close to the wall
                inset_dist.append(Ward.MAIN_STREET / 2)
            else:
                on_street = inner_patch and (
                    self.model.plaza is not None and 
                    self.model.plaza.shape.find_edge(v1, v0) != -1
                )
                
                if not on_street:
                    for street in self.model.arteries:
                        if street.contains(v0) and street.contains(v1):
                            on_street = True
                            break
                
                if on_street:
                    inset_dist.append(Ward.MAIN_STREET / 2)
                elif inner_patch:
                    inset_dist.append(Ward.REGULAR_STREET / 2)
                else:
                    inset_dist.append(Ward.ALLEY / 2)
        
        self.patch.shape.for_edge(calculate_inset)
        
        if self.patch.shape.is_convex():
            return self.patch.shape.shrink_eq(inset_dist[0]) if len(set(inset_dist)) == 1 else self.patch.shape
        else:
            # Buffer method not fully implemented in polygon.py yet
            return self.patch.shape
