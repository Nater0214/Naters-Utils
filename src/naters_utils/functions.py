# src/func_cache.py
# Caches the return values of a function


# Imports
from __future__ import annotations

import hashlib
from functools import partial
from typing import Any, Callable


# Metadata
__all__ = ["func_cache"]


# Definitions
def func_cache() -> Callable:
    """
    ### Summary
    A decorator for caching function return values.  
    Caches based on function arguments.  
    This can be useful for functions that will return the same value each time for given arguments, but for whatever reason, may not be ideal to run more than once.
    
    Usage:
    >>> @func_cache()
    ... def get_file_contents(file_path: str) -> str:
    ...     with open(file_path, 'r') as file:
    ...         return file.read()
    
    >>> get_file_contents('test.txt')
    'test'
    >>> get_file_contents('test.txt')
    'test'
    """
    
    def decorator(func: callable) -> Callable:
        """The decorator itself"""
        
        class Wrapper:
            """The wrapper itself"""

            def __init__(self, func: callable) -> None:
                """Create the wrapper"""

                # Set variables
                self._func = func
                self._cache = {}


            def __call__(self, *args, **kwargs) -> Any:
                """Run the function and cache, or return cached value"""
                
                try:
                    out = self._cache[hashlib.new("sha1", str({"args": args, "kwargs": kwargs}).encode()).hexdigest()]
                except KeyError:
                    out = self._func(*args, **kwargs)
                    self._cache[hashlib.new("sha1", str({"args": args, "kwargs": kwargs}).encode()).hexdigest()] = out
                
                return out
            
            def __get__(self, instance, owner) -> partial:
                """Compatibility with objects"""
                
                return partial(self, instance)
        
        return Wrapper(func)
    
    return decorator