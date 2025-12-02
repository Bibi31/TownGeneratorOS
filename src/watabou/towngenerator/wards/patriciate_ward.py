"""Patriciate ward type for wealthy residents."""
from typing import TYPE_CHECKING
from .common_ward import CommonWard
from .park import Park
from .slum import Slum
from ...utils.random import Random

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class PatriciateWard(CommonWard):
    """Ward for wealthy patricians."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a patriciate ward."""
        min_sq = 80 + 30 * Random.float() * Random.float()  # large
        grid_chaos = 0.5 + Random.float() * 0.3  # moderately regular
        size_chaos = 0.8
        empty_prob = 0.2
        
        super().__init__(model, patch, min_sq, grid_chaos, size_chaos, empty_prob)
    
    @staticmethod
    def rate_location(model: 'Model', patch: 'Patch') -> float:
        """Rate location (prefers to border parks, avoid slums)."""
        rate = 0.0
        for p in model.patches:
            if p.ward is not None and p.shape.borders(patch.shape):
                if isinstance(p.ward, Park):
                    rate -= 1
                elif isinstance(p.ward, Slum):
                    rate += 1
        return rate
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Patriciate"
