from __future__ import annotations

from ._array_object import Array

from typing import Tuple, Union

import cupy as np


def unique(
    x: Array,
    /,
    *,
    return_counts: bool = False,
    return_index: bool = False,
    return_inverse: bool = False,
) -> Union[Array, Tuple[Array, ...]]:
    """
    Array API compatible wrapper for :py:func:`np.unique <numpy.unique>`.

    See its docstring for more information.
    """
    res = np.unique(
        x._array,
        return_counts=return_counts,
        return_index=return_index,
        return_inverse=return_inverse,
    )
    if isinstance(res, tuple):
        return tuple(Array._new(i) for i in res)
    return Array._new(res)
