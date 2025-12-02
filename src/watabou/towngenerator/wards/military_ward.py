"""Military ward type."""
from typing import TYPE_CHECKING
import math
from .ward import Ward
from ...utils.random import Random

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class MilitaryWard(Ward):
    """Military district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a military ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create military ward geometry."""
        block = self.get_city_block()
        
        # Note: Requires Ward.create_alleys implementation
        # min_sq = math.sqrt(block.square) * (1 + Random.float())
        # grid_chaos = 0.1 + Random.float() * 0.3  # regular
        # size_chaos = 0.3
        # empty_prob = 0.25  # squares
        # self.geometry = Ward.create_alleys(block, min_sq, grid_chaos, size_chaos, empty_prob)
        
        # Placeholder
        self.geometry = [block]
    
    @staticmethod
    def rate_location(model: 'Model', patch: 'Patch') -> float:
        """Rate location (should border citadel or city walls)."""
        if model.citadel is not None and model.citadel.shape.borders(patch.shape):
            return 0.0
        elif model.wall is not None and model.wall.borders(patch):
            return 1.0
        else:
            return 0.0 if (model.citadel is None and model.wall is None) else math.inf
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Military"
