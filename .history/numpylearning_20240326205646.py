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
    # note: slicing is inclusive of first index but not the last.

    arr = np.array([1, 2, 3, 4, 5, 6, 7])

    print(arr[1:5:2])
    # step value of 2 so prints every other item

    
    arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

    print(arr[1, 1:4])
    #slicing 2D. Specify dimension then range

def dataTypes():
    # i - integer
    # b - boolean
    # u - unsigned integer
    # f - float
    # c - complex float
    # m - timedelta
    # M - datetime
    # O - object
    # S - string
    # U - unicode string
    # V - fixed chunk of memory for other type ( void )

    arr = np.array([1, 2, 3, 4])

    print(arr.dtype)
    # .dtype prints the datatype

    arr = np.array([1, 2, 3, 4], dtype='S')
    #define datatype  (string in this case)

    arr = np.array([1.1, 2.1, 3.1])

    newarr = arr.astype('i')
    print(newarr)
    # copies the arr array with the integer type
    # will round the numbers to integers
dataTypes()