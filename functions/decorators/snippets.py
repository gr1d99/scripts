from functools import wraps
import logging
# # lets say we want to add 1 to an argument passed to
# # the function called
#
#
# def call(log=False):
#
#     def call_fn(fn):
#         mylogger = logging.log(level=logging.INFO, msg='warnin')
#         if log == True:
#                print mylogger
#         return fn
#
#     return call_fn
#
#
# @call(log=True)
# def some_func(n):
#     value = []
#     for i in range(n):
#         value.append(i * i)
#
#     return value
#
# print some_func(5)


# today snippet#2 is about decorators with arguments.
def underline(above=False, below=False, symbol='-', symbols_no=20):
    def underline_decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            if above and below:
                print symbol * symbols_no
                func(*args, **kwargs)
                print symbol * symbols_no

            elif above and not below:
                print symbol * symbols_no
                func(*args, **kwargs)

            elif not above and below:
                func(*args, **kwargs)
                print symbol * symbols_no

            else:
                func(*args, **kwargs)
        return wrapped
    return underline_decorator


# usage
@underline(above=True, below=True, symbol='@')
def somefunc():
    print ("Function is running")


somefunc()