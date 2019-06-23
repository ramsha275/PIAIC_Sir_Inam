import random
temp = random.randint(30, 50)
while temp < 45:
    print('It\'s better weather, temp=', temp)
    temp = random.randint(30, 50)
print('I came back due to Hot Weather, temp=', temp)
