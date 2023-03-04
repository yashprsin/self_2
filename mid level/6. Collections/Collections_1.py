# Collections: Counter, namedtuple, OrderedDict, deque
from collections import Counter
from collections import namedtuple
from collections import OrderedDict
from collections import defaultdict
from collections import deque

a = "aaaaabbbbccc"
my_counter = Counter(a)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())

# most common element
print(my_counter.most_common(1))
print(my_counter.most_common(1)[0])
print(my_counter.most_common(1)[0][0])
print(my_counter.elements())
# To many similar element

# print a list
print(list(my_counter.elements()))

# namedtuple
Point = namedtuple('Point','x,y')
pt = Point(1,-3)
print(pt.x, pt.y)

# OrderDict
ordered_dict = OrderedDict()
ordered_dict['a'] = 1
ordered_dict['b'] = 2
ordered_dict['c'] = 3
ordered_dict['d'] = 4
ordered_dict['e'] = 5

print(ordered_dict)

ordered_dict_2 = OrderedDict()
ordered_dict_2['d'] = 4
ordered_dict_2['a'] = 1
ordered_dict_2['b'] = 2
ordered_dict_2['c'] = 3
ordered_dict_2['e'] = 5

print(ordered_dict_2)


# Defaultdict

d = defaultdict(int)
d['a'] = 1
d['b'] = 2
print(d['a'])
print(d['b'])
print(d['c'])

# float value
a = defaultdict(float)
a['a'] = 1.22
a['b'] = 2.33
print(a['a'])
print(a['b'])
print(a['c'])

# using list

c = defaultdict(list)
c['a'] = 1.22
c['b'] = 2.33
print(c['a'])
print(c['b'])
print(c['c'])

# duque

d1 = deque()
d1.append(1)
d1.append(2)
print(d1)

d1.appendleft(3)
print(d1)

d1.pop()
print(d1)

d1.popleft()
print(d1)

d1.clear()
print(d1)

d2 = deque()
d2.append(1)
d2.append(2)
d2.append(3)
print(d2)

d2.extend([4,5])
print(d2)

d2.extendleft([6,7])
print(d2)

# rotate tool
d3 = deque([1,2,3,4,5,6])
print(d3)
d3.rotate(2)
print(d3)
d3.rotate(-1)
print(d)
