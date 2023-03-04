# import random
#
# friends=[input("Enter a name: ").split(' ',1) for i in range(int(input("Enter number of friends: ")))]
# l=random.sample([i for i in range(len(friends))],len(friends))
# for i in range(len(friends)):
#     print(friends[l[i]][0]+" "+friends[i][1])
import random
friends = [input(f"Enter {i +1} name : ").split(' ') for i in range(int(input("No of Friends: ")))]
l = random.sample([i for i in range(len(friends))], len(friends))
for i in range(len(friends)):
    print(friends[l[i]][0]+" "+friends[i][1])
