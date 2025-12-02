"""Administration ward type."""
from typing import TYPE_CHECKING
from .common_ward import CommonWard
from ...utils.random import Random

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class AdministrationWard(CommonWard):
    """Ward for government and administration."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize an administration ward."""
        min_sq = 30 + 40 * Random.float() * Random.float()
        grid_chaos = 0.3 + Random.float() * 0.4
        size_chaos = 0.6
        empty_prob = 0.15
        
        super().__init__(model, patch, min_sq, grid_chaos, size_chaos, empty_prob)
    
    @staticmethod
    def rate_location(model: 'Model', patch: 'Patch') -> float:
        """Rate location for administration ward."""
        center = model.plaza.shape.center if model.plaza is not None else model.center
        return patch.shape.distance(center)
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Administration"
