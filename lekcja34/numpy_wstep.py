import numpy as np
from numpy import random


lista = [[[1], [2], [3]], [[4], [5], [6]], [[7], [8], [9]]]

print(lista)
print(lista[0])
print(lista[0][0])
print(lista[0][0][0])

def print_array():
    arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(f"Tablica:\n{arr}")
    print(f"Pierwszy element tablicy:\n{arr[0]}")
    print(f"Pierwszy element tablicy:\n{arr[0][0]}")
    print(f"Typ obiektu tablicy:\n{type(arr)}")
    print(f"Kształt tablicy:\n{arr.shape}")
    return arr


def change_dimensions(arr):
    print("9x1")
    print(arr.reshape(9, 1))
    print("1x9")
    print(arr.reshape(1, 9))
    print("3x3")
    print(arr.reshape(3, 3))
    print("?x9")
    print(arr.reshape(-1, 9))
    print("3x?")
    print(arr.reshape(3, 1, 3, 1))
    
def data_format():
    try:
        arr = np.array([[1.1, 2.2, 3.3], ["kot", 2, "pies"], ['a', 'b', 'c']], dtype="U")
        print(arr)
        print(type(arr))
    except Exception as e:
        print(e)
        
    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype="U")
    print(arr)
    print(type(arr))
    
    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype="i")
    print(arr)
    print(type(arr))
    
    arr = np.array([[1.1, 2.2, 3.3], [4.4, 5.5, 6.6], [7.7, 8.8, 9.9]], dtype="f")
    print(arr)
    print(type(arr))
    
def sorted_ndarray():
    arr = np.array([[1, 6, 4], [3, 6, 7], [3, 7, 2]])
    print(f"Tablica przed sortowaniem:\n{arr}")
    print(f"Tablica po sortowaniu:\n{np.sort(arr)}")

def pick_random_ndarray():
    print(random.rand(3, 5))
    print(random.choice([3, 5, 7, 9]))
    print(random.choice([3, 5, 7, 9], size=(3, 5)))
    print(random.choice([3, 5, 7, 9], p=[0.1, 0.2, 0.3, 0.4], size=(100)))

def shuffle_ndarray():
    arr = np.array([1, 2, 3, 4, 5])
    random.shuffle(arr)
    print(f"Po tasowaniu:\n{arr}")

def shuffle_ndarray():
    arr = np.array([1, 2, 3, 4, 5])
    random.permutation(arr)
    print(f"Po tasowaniu:\n{arr}")

arr = print_array()

change_dimensions(arr)

data_format()

sorted_ndarray()