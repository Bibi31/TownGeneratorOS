"""Markov chain implementation."""
from typing import TypeVar, List, Dict, Optional, Callable
import random

T = TypeVar('T')


class MarkovChain:
    """Markov chain for generating sequences."""
    
    def __init__(self):
        """Initialize the Markov chain."""
        self.table: Dict[Optional[T], '_FollowUp'] = {}
        self.is_terminal: Callable[[Optional[T]], bool] = lambda state: False
    
    def add_sample(self, sample: List[T]) -> None:
        """Add a sample sequence to the chain."""
        prev: Optional[T] = None
        for i in range(len(sample)):
            cur = sample[i]
            self._add_case(prev, cur)
            prev = cur
        self._add_case(prev, None)
    
    def _add_case(self, a: Optional[T], b: Optional[T]) -> None:
        """Add a single transition case."""
        if a not in self.table:
            self.table[a] = _FollowUp()
        self.table[a].observe(b)
    
    def generate(self) -> List[T]:
        """Generate a sequence using the Markov chain."""
        result: List[T] = []
        
        state: Optional[T] = None
        while True:
            state = self.get_next(state)
            if self.is_terminal(state):
                break
            if state is not None:
                result.append(state)
        
        return result
    
    def get_next(self, a: Optional[T]) -> Optional[T]:
        """Get the next state from current state."""
        return self.table[a].get()


class _FollowUp:
    """Internal class for tracking follow-up states."""
    
    def __init__(self):
        """Initialize follow-up tracker."""
        self.states: List = []
        self.weights: List[float] = []
    
    def observe(self, state) -> None:
        """Observe a state transition."""
        try:
            index = self.states.index(state)
            self.weights[index] += 1
        except ValueError:
            self.states.append(state)
            self.weights.append(1)
    
    def get(self):
        """Get a weighted random state."""
        if not self.states:
            return None
        
        total = sum(self.weights)
        r = random.random() * total
        cumsum = 0
        for i, weight in enumerate(self.weights):
            cumsum += weight
            if r < cumsum:
                return self.states[i]
        return self.states[-1]
