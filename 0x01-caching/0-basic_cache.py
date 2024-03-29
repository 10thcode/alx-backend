#!/usr/bin/env python3
"""
Defines BasicCache class
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A basic caching system
    """
    def __init__(self):
        """
        Initialize
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign an item to a dictionary
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Gets a value from a dictionary
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
