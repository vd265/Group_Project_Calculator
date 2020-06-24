import functools
class Sanitization():
    @staticmethod
    def CheckIfToNumeric(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for item in args:
                print(type(item))
            return func(*args, **kwargs)
        return wrapper






