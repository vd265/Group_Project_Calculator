import math
from src.project.helper import Helper
class Calculator:
    @Helper.validateNumberInput
    def add(self,x,y):
        if type(x) not in (int, float) :
            raise ValueError('Value is not int or float')
        return x+y

    @Helper.validateNumberInput
    def minus(self,x,y):
        return y-x

    @Helper.validateNumberInput
    def multiply(self,x,y):
        return x*y

    @Helper.validateNumberInput
    def divide(self,x,y):
        if y == 0:
            raise ValueError("Can't be divided by zero")
        return x/y

    @Helper.validateListInput
    def sumList(self,lst):
        result =0
        for x in range(0, len(lst)):
            result += lst[x]
        return result

    @Helper.validateNumberInput
    def square(self,x):
        return x**2

    @Helper.validateNumberInput
    def sqrt(self,x):
        return math.sqrt(x)