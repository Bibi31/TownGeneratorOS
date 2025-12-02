"""Math utility functions."""


def gate(value: float, min_val: float, max_val: float) -> float:
    """Clamp a value between min and max."""
    return min_val if value < min_val else (value if value < max_val else max_val)


def gatei(value: int, min_val: int, max_val: int) -> int:
    """Clamp an integer value between min and max."""
    return min_val if value < min_val else (value if value < max_val else max_val)


def sign(value: float) -> int:
    """Return the sign of a value: -1, 0, or 1."""
    return 0 if value == 0 else (-1 if value < 0 else 1)
