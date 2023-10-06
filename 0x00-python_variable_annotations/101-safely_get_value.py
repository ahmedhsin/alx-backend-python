#!/usr/bin/env python3
"""element_length function with type anotition"""
from typing import Any, Mapping, Union, TypeVar


T = TypeVar("T")


def safely_get_value(dct: Mapping, key: Any, default: Union[~T, None] = None) -> Union[Any, ~T]:
    """a comment for checker"""
    if key in dct:
        return dct[key]
    else:
        return default
