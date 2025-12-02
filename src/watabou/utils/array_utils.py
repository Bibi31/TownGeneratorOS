"""Array utility functions."""
from typing import TypeVar, List, Callable, Optional
from .random import Random

T = TypeVar('T')
S = TypeVar('S')


def shuffle(a: List[T]) -> List[T]:
    """Shuffle an array randomly."""
    result = []
    for e in a:
        result.insert(int(Random.float() * (len(result) + 1)), e)
    return result


def random_choice(a: List[T]) -> T:
    """Get a random element from an array."""
    return a[int(Random.float() * len(a))]


def weighted(a: List[T], weights: List[float]) -> T:
    """Get a weighted random element from an array."""
    total = sum(weights)
    
    z = Random.float() * total
    acc = 0.0
    for i in range(len(a)):
        acc += weights[i]
        if z <= acc:
            return a[i]
    
    return a[0]


def contains(a: List[T], value: T) -> bool:
    """Check if array contains a value."""
    return value in a


def is_empty(a: List[T]) -> bool:
    """Check if array is empty."""
    return len(a) == 0


def last(a: List[T]) -> T:
    """Get the last element of an array."""
    return a[-1]


def min_by(a: List[T], f: Callable[[T], float]) -> T:
    """Get the element with minimum value according to function."""
    result = a[0]
    min_val = f(result)
    for i in range(1, len(a)):
        element = a[i]
        measure = f(element)
        if measure < min_val:
            result = element
            min_val = measure
    return result


def max_by(a: List[T], f: Callable[[T], float]) -> T:
    """Get the element with maximum value according to function."""
    result = a[0]
    max_val = f(result)
    for i in range(1, len(a)):
        element = a[i]
        measure = f(element)
        if measure > max_val:
            result = element
            max_val = measure
    return result


def every(a: List[T], test: Callable[[T], bool]) -> bool:
    """Check if all elements pass the test."""
    return all(test(e) for e in a)


def some(a: List[T], test: Callable[[T], bool]) -> bool:
    """Check if any element passes the test."""
    return any(test(e) for e in a)


def count(a: List[T], test: Callable[[T], bool]) -> int:
    """Count elements that pass the test."""
    return sum(1 for e in a if test(e))


def map_array(a: List[T], f: Callable[[T], S]) -> List[S]:
    """Map function over array."""
    return [f(el) for el in a]


def replace(a: List[T], el: T, new_els: List[T]) -> None:
    """Replace an element with multiple elements."""
    index = a.index(el)
    a[index] = new_els[0]
    for i in range(1, len(new_els)):
        a.insert(index + i, new_els[i])


def add(a: List[T], el: T) -> None:
    """Add element if not already present."""
    if el not in a:
        a.append(el)


def clean(a: List[T]) -> List[T]:
    """Remove duplicates from array."""
    seen = set()
    result = []
    for el in a:
        if el not in seen:
            seen.add(el)
            result.append(el)
    return result


def intersect(a: List[T], b: List[T]) -> List[T]:
    """Get intersection of two arrays."""
    return [el for el in a if el in b]


def union(a: List[T], b: List[T]) -> List[T]:
    """Get union of two arrays."""
    return a + [el for el in b if el not in a]


def remove_all(a: List[T], b: List[T]) -> None:
    """Remove all elements from b from a."""
    for el in b:
        if el in a:
            a.remove(el)


def difference(a: List[T], b: List[T]) -> List[T]:
    """Get elements in a but not in b."""
    return [el for el in a if el not in b]


def flatten(a: List[List[T]]) -> List[T]:
    """Flatten a 2D array."""
    if len(a) == 0:
        return []
    else:
        result = a[0].copy()
        for i in range(1, len(a)):
            result.extend(a[i])
        return result


def uflatten(a: List[List[T]]) -> List[T]:
    """Flatten a 2D array removing duplicates."""
    if len(a) == 0:
        return []
    else:
        result = a[0].copy()
        for i in range(1, len(a)):
            result = union(result, a[i])
        return result


def equals(a: List[T], b: List[T]) -> bool:
    """Check if two arrays contain the same elements (unordered)."""
    if len(a) != len(b):
        return False
    elif len(a) == 0:
        return True
    else:
        for el in a:
            if el not in b:
                return False
        return True
