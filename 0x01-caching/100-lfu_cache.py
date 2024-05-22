#!/usr/bin/python3
"""
LFUCache module
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache class that inherits from BaseCaching
    """

    def __init__(self):
        """
        Initialize LFUCache
        """
        super().__init__()
        self.frequency = {}
        self.queue = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
                self.frequency[key] += 1
            elif len(self.cache_data) >= self.MAX_ITEMS:
                min_frequency = min(self.frequency.values())
                lru_keys = [k for k,
                            v in self.frequency.items() if v == min_frequency]
                lru_key = min(lru_keys, key=lambda k: self.queue.index(k))
                del self.cache_data[lru_key]
                del self.frequency[lru_key]
                print("DISCARD:", lru_key)
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.queue.append(key)
            else:
                self.cache_data[key] = item
                self.frequency[key] = 1
                self.queue.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
