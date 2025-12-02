"""Park ward type."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Park(Ward):
    """Park district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a park ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create park geometry (empty - parks have no buildings)."""
        self.geometry = []
