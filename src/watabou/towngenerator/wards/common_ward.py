"""Common ward type for residential areas."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class CommonWard(Ward):
    """Common/residential ward type."""
    
    def __init__(self, model: 'Model', patch: 'Patch', 
                 min_sq: float, grid_chaos: float, size_chaos: float, 
                 empty_prob: float = 0.04):
        """Initialize a common ward."""
        super().__init__(model, patch)
        
        self.min_sq = min_sq
        self.grid_chaos = grid_chaos
        self.size_chaos = size_chaos
        self.empty_prob = empty_prob
    
    def create_geometry(self) -> None:
        """Create the geometric layout of this ward."""
        block = self.get_city_block()
        # Note: create_alleys method needs to be implemented in Ward base class
        # self.geometry = Ward.create_alleys(block, self.min_sq, self.grid_chaos, 
        #                                    self.size_chaos, self.empty_prob)
        
        # if not self.model.is_enclosed(self.patch):
        #     self.filter_outskirts()
        
        # Placeholder until full implementation
        self.geometry = [block]
