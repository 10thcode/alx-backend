#!/usr/bin/env python3
"""
Define FIFOCache class
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Caching system using FIFO
    """
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
                discarded_key = list(self.cache_data.keys())[0]
                print("DISCARD: {}".format(discarded_key))
                del self.cache_data[discarded_key]

    def get(self, key):
        """
        Gets a value from a dictionary
        """
        if key and key in self.cache_data:
            return self.cache_data[key]
