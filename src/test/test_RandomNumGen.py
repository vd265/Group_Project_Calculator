import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)
import random
data=[1,2,3,4,5,6,7,8,9,10]
datalist=[]
random.seed(a=None,version=None)

#Random Generator Functions

# 1 - Generate a random number without a seed between a range of two numbers - Both Integer and decimal
print(random.randint(0,10))

# 2 - Generate a random number with a seed between a range of two numbers - Both Integer and Decimal
random.seed(2)
print(random.randint())

# 3 - Generate a list of numbers with a seed and between a range of numbers - Both Integer and Decimal
random.seed(1)
while len(datalist)<random.randint(0,10):
    datalist.append(random.uniform(0,10))
    print(datalist)

# 4 - Select a random item from a list
print(random.choice(data))

# 5 - Set a seed and randomly select the same value from a list
random.seed(5)
print(random.choice(data))
random.seed(5)
print(random.choice(data))

# 6 - Select N number of items from a list without a seed
count=0
while count<=random.randint(0,10):
    datalist.append(random.choice(data))
count+=1
print(datalist)

# 7 - Select N number of items from a list with a seed.
count=0
random.seed()
while count<=random.randint(0,10):
    datalist.append(random.choice(data))
    count+=1
    print(datalist)

if __name__ == '__main__':
    unittest.main()
