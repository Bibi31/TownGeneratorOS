"""State manager for handling application state."""
from ..utils.random import Random


class StateManager:
    """Manages application state including size and seed."""
    
    SIZE = "size"
    SEED = "seed"
    
    size: int = 15
    seed: int = -1
    
    @classmethod
    def pull_params(cls) -> None:
        """Pull parameters from URL/environment (stub for Python)."""
        # In Python, we could read from command line args or config
        pass
    
    @classmethod
    def push_params(cls) -> None:
        """Initialize random seed if not set."""
        if cls.seed == -1:
            Random.reset()
            cls.seed = Random.get_seed()
    
    @classmethod
    def get_state_name(cls) -> str:
        """Get the state name based on city size."""
        if cls.size >= 6 and cls.size < 10:
            return "Small Town"
        elif cls.size >= 10 and cls.size < 15:
            return "Large Town"
        elif cls.size >= 15 and cls.size < 24:
            return "Small City"
        elif cls.size >= 24 and cls.size < 40:
            return "Large City"
        elif cls.size >= 40:
            return "Metropolis"
        else:
            return "Unknown state"
