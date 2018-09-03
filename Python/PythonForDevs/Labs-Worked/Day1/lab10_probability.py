import random
from random import randint

rollCounter = 13 * [0]
for l in range(10000):
    roll = random.randint(1,6) + random.randint(1,6)
    rollCounter[roll]+=1

for roll, val in enumerate(rollCounter):
    if roll < 2:
        continue
    val = float(val)
    prob = (val/10000)
    print 'For roll {}, the probability of rolling it is {:6.2%}'.format(roll, prob)
