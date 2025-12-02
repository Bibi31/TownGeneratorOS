"""String utility functions."""
from typing import List, Any


def capitalize(s: str) -> str:
    """Capitalize the first letter of a string."""
    return s[0].upper() + s[1:] if len(s) > 0 else s


def enumerate_list(a: List[Any]) -> str:
    """Convert a list to an enumerated string with 'and' before the last item."""
    if len(a) == 0:
        return ""
    elif len(a) == 1:
        return str(a[0])
    else:
        return ", ".join(str(x) for x in a[:-1]) + " and " + str(a[-1])


def plural(s: str) -> str:
    """Return the plural form of a word."""
    if len(s) >= 3 and s[-3:] == "man":
        return s[:-3] + "men"
    elif len(s) > 0 and s[-1] == "s":
        return s + "es"
    else:
        return s + "s"


def genitive(s: str) -> str:
    """Return the genitive form of a word."""
    return s + "'" if len(s) > 0 and s[-1] == "s" else s + "'s"
