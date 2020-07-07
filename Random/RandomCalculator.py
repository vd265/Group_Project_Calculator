import random

print("Random integer from 0 to 9")
num1 = random.randint(0, 9)
print("Random integer: ", num1)

print("Random integer from 10 to 100")
num2 = random.randint(10, 100)
print("Random integer: ", num2)

#Setup
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

print(random)

#6 - Works?
# count=0
# while count<=random.randint(0,10):
# 	datalist.append(random.choice(data))
# 	count+=1
# print(datalist)

#7 - Works?
# count=0
# while count<=random.randint(0,10):
# 	datalist.append(random.choice(data))
# 	count+=1
# print(datalist)