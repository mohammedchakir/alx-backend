#!/usr/bin/env python3
"""
Helper function for pagination
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start and end index for pagination.
    Args:
        page: An integer representing the current page (1-indexed).
        page_size: An integer representing the number of items per page.
    Returns:
        A tuple of two integers representing start & end index for pagination.
    """

    return ((page-1) * page_size, page_size * page)
