import matplotlib.pyplot as plt
import numpy as np
from math import e
#Exercise 1:
def function1 (x,r):
    return (x*(np.exp(r-r*x)))


#Exercise 2:
#print("For obtaining the result for this function I will need two numbers:")
#x = int(input(f"First number: "))
#r = int(input(f"Second number: "))

def function2 (x,r):
    data =[] #records
    for i in range(100):
        y = function1(x, r) #iterative call
        x = y               #update for y value
        data.append(x)

    #plot set up:

    xaxis= range(len(data))
    plt.plot(xaxis, data, '-b', linewidth = 1.5, marker='o', markerfacecolor='yellow', markersize=5)
    plt.title("Exponential Map")
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.legend(['y = x*e^(r*(1-x))'])
    plt.show()

#test cases fro exercise 2
x=0.5
function2(x, 2.8)
