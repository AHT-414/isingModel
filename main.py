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

    print(len(A))
    return(A,arraySize)


def initialize_Array(N):
    # Array will have dimensions of nPoints x nPoints
    nPoints = N
    A = np.zeros((nPoints,nPoints))

    # loop through array and assign each point +1 or -1
    for i in range(nPoints):
        for j in range(nPoints):
            # Generate random +1 or -1
            A[i,j] = random.choice([1,-1])

    return(A)


def main(domain,N):

    nPoints = N
    # Initialize domain temperature
    Temp = 5.1

    fig = plt.gcf()
    fig.show()
    fig.canvas.draw()
    ax = fig.add_subplot(111)
    ax.set_title('Ising Domain')
    ax.set_aspect('equal')
    cax = fig.add_axes([0.12, 0.1, 0.78, 0.8])
    cax.get_xaxis().set_visible(False)
    cax.get_yaxis().set_visible(False)
    cax.patch.set_alpha(0)
    cax.set_frame_on(False)

    # Begin the main, outside loop
    for outerLoop in range(1,51):
        Temp -= 0.1
        print("Temperature = {}".format(Temp))

        # Go into calculation loop
        domain = updateDomain(domain,nPoints,Temp)

        # Plot the domain figure

        plt.imshow(domain)
        fig.canvas.draw()



    return(domain)

def updateDomain(A,nPoints,Temp):
    for iteration in range(1,10*nPoints**2):
        i = random.randrange(nPoints)
        j = random.randrange(nPoints)



        if j == 0: #Top
            nu = nPoints-1
        else:
            nu = j-1

        if j == nPoints-1: # bottom
            nd = 0
        else:
            nd = j-1

        if i == 0: # Right
            nr = nPoints-1
        else:
            nr = i-1

        if i == nPoints-1: # left
            nl = 0
        else:
            nl = i+1

        # Calculate delta u
        deltaU = A[i,j] * (A[i,nu] + A[i,nd] + A[nr,j] + A[nl,j])

        if deltaU <= 0:
            # If the energy difference warrents, flip
            A[i,j] = A[i,j] * -1
        else:
            savingThrow = random.random()
            if savingThrow < mt.exp(-deltaU/Temp):
                A[i,j] = A[i,j] * -1

    return(A)




#### This part runs the porgram
random.seed()
[domain,N] = start()
domain = main(domain,N)
