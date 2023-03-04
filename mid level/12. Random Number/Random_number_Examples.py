import random

# Random Float Number
'''
a = random.random()
print(a)
'''
# Output: is smaller than 1

# Random no. with specific range
'''
a = random.uniform(1, 10)
print(a)
'''
# Output: in float 0 to 10

# Random Integer
'''
a = random.randint(1, 10)
print(a)
'''

# Similar program
'''
a = random.randrange(1, 10)
print(a)
'''
# Note: the program never pick integer 10

# Probability density function for the normal distribution
'''
a = random.normalvariate(0, 1)
print(a)
'''

# Choice a random word
'''
mylist = list("ABCDEFGH")
a = random.choice(mylist)
print(a)
'''

# Choice random Multi words
'''
mylist = list("ABCDEFGH")
a = random.sample(mylist, 3)
print(a)
'''

# similar method
'''
mylist = list("ABCDEFGH")
a = random.choices(mylist, k=3)
print(a)
'''

# Shuffle Method

'''
mylist = list("ABCDEFGH")
random.shuffle(mylist)
print(mylist)
'''
# Seed Method
'''
random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))

random.seed(1)
print(random.random())
print(random.randint(1, 10))
random.seed(2)
print(random.random())
print(random.randint(1, 10))
'''
