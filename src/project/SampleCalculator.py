from src.project.Calculator import Calculator
from src.project.StatsCalculator import StatsCalculator
import math

class SampleCalculator(StatsCalculator):
    def cohran(self,zScore, p, e):
        return math.ceil((self.square(zScore) * p *(1-p))/self.square(1-e))
