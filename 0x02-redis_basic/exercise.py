#!/usr/bin/env python3
"""redis learning"""
import redis
import uuid
from typing import Callable, Optional, Union


class Cache:
    """Class cache"""

    def __init__(self):
        """initialization here"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """sroring data"""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self,
            key: str,
            fn:
            Optional[Callable] = None) -> Union[str, bytes, int, float, None]:
        """Retrieve data"""
        data = self._redis.get(key)
        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Optional[str]:
        """Retrieve data as str"""
        return self.get(key, lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Optional[int]:
        """Retrieve data as int"""
        return self.get(key, lambda d: int(d))
