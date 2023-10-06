#!/usr/bin/env python3
"""element_length function with type anotition"""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """comment for checker"""
    zoomed_in: List = [
        item * factor for item in lst
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)
