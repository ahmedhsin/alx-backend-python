#!/usr/bin/env python3
"""sum_mixed_list function with type anotition"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """sum mixed list"""
    sum: float = 0
    for i in mxd_lst:
        sum = sum + i
    return sum
