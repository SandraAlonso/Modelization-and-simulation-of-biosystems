import matplotlib.pyplot as plt

#Exercise 1:
def function1 (r, x):
    return r*x*(1-x)

print("For obtaining the result for this function I will need two numbers:")
r = int(input(f"First number: "))
x = int(input(f"Second number: "))
y = function1(r,x)   
print("The solution for this function is:", y)

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
    plt.title("Logistic equation")
    plt.xlabel("Generations")
    plt.ylabel("Population")
    plt.legend(['y = rx*(1-x)'])
    plt.show()

#test cases fro exercise 2
x=0.5
function2(x, 1)
function2(x, 2.5)
function2(x, 3.2)
function2(x, 3.5)
function2(x, 3.8)
function2(x, 5)
x=0.4
function2(x, 1)
function2(x, 2.5)
function2(x, 3.2)
function2(x, 3.5)
function2(x, 3.8)
function2(x, 5)
