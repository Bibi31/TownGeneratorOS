"""Craftsmen ward type."""
from typing import TYPE_CHECKING
from .common_ward import CommonWard

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class CraftsmenWard(CommonWard):
    """Ward for craftsmen and artisans."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a craftsmen ward."""
        super().__init__(model, patch, 
                        min_sq=12.0,
                        grid_chaos=0.2,
                        size_chaos=0.3)
