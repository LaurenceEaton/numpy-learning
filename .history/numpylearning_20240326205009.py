import numpy as np


def arrayIndexing():
    arr = np.array([1,2,3,4])

    #Index
    print(arr[0])

    #2D array
    arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

    print('2nd element on 1st row: ', arr[0, 1])

    #3D array
    arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

def arraySlicing():
    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    print(arr[1:5])