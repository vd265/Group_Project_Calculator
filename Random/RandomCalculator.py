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

#1 - Flawed
# print(random.uniform(0,10))

#2 - Works?
# print(random.uniform(0,10))

#3 - Works?
# while len(datalist)<random.randint(0,10):
# 	datalist.append(random.uniform(0,10))
# print(datalist)

#4 - Works
# print(random.choice(data))

#5 - Skipped


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