"""Merchant ward type."""
from typing import TYPE_CHECKING
from .common_ward import CommonWard
from ...utils.random import Random

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class MerchantWard(CommonWard):
    """Ward for merchants and traders."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a merchant ward."""
        min_sq = 50 + 60 * Random.float() * Random.float()  # medium to large
        grid_chaos = 0.5 + Random.float() * 0.3  # moderately regular
        size_chaos = 0.7
        empty_prob = 0.15
        
        super().__init__(model, patch, min_sq, grid_chaos, size_chaos, empty_prob)
    
    @staticmethod
    def rate_location(model: 'Model', patch: 'Patch') -> float:
        """Rate this location for a merchant ward (closer to center is better)."""
        center = model.plaza.shape.center if model.plaza is not None else model.center
        return patch.shape.distance(center)
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Merchant"
