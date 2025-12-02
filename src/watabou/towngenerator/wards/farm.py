"""Farm ward type."""
from typing import TYPE_CHECKING
from .ward import Ward

if TYPE_CHECKING:
    from ..building.patch import Patch
    from ..building.model import Model


class Farm(Ward):
    """Farm district ward."""
    
    def __init__(self, model: 'Model', patch: 'Patch'):
        """Initialize a farm ward."""
        super().__init__(model, patch)
    
    def create_geometry(self) -> None:
        """Create farm geometry (mostly empty with few buildings)."""
        # Farms have minimal geometry
        self.geometry = []
    
    def get_label(self) -> str:
        """Get the label for this ward type."""
        return "Farm"
