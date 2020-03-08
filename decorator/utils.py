"""Common gadget:

1.timer
2.retry
3.count
"""

import functools
import time


def timer(func):
    """Get function execution time."""
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        stop_time = time.time()
        run_time = int(stop_time-start_time)
        print('Finish {} in {} seconds.'.format(func.__name__, run_time))
        return result
    return wraps


def retry(func):
    """Set function retry times."""
    @functools.wraps(func)
    def wraps(count=1, *args, **kwargs):
        try:
            print('{}: try {} times.'.format(func.__name__, count))
            func(*args, **kwargs)
        except Exception:
            count += 1
            if count < 6:
                return wraps(count=count, *args, **kwargs)
    return wraps


def count(func, count={}):
    """Get function execution number."""
    count[func] = 0
    @functools.wraps(func)
    def wraps(*args, **kwargs):
        count[func] += 1
        print('{} had been call {} times.'.format(func.__name__, count[func]))
        return func(*args, **kwargs)
    return wraps
