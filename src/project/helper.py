import functools
class Helper():
    @staticmethod
    def validateNumberInput(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            counter = 0
            containStringInput = False
            for item in args:
                if counter >= 1:
                    if type(item) not in (float,int):
                        print(type(item))
                        containStringInput = True
                        break
                counter += 1
            if containStringInput:
                raise ValueError("Input is not int or float")
            else:
                return func(*args, **kwargs)
        return wrapper

    @staticmethod
    def validateListInput(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            counter = 0
            wrongInput = False
            wrongValueinList = False
            for item in args:
                if counter >= 1:
                    if type(item) not in (list,tuple):
                        print(type(item))
                        wrongInput = True
                        break
                    if type(item) in (list,tuple):
                        if any([type(num) not in (int, float) for num in item]):
                            raise ValueError("Number in the list not int or float")
                counter += 1
            if wrongInput:
                raise ValueError("Input is not list")
            else:
                return func(*args, **kwargs)
        return wrapper




