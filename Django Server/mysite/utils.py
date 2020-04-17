from django.db import connection, reset_queries
from consts import LOG_DIVIDER
from time import perf_counter


def query_debugger(func):
    def wrapper(*args, **kwargs):
        reset_queries()

        start = len(connection.queries)
        time_start = perf_counter()
        wrapper_func = func(*args, **kwargs)
        time_end = perf_counter()
        end = len(connection.queries)

        print(LOG_DIVIDER)
        print(f'Query Count: {end-start}')
        print(f'Query Time: {time_end - time_start}')
        print(f'Function Name: {func.__name__}')
        print(LOG_DIVIDER)

        return wrapper_func
    return wrapper
