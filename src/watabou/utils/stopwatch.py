"""Stopwatch utility for timing operations."""
import time
from typing import Callable


class Stopwatch:
    """Simple stopwatch for timing operations."""
    
    _start_time = 0
    
    @classmethod
    def start(cls) -> None:
        """Start the stopwatch."""
        cls._start_time = int(time.time() * 1000)
    
    @classmethod
    def lap(cls) -> int:
        """Get elapsed time without resetting."""
        return int(time.time() * 1000) - cls._start_time
    
    @classmethod
    def next(cls) -> int:
        """Get elapsed time and reset."""
        cur_time = int(time.time() * 1000)
        result = cur_time - cls._start_time
        cls._start_time = cur_time
        return result
    
    @classmethod
    def measure(cls, fn: Callable[[], None]) -> int:
        """Measure execution time of a function."""
        cls.start()
        fn()
        return cls.next()
