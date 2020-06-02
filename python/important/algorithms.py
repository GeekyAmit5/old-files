import random
import math
import time
import sys

# sys.setrecursionlimit(10000)

# joining a string
# date = "18"
# month = "05"
# year = "2020"
# today = "-".join([date, month, year])
# print(today)

# s = "String"
# print(s.center(50, "-"))
# print(s.rjust(50, "-"))

# print("v : {0:3d}".format(5))

# l = [1, 2, 3]
# del(l[1])
# x=6
# del(x)

# taking interger from user
while True:
    try:
        n = int(input("Enter a Number : "))
    except:
        pass
    else:
        break
print(n)

# print("x = ", 10, ".", sep="")


def binarySearch(list, target):
    left = 0
    right = len(list)-1
    while left <= right:
        mid = (right - left)//2
        if list[mid] == target:
            return mid
        if list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def linearSearch(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1


def bubbleSort(list):
    for i in range(len(list)):
        for j in range(i, len(list)):
            if list[i] > list[j]:
                t = list[j]
                list[j] = list[i]
                list[i] = t


def selectionSort(l):
    for i in range(len(l)):
        min = i
        for j in range(i, len(l)):
            if l[j] < l[min]:
                min = j
        l[min], l[i] = l[i], l[min]


# inserting in other list faster than inserting into same list


def insertionSort(l):
    b = [l[0]]
    for i in range(1, len(l)):
        for j in range(len(b)):
            if l[i] < b[j]:
                b.insert(j, l[i])
                break
        else:
            b.append(l[i])
    return b


# sorting same list faster when already sorted


def insertionSort(l):
    for i in range(len(l)):
        j = i
        while j > 0 and l[j] < l[j-1]:
            l[j], l[j-1] = l[j-1], l[j]
            j -= 1


def merge(a, b):
    c = []
    i, j = 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if a[i:]:
        c += a[i:]
    else:
        c += b[j:]
    return c


def mergeSort(l):
    if len(l) == 1:
        return l
    else:
        return merge(mergeSort(l[:len(l)//2]), mergeSort(l[len(l)//2:]))


# inserting b into a to form a single sorted list much slower than creating new sorted using a and b
# def merge(a, b):
#     j = 0
#     for i in range(len(b)):
#         for j in range(len(a)):
#             if b[i] < a[j]:
#                 a.insert(j, b[i])
#                 break
#         else:
#             a.append(b[i])
#     return a

# binary search with Recursion
# selection sort with and without recursion
# also write my strategy this is actually insertion sort
# adjacency matrix and list
# lambda , map ,filter
