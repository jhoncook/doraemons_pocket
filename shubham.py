"""count = 5
s = 0
while count!=0:
        s = s + int(input('Enter'))
        count = count -1
avg = s / 5
print(avg)

for i in range(5):
        for j in range(i):
                print('*',end='')
        print()
"""
from random import *
seed(23)
for i in range(100):
    print(randrange(1,1000),end=" ")
