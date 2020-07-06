from src.project.Calculator import Calculator
from src.project.StatsCalculator import StatsCalculator
import math
from src.project.helper import Helper

class SampleCalculator(StatsCalculator):

    @Helper.validateNumberInput
    def cohran(self,zScore, p, e):
        return math.ceil((self.square(zScore) * p *(1-p))/self.square(1-e))

    @Helper.validateNumberInput
    def marginOfError(self,std,size,z):
        # implement a margin of error function here
        pass

    @Helper.validateNumberInput
    def confidenceIntervalSmaple(self,W,cL ,p= 0.5):
        pass
