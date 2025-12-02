"""Cathedral ward type."""
from typing import TYPE_CHECKING
from .ward import Ward
from ...utils.random import Random

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Cathedral(Ward):
    """Cathedral/temple district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a cathedral ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create cathedral geometry."""
        block = self.get_city_block()
        
        # Note: Requires Cutter.ring implementation
        # if Random.bool(0.4):
        #     self.geometry = Cutter.ring(block, 2 + Random.float() * 4)
        # else:
        #     self.geometry = Ward.create_ortho_building(block, 50, 0.8)
        
        # Placeholder
        self.geometry = [block]
    
    @staticmethod
    def rate_location(model: 'Model', patch: 'Patch') -> float:
        """Rate location (prefers to overlook plaza or be close to center)."""
        if model.plaza is not None and patch.shape.borders(model.plaza.shape):
            return -1 / patch.shape.square
        else:
            center = model.plaza.shape.center if model.plaza is not None else model.center
            return patch.shape.distance(center) * patch.shape.square
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Temple"
