import math
import matplotlib
import matplotlib.pyplot as plt
import sys
#import Tkinter as tk
sys.setrecursionlimit(10000)
steps=0
sut=[]
big=0
def coll(n):
    global steps, sut, big
    sut.append(n)
    if n > big:
        big=n
    if n==1:
        print('The number of steps: {}\n'.format(steps))
        return
    steps+=1
    if n%2 == 0:
        return coll(n/2)
    if (n%2!=0):
        return coll(3*n+1)
    
b=input('Please enter the number: ')
coll(b)
print(big)

seq=[]
for i in range(0, steps+1):
    seq.append(i)
#plt.xkcd()
plt.plot(seq, sut, linestyle='-', linewidth=1)
plt.xlabel('Amount of steps')
plt.ylabel('Value of a step')
plt.title('{} steps for {} to reach 1'.format(steps, b))
plt.legend()
plt.show()
