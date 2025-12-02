"""Gate ward type."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class GateWard(Ward):
    """Gate ward for city entrances."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a gate ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create gate geometry."""
        # Gates have special geometry near walls
        block = self.get_city_block()
        self.geometry = [block]
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Gate"
