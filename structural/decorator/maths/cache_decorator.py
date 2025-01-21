from functools import lru_cache

def cache_result(func):
    """Decorator to cache function results."""
    cached_func = lru_cache(maxsize=128)(func)
    return cached_func