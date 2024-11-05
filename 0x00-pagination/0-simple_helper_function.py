#!/usr/bin/env python3
"""Pagination - Simple helper function.
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Computes pagination indices from page number and size.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return (start, end)
