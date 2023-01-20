import matplotlib.pyplot as plt
import numpy as np
import time
import math
import random
import os

infinity = 'zzzzzzzzzz'
heapSize = 0


def insertionSort(A):  # Working

    for j in range(1, len(A)):
        key = A[j]
        i = j

        while i > 0 and A[i - 1] > key:
            A[i] = A[i - 1]
            # if i != 0:
            i = i - 1
        A[i] = key


def mergeSort(A, p, r):
    if p < r:
        q = int(((p + (r-1)) / 2))
        mergeSort(A, p, q)
        mergeSort(A, q + 1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):  # Issue with sorting
    n1 = q - p + 1
    n2 = r - q

    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = A[p + i]
    for j in range(0, n2):
        R[j] = A[q + j]
    L.append(infinity)
    R.append(infinity)
    i = 0
    j = 0
    k = p
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i = i + 1
        else:
            A[k] = R[j]
            j = j + 1

# def buildMaxHeap(A):
#     heapSize = len(A)
#     for i in range(0, int(len(A) / 2)):
#         maxHeapify(A, i)

# def heapSort(A):
#     buildMaxHeap(A)
#     for i in range(0, len(A)):
#         A[1] = A[i]
#         heapSize = heapSize - 1
#         maxHeapify(A, 1)

# def maxHeapify(A, i):
#     l =

# Main function


def main():
    x1 = [0]
    y1 = [0]
    fileSize = 0
    for i in range(3):
        fileSize += 15
        fileName = 'perm' + str(fileSize) + 'K.txt'

        fileDestination = os.path.join(
            *[os.path.dirname(__file__), 'wordlists', 'PERM', fileName])

        try:

            # Reading from Files

            fileObject = open(fileDestination, "r")

            word_list = fileObject.readlines()

            fileObject.close()

            start_time = time.time()
            insertionSort(word_list)  # Meat and Potatoes
            end_time = time.time()
            x1.append(fileSize)
            y1.append(end_time - start_time)

            # Writing to Files

            fileName = 'IS' + str(fileSize) + 'K.txt'

            fileDestination = os.path.join(
                *[os.path.dirname(__file__), 'wordlists', 'PERM_OUT', fileName])

            fileObject = open(fileDestination, 'x')

            for line in word_list:
                fileObject.writelines(line)

            fileObject.close()

        except IOError:
            print(fileName + ' failed to open')

    plt.rcParams['figure.figsize'] = [10, 6]  # Setting size of plot

    plt.plot(x1, y1, label="Insertion Sort")
    plt.legend()
    plt.show()

# main()


testSortingList = ['date', 'apple', 'banana', 'cucumber', 'acorn', 'aaaa']
n = len(testSortingList)
mergeSort(testSortingList, 0, n)
print('Merge Sort:     ', testSortingList)

testSortingList = ['date', 'apple', 'banana', 'cucumber', 'acorn', 'aaaa']

insertionSort(testSortingList)
print('Insertion Sort: ', testSortingList)
