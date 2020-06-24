from src.project.Calculator import Calculator
from src.project.sanitization import Sanitization
import statistics
class StatsCalculator(Calculator):

    def mean(self,lst):
        if any([type(num) not in (int,float) for num in lst]):
            raise ValueError("Number in the list not int or float")
        return statistics.mean(lst)

    def median(self,lst):
        if any([type(num) not in (int, float) for num in lst]):
            raise ValueError("Number in the list not int or float")
        return statistics.median(lst)



