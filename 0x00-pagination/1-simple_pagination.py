#!/usr/bin/env python3
"""Simple pagination sample.
"""
import csv
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Generates index range for pagination based on specified page and size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)


class Server:
    """A `Server` class for handling pagination of a popular baby names database.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Instantiates a new Server object.
        """
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Fetches a paginated dataset.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]
