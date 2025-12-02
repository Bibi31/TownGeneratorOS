"""Observable pattern implementation."""
from typing import TypeVar, Callable, List, Generic

T = TypeVar('T')


class Observable(Generic[T]):
    """Observable value with change notification."""
    
    def __init__(self, v: T):
        """Initialize with a value."""
        self._value = v
        self._listeners: List[Callable[[T], None]] = []
    
    @property
    def value(self) -> T:
        """Get the current value."""
        return self._value
    
    @value.setter
    def value(self, v: T) -> None:
        """Set the value and notify listeners."""
        self._value = v
        for listener in self._listeners:
            listener(self._value)
    
    def add_listener(self, listener: Callable[[T], None]) -> None:
        """Add a change listener."""
        self._listeners.append(listener)
    
    def remove_listener(self, listener: Callable[[T], None]) -> None:
        """Remove a change listener."""
        if listener in self._listeners:
            self._listeners.remove(listener)


class ObservableInt(Observable[int]):
    """Observable integer with min/max bounds."""
    
    def __init__(self, v: int, min_val: int, max_val: int):
        """Initialize with value and bounds."""
        super().__init__(v)
        self.min = min_val
        self.max = max_val
        self._listeners2: List[Callable[[int, int], None]] = []
    
    @property
    def value(self) -> int:
        """Get the current value."""
        return self._value
    
    @value.setter
    def value(self, v: int) -> None:
        """Set the value (clamped to bounds) and notify listeners."""
        from .math_utils import gatei
        old = self._value
        v = gatei(v, self.min, self.max)
        for listener in self._listeners2:
            listener(v, v - old)
        self._value = v
        for listener in self._listeners:
            listener(self._value)
    
    def add_listener2(self, listener: Callable[[int, int], None]) -> None:
        """Add a change listener with delta."""
        self._listeners2.append(listener)
    
    def remove_listener2(self, listener: Callable[[int, int], None]) -> None:
        """Remove a change listener."""
        if listener in self._listeners2:
            self._listeners2.remove(listener)
