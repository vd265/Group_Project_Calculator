from src.project.Calculator import Calculator
import random
from src.project.helper import Helper
class RandomCalculator(Calculator):
    @Helper.validateNumberInput
    def generateRandomNumber(self,low,high):
       return random.randrange(low,high)

    @Helper.validateNumberInput
    def generateRandomSeedNumber(self,seed,low,high):
        random.seed(seed)
        return random.randrange(low,high)

    @Helper.validateNumberInput
    def generateRandomList(self,n,low,high):
        return [random.randrange(low,high) for x in range(n)]

    @Helper.validateListInput
    def selectRandomFromList(self,lst):
        return random.choice(lst)

    @Helper.validateListInput
    def selectRandomwithSeed(self,lst):
        random.seed(1)
        return random.choice(lst)

    def selectRandomNList(self,lst,n):
        return random.sample(lst,n)

    def selectRandomNListSeed(self,lst,n,seed):
        random.seed(seed)
        return random.sample(lst, n)


