from src.project.Calculator import Calculator
from src.project.helper import Helper
import statistics

class StatsCalculator(Calculator):

    @Helper.validateListInput
    def mean(self,lst):
        return statistics.mean(lst)

    @Helper.validateListInput
    def median(self,lst):
        return statistics.median(lst)

    @Helper.validateListInput
    def mode(self,lst):
        return statistics.mode(lst)

    @Helper.validateListInput
    def stdev(self,lst):
        return statistics.pstdev(lst)

    @Helper.validateListInput
    def variance(self,lst):
        return statistics.variance(lst)

    @Helper.validateListInput
    def z_score(self, x, lst):
        return (x - self.mean(lst))/self.stdev(lst)




