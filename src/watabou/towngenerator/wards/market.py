"""Market ward type."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Market(Ward):
    """Market district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a market ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create market geometry."""
        block = self.get_city_block()
        # Markets have special geometry - stalls and open spaces
        # Placeholder implementation
        self.geometry = [block]
