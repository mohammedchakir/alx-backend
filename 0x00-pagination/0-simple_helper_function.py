#!/usr/bin/env python3
"""
Helper function for pagination
"""


def index_range(page: int, page_size: int) -> tuple[int, int]:
    """
    Returns a tuple of start and end index for pagination.
    Args:
        page: An integer representing the current page (1-indexed).
        page_size: An integer representing the number of items per page.
    Returns:
        A tuple of two integers representing start & end index for pagination.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page size must be positive integers.")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
