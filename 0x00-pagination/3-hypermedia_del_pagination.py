#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
from typing import List, Dict


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """the init function"""
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns hypermedia pagination information based on given start index.
        Args:
            index: An integer representing the current start index (0-indexed).
            page_size: An integer representing the number of items per page.
        Returns:
            A dictionary containing hypermedia pagination information.
        """
        assert index is None or (isinstance(index, int) and 0 <= index < len(
            self.__indexed_dataset)), "Index out of range"
        assert isinstance(page_size, int) and page_size > 0, "Page size must /\
            be a positive integer"

        next_index = index + page_size if index is not None else 0
        data = []
        for i in range(index, min(index + page_size,
                                  len(self.__indexed_dataset))):
            row = self.__indexed_dataset.get(i)
            if row:
                data.append(row)

        return {
            'index': index,
            'data': data,
            'page_size': page_size,
            'next_index': next_index
        }
