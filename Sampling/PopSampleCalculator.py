class Calculator:
    def add(self,x,y):
        if type(x) not in (int, float) :
            raise ValueError('Value is not int or float')
        return x+y
    def minus(self,x,y):
        return y-x
    def multiply(self,x,y):
        return x*y
    def divide(self,x,y):
        if y == 0:
            raise ValueError("Can't be divided by zero")
        return x/y
    def sumList(self,lst):
        result =0
        for x in range(0, len(lst)):
            result += lst[x]
        return result

    def square(self,x):
        return x**2
    def sqrt(self,x):
        return math.sqrt(x)