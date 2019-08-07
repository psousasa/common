from concurrent.futures import ThreadPoolExecutor
from functools import wraps


_DEFAULT_POOL = ThreadPoolExecutor()


def parallel_task(f, executor=None):
    """
    This decorators allows to parallelize any method invocation. Use this decorator by writing @parallel_task before any
    method declaration, and it will be called in parallel without blocking the main thread.
    To fetch the result of this Future, one has to call Future.result(), which will block the main thread until the
    result is fetched.
    Refer to htpps://docs.python.org/3/library/concurrent.futures.html for more information
    :param f: function or method to be called in parallel
    :param executor: optional ThreadPoolExecutor
    :return: Returns a concurrent.futures.Future instance
    """

    @wraps(f)
    def wrap(*args, **kwargs):
        return (executor or _DEFAULT_POOL).submit(f, *args, **kwargs)

    return wrap


