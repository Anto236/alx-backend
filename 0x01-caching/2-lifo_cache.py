#!/usr/bin/env python3
""" FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """ FIFOCache
    """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """ assigns the new item to the dictionary
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                """Discard the first item (FIFO)"""
                last_key = next(reversed(self.cache_data))
                print(f"DISCARD: {last_key}")
                self.cache_data.pop(last_key)

            self.cache_data[key] = item

    def get(self, key):
        """ returns the value in self.cache_data linked to key
        """
        if key is None or not (key in self.cache_data):
            return None
        return self.cache_data[key]
