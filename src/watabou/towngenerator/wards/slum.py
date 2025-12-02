"""Slum ward type."""
from typing import TYPE_CHECKING
from .common_ward import CommonWard

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Slum(CommonWard):
    """Slum district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a slum ward."""
        super().__init__(model, patch,
                        min_sq=8.0,
                        grid_chaos=0.4,
                        size_chaos=0.5,
                        empty_prob=0.08)
