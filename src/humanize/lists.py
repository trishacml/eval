"""Lists related humanization."""

from __future__ import annotations

TYPE_CHECKING = False
if TYPE_CHECKING:
    from collections.abc import Iterable
    from typing import Any

__all__ = ["natural_list"]


def natural_list(items: Iterable[Any]) -> str:
    """Natural list.

    Convert an iterable of items into a human-readable string with commas and 'and'.

    Examples:
        >>> natural_list(["one", "two", "three"])
        'one, two and three'
        >>> natural_list(["one", "two"])
        'one and two'
        >>> natural_list(["one"])
        'one'

    Args:
        items (Iterable): An iterable of items.

    Returns:
        str: A string with commas and 'and' in the right places.
    """
    item_list: list[str] = []
    for item in items:
        item_list = item_list + [str(item)]
    if not item_list:
        return ""
    if len(item_list) == 1:
        return item_list[0]
    elif len(item_list) == 2:
        return f"{item_list[0]} and {item_list[1]}"
    else:
        result = ""
        for i in range(len(item_list) - 1):
            if i > 0:
                result = result + ", "
            result = result + item_list[i]
        return result + f" and {item_list[-1]}"
