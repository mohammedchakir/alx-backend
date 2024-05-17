#!/usr/bin/env python3
"""Function to calculate start and end indexes for pagination."""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Calculate start and end indexes for pagination.

    Args:
        page: An integer representing the current page (1-indexed).
        page_size: An integer representing the number of items per page.

    Returns:
        A tuple of 2 integers representing start & end indexes for pagination.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
