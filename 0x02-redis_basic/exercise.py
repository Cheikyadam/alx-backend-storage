#!/usr/bin/env python3
"""redis learning"""
import redis
import uuid
from typing import Union


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
