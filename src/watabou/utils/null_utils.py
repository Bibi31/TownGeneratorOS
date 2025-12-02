"""Null/None utility functions."""
from typing import Any, List, TypeVar, Optional

T = TypeVar('T')


def float_or(value: Optional[float], def_value: float = 0.0) -> float:
    """Return value if not None, otherwise return default."""
    return def_value if value is None else value


def int_or(value: Optional[int], def_value: int = 0) -> int:
    """Return value if not None, otherwise return default."""
    return def_value if value is None else value


def bool_or(value: Optional[bool], def_value: bool = False) -> bool:
    """Return value if not None, otherwise return default."""
    return def_value if value is None else value


def string_or(value: Optional[str], def_value: str = "") -> str:
    """Return value if not None, otherwise return default."""
    return def_value if value is None else value


def array_or(value: Any) -> List[T]:
    """Return value as list if not None, otherwise return empty list."""
    if value is None:
        return []
    elif isinstance(value, list):
        return value
    else:
        return [value]


def or_empty(value: Optional[dict]) -> dict:
    """Return value if not None, otherwise return empty dict."""
    return {} if value is None else value
