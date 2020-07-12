import math as mt
import numpy as np
import random
import matplotlib.pyplot as plt

def start():
    print("~~~ Welcome the the 2D Ising Model ~~~\n")
    print("Please enter the size of the array you would like to use")
    arraySize = input("Size of array: ")
    print("\nGreat, let's get started!\n")

    print ("Initializing domain\n")
    A = initialize_Array(arraySize)

    return(A,arraySize)


def initialize_Array(N):
    # Array will have dimensions of nPoints x nPoints
    nPoints = N
    A = np.zeros((nPoints-1,nPoints-1))

    # loop through array and assign each point +1 or -1
    for i in range(0,nPoints-1):
        for j in range(0,nPoints-1):
            # Generate random +1 or -1
            A[i,j] = random.choice([1,-1])


    return(A)


def main(domain,N):

    nPoints = N
    # Initialize domain temperature
    Temp = 10.1

    # Begin the main, outside loop
    for outerLoop in range(1,101):
        Temp -= 0.1
        print("Temperature = {}".format(Temp))

        # Go into calculation loop
        #updateDomain(domain,nPoints)


    return(domain)

def updateDomain(domain,nPoints):
    for iteration in range(1,nPoints**2):
        i = random.randomrange(0,nPoints-1)
        j = random.randomrange(0,nPoints-1)

        if i == 0 and j == 0: # Top right corner
            nu = nPoints-1
            nd = j+1
            nr = i+1
            nl = nPoints-1
        elif i == nPoints-1 and j == 0: # Top Left corner
            nu = nPoints-1
            nd = j+1
            nr = 0
            nl = i-1
        elif i == nPoints-1 and j == nPoints-1 #bottom left corner

    return()




#### This part runs the porgram
[domain,N] = start()
domain = main(domain,N)


# Plot the domain figure
fig = plt.figure(figsize=(9,9))
ax = fig.add_subplot(111)
ax.set_title('Ising Domain')
plt.imshow(domain)
ax.set_aspect('equal')
cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
cax.get_xaxis().set_visible(False)
cax.get_yaxis().set_visible(False)
cax.patch.set_alpha(0)
cax.set_frame_on(False)
plt.show()
