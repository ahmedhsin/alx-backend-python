#!/usr/bin/env python3
"""to_kv function with type anotition"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """to kv"""
    return (k, v * v)
