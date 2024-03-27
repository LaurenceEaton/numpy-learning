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

    arr = np.array([1.1, 2.5, 3.9])

    newarr = arr.astype('i')
    print(newarr)
    # copies the arr array with the integer type
    # will CUT OFF THE DECIMAl (round down)

def copyVSview():
    arr = np.array([1, 2, 3, 4, 5])
    x = arr.copy()
    # copy is not affected by changes to the original array

    x = arr.view()
    # view IS affected by changes to the original array

def arrayShape():
    arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

    print(arr.shape)
    # above returns (2, 4), which means that the array has 2 dimensions, where the first dimension has 2 elements and the second has 4.

def arrayReshape():
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    newarr = arr.reshape(4, 3)
    # changes the shape to 2D with 4 arrays and 3 elements in each array (12 elements in total
    
    newarr = arr.reshape(2, 3, 2)
    # 2 dimensions each with 3 arrays that each contain 2 elements
    
    arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    print(arr.reshape(2, 4).base)
    # checks if the array is a copy or view. (if it returns the original array, it is a view)



    

