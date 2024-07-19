#!/usr/bin/env python3
"""redis learning"""
import redis
import uuid
from typing import Callable, Optional, Union
import functools


def count_calls(method: Callable) -> Callable:
    """To count calls to a method"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to count method calls"""
        key = f"{method.__qualname__}_calls"
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store call history of a method"""

    @functools.wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function to store call history"""
        inputs_key = f"{method.__qualname__}:inputs"
        outputs_key = f"{method.__qualname__}:outputs"

        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))

        return result

    return wrapper


class Cache:
    """Class cache"""

    def __init__(self):
        """initialization here"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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

    def get_call_count(self, method_name: str) -> int:
        """Retrieve the call count for a method"""
        return int(self._redis.get(f"{method_name}_calls") or 0)

    def get_input_history(self, method_name: str) -> list:
        """Retrieve the input history for a method"""
        inputs_key = f"{method_name}:inputs"
        return self._redis.lrange(inputs_key, 0, -1)

    def get_output_history(self, method_name: str) -> list:
        """Retrieve the output history for a method"""
        outputs_key = f"{method_name}:outputs"
        return self._redis.lrange(outputs_key, 0, -1)


def replay(method: Callable):
    """Display the history of calls to a method"""
    cache = method.__self__
    method_name = method.__qualname__

    inputs = cache.get_input_history(method_name)
    outputs = cache.get_output_history(method_name)

    print(f"{method.__qualname__} was called {len(inputs)} times:")

    for input_data, output_data in zip(inputs, outputs):
        print(
            f"{method.__qualname__}(*{eval(input_data)})
            -> {output_data.decode('utf-8')}")
