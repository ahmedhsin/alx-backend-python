#!/usr/bin/env python3
"""safe_first_element function with type anotition"""
from typing import List, Any, Sequence, Iterable, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """safe first ele """
    if lst:
        return lst[0]
    else:
        return None
