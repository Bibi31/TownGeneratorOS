"""Castle ward type."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Castle(Ward):
    """Castle district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a castle ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create castle geometry."""
        block = self.get_city_block()
        # Castle has large central structure
        # Placeholder implementation
        self.geometry = [block]
