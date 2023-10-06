#!/usr/bin/env python3
"""sum_list function with type anotition"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    sum: float = 0
    for i in input_list:
        sum = sum + i
    return sum
