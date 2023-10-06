#!/usr/bin/env python3
"""element_length function with type anotition"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """apply annotion fn"""
    return [(i, len(i)) for i in lst]
