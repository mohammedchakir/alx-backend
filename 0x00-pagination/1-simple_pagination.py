#!/usr/bin/env python3
"""
Helper functions and class for pagination
"""

import csv
from typing import List


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


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """the init function"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the specified page of the dataset.
        Args:
            page: An integer representing the page number (1-indexed).
            page_size: An integer representing the number of items per page.
        Returns:
            A list of rows representing the specified page of the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page must be /\
            a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page size must /\
            be a positive integer"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        return dataset[start_index:end_index]
