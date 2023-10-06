#!/usr/bin/python3
"""make_multiplier function with type anotition"""
from typing import List, Union, Tuple, Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier"""
    def func(n: float) -> float:
        """helper func"""
        return multiplier * n
    return func
