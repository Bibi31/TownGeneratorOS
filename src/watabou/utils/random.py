"""Random number generator using a linear congruential generator."""
import time


class Random:
    """Random number generator with seed support."""
    
    _G = 48271.0
    _N = 2147483647
    _seed = 1
    
    @classmethod
    def reset(cls, seed: int = -1) -> None:
        """Reset the random seed."""
        if seed != -1:
            cls._seed = seed
        else:
            cls._seed = int(time.time() * 1000) % cls._N
    
    @classmethod
    def get_seed(cls) -> int:
        """Get the current seed."""
        return cls._seed
    
    @classmethod
    def _next(cls) -> int:
        """Generate next random number."""
        cls._seed = int((cls._seed * cls._G) % cls._N)
        return cls._seed
    
    @classmethod
    def float(cls) -> float:
        """Generate a random float between 0 and 1."""
        return cls._next() / cls._N
    
    @classmethod
    def normal(cls) -> float:
        """Generate a random float with normal-like distribution."""
        return (cls.float() + cls.float() + cls.float()) / 3
    
    @classmethod
    def int(cls, min_val: int, max_val: int) -> int:
        """Generate a random integer between min and max (exclusive)."""
        return int(min_val + cls._next() / cls._N * (max_val - min_val))
    
    @classmethod
    def bool(cls, chance: float = 0.5) -> bool:
        """Generate a random boolean with given probability."""
        return cls.float() < chance
    
    @classmethod
    def fuzzy(cls, f: float = 1.0) -> float:
        """Generate a fuzzy random value."""
        if f == 0:
            return 0.5
        else:
            return (1 - f) / 2 + f * cls.normal()
