#!/usr/bin/env python3
"""
Define LIFOCache class
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    A caching system using LIFO
    """
    prev_key = None

    def __init__(self):
        """
        Initilize
        """
        super().__init__()

    def put(self, key, item):
        """
        Assign an item to a dictionary
        """
        if key and item:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                print("DISCARD: {}".format(LIFOCache.prev_key))
                del self.cache_data[LIFOCache.prev_key]

            LIFOCache.prev_key = key

    def get(self, key):
        """
        Gets a value from a dictionary
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
