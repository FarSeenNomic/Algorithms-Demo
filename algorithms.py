"""
Author: Anton Hirschl
Date: 2025-09-13
Class: CPSC 335
"""
import numpy as np
import math

def network_sort(arr, o=0):
    #https://bertdobbelaere.github.io/sorting_networks.html
    #Sorting network for 8 inputs, 19 CEs, 6 layers
    #assert(len(arr) == 8)
    if arr[o+0] > arr[o+2]: arr[o+0], arr[o+2] = arr[o+2], arr[o+0]
    if arr[o+1] > arr[o+3]: arr[o+1], arr[o+3] = arr[o+3], arr[o+1]
    if arr[o+4] > arr[o+6]: arr[o+4], arr[o+6] = arr[o+6], arr[o+4]
    if arr[o+5] > arr[o+7]: arr[o+5], arr[o+7] = arr[o+7], arr[o+5]
    if arr[o+0] > arr[o+4]: arr[o+0], arr[o+4] = arr[o+4], arr[o+0]
    if arr[o+1] > arr[o+5]: arr[o+1], arr[o+5] = arr[o+5], arr[o+1]
    if arr[o+2] > arr[o+6]: arr[o+2], arr[o+6] = arr[o+6], arr[o+2]
    if arr[o+3] > arr[o+7]: arr[o+3], arr[o+7] = arr[o+7], arr[o+3]
    if arr[o+0] > arr[o+1]: arr[o+0], arr[o+1] = arr[o+1], arr[o+0]
    if arr[o+2] > arr[o+3]: arr[o+2], arr[o+3] = arr[o+3], arr[o+2]
    if arr[o+4] > arr[o+5]: arr[o+4], arr[o+5] = arr[o+5], arr[o+4]
    if arr[o+6] > arr[o+7]: arr[o+6], arr[o+7] = arr[o+7], arr[o+6]
    if arr[o+2] > arr[o+4]: arr[o+2], arr[o+4] = arr[o+4], arr[o+2]
    if arr[o+3] > arr[o+5]: arr[o+3], arr[o+5] = arr[o+5], arr[o+3]
    if arr[o+1] > arr[o+4]: arr[o+1], arr[o+4] = arr[o+4], arr[o+1]
    if arr[o+3] > arr[o+6]: arr[o+3], arr[o+6] = arr[o+6], arr[o+3]
    if arr[o+1] > arr[o+2]: arr[o+1], arr[o+2] = arr[o+2], arr[o+1]
    if arr[o+3] > arr[o+4]: arr[o+3], arr[o+4] = arr[o+4], arr[o+3]
    if arr[o+5] > arr[o+6]: arr[o+5], arr[o+6] = arr[o+6], arr[o+5]
    """
    net = [
        [(0,2),(1,3),(4,6),(5,7)],
        [(0,4),(1,5),(2,6),(3,7)],
        [(0,1),(2,3),(4,5),(6,7)],
        [(2,4),(3,5)],
        [(1,4),(3,6)],
        [(1,2),(3,4),(5,6)],
    ]
    for layer in net:
        for i,j in layer:
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j],arr[i]"""
    return arr

def stooge_sort(arr):
    def nodulate(stp, enp):
        if enp-stp == 0:
            return
        elif enp-stp == 1:
            return
        elif enp-stp == 2:
            if arr[stp] > arr[enp]:
                arr[stp], arr[enp] = arr[enp], arr[stp]

        # Sorts of length 3 cut time down by 47%
        #elif enp-stp == 3:
        #    if arr[stp+0] > arr[stp+2]: arr[stp+0], arr[stp+2] = arr[stp+2], arr[stp+0]
        #    if arr[stp+0] > arr[stp+1]: arr[stp+0], arr[stp+1] = arr[stp+1], arr[stp+0]
        #    if arr[stp+1] > arr[stp+2]: arr[stp+1], arr[stp+2] = arr[stp+2], arr[stp+1]
        else:
            midlow = math.floor((2*stp+enp)/3)
            midhigh = math.ceil((stp+2*enp)/3)

            nodulate(stp, midhigh)
            nodulate(midlow, enp)
            nodulate(stp, midhigh)
    nodulate(0, len(arr)-1)
    return arr

# Orignal
"""
def radix_sort(arr):
    bitdepth = max(arr).bit_length()
    for bitcheck in range(bitdepth):
        bins = {0:[],1:[]}
        for i in arr:
            bins[i >> bitcheck & 1].append(i)
        arr = bins[0] + bins[1]
    return arr
"""

def radix_sort_cpp(arr):
    bitdepth = max(arr).bit_length()
    for bitcheck in range(bitdepth):
        bin0 = []
        bin1 = []
        for i in arr:
            if i & (1<<bitcheck):
                bin1.append(i)
            else:
                bin0.append(i)
        arr = bin0 + bin1
    return arr

# More pythonic
def radix_sort_py(arr):
    bitdepth = max(arr).bit_length()
    for bitcheck in range(bitdepth):
        arr = [i for i in arr if (i>>bitcheck)==0] + [i for i in arr if (i>>bitcheck)==1]
    return arr

def shellsort(arr):
    gaps = [109, 41, 19, 5, 1]
    for gap in gaps:
        # Just insertion sort but with gap instead of size 1
        for i in range(gap, len(arr)):
            j = i
            temp = arr[i]
            while (j >= gap) and (arr[j - gap] > temp):
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

def comb_sort(arr):
    gap = len(arr)
    shrink = 1.24733
    sortd = False

    while not sortd:
        gap = int(gap / shrink)
        if gap <= 1:
            gap = 1
            sortd = True
        elif gap == 9 or gap == 10:
            gap = 11

        for i in range(0, len(arr)-gap):
            if arr[i] > arr[i+gap]:
                arr[i], arr[i+gap] = arr[i+gap], arr[i]
                sortd = False
    return arr

def bubble_sort(arr):
    #for i in range(0, len(arr), 8):
    #    arr = network_sort(arr, i)
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def selection_sort(arr):
    for i in range(len(arr)-1):
        mip = i+1
        mi = arr[mip]
        for j in range(i+2, len(arr)-1):
            if arr[j] > mi:
                mip = j
                mi = arr[mip]
        arr[mip],arr[i] = arr[i],arr[mip]

def cocktail_sort(arr):
    low = 0
    high = len(arr)
    while True:
        swapped = False
        highest_swap = high
        for i in range(low, high-1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
                highest_swap = i
        high = highest_swap+1
        if not swapped:
            break

        lowest_swap = low
        for i in range(high-2, low, -1):
            if arr[i] > arr[i+1]:
                arr[i],arr[i+1] = arr[i+1],arr[i]
                swapped = True
                lowest_swap = i
        low = lowest_swap
        if not swapped:
            break
    return arr

def counting_sort(arr):
    if not arr:
        return []
    min_val = min(arr)
    max_val = max(arr)
    k = max_val - min_val + 1
    count = [0]*k
    for num in arr:
        count[num - min_val] += 1
    output = []
    for i,freq in enumerate(count):
        value = i+min_val
        output.extend([value] * freq)
    return output

def other_counting_sort(arr):
    li = []
    [].join([i] * arr.count(i) for i in range(min(arr), max(arr)))

def heapsort(arr):
    def heapify(n, i):
        largest = i
        left = 2*i+1
        right = 2*i+2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)

    n = len(arr)
    for i in range(n // 2-1, -1, -1):
        heapify(n, i)

    for end in range(n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(end, 0)

    return arr

def heapsort_np(pyarr):
    arr = np.array(pyarr)
    def heapify(n, i):
        largest = i
        left = 2*i + 1
        right = 2*i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left
        if right < n and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(n, largest)
    
    n = len(arr)
    for i in range(n // 2-1, -1, -1):
        heapify(n, i)

    for end in range(n-1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        heapify(end, 0)

    return arr

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr

def mergesort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])
    return merge(left, right)
def merge(left, right):
    results = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            results.append(left[i])
            i += 1
        else:
            results.append(right[j])
            j += 1
    results.extend(left[i:])
    results.extend(right[j:])
    return results

# https://www.geeksforgeeks.org/dsa/in-place-merge-sort/
def mergesort_inplace(arr, l=0, r=None):
    if r is None: r = len(arr)-1
    #print(l, r)
    if l < r:
        mid = (l + r) // 2
        mergesort_inplace(arr, l, mid)
        mergesort_inplace(arr, mid + 1, r)
        merge_inplace(arr, l, mid, r)
def merge_inplace(arr, start, mid, end):
    start2 = mid + 1
    if (arr[mid] <= arr[start2]):
        return
    while (start <= mid and start2 <= end):
        if (arr[start] <= arr[start2]):
            start += 1
        else:
            value = arr[start2]
            index = start2
            while (index != start):
                arr[index] = arr[index - 1]
                index -= 1
            arr[start] = value
            start += 1
            mid += 1
            start2 += 1

#quicksort out of place
def quicksort_oop(arr):
    if not arr: return []
    pivot = arr[len(arr) // 2]
    return quicksort_oop([i for i in arr if i < pivot]) + [pivot]*arr.count(pivot) + quicksort_oop([i for i in arr if i > pivot])

def quicksort(arr):
    def partition(low, high):
        pivot = arr[(low + high) // 2]
        i = low
        j = high
        while i <= j:
            while arr[i] < pivot:
                i += 1
            while arr[j] > pivot:
                j -= 1
            if i <= j:
                arr[i],arr[j] = arr[j],arr[i]
                i += 1
                j -= 1
        return i,j

    def sort(low, high):
        if low < high:
            i,j = partition(low, high)
            sort(low, j)
            sort(i, high)

    sort(0, len(arr)-1)
    return arr

import random
def bogosort(arr):
    while arr != sorted(arr):
        arr = random.sample(arr, k=len(arr))
    return arr

def bucket_sort(arr, k=6, nextSort=bucket_sort):
    buckets = {}
    m = max(arr)+1
    for i in arr:
        buckets[int(k * i / m)].append(i)
    for i in range(k): 
        nextSort(buckets[i])
    return [].extend(i for i in buckets)

"""
Todo:
binary insertion
bogosort
Bucket sort
thread sort
Counting sort
Exchange sort
Bitonic sort
stalin sort
"""

from collections import namedtuple
sorting_fuction = namedtuple('sorting_fuction', 'function eta')

sorts = [
    # name              function that given the size (length = 1<<size) returns the size
    # From class
    sorting_fuction(bubble_sort,       lambda s:0.00006295164470033*s**1.97910176019928 ),
    sorting_fuction(counting_sort,     lambda s:0.12590966103887818 + 0.0001407200845374504*s),
    sorting_fuction(heapsort,          lambda s:0.00093884606337985*s**1.21022819271525 ),
    sorting_fuction(insertion_sort,    lambda s:0.00004837195814484*s**1.90217391392381 ),
    sorting_fuction(mergesort,         lambda s:0.00106095999695890*s**1.13649341850985 ),
    sorting_fuction(mergesort_inplace, lambda s:0.00017102099095920*s**1.66000746488193 ),
    sorting_fuction(quicksort,         lambda s:0.00066252394136697*s**1.12818705558610 ),
    sorting_fuction(quicksort_oop,     lambda s:0.00145718559191774*s**0.97184412899861 ),
    sorting_fuction(bucket_sort,       lambda s:0.10000000000000000*s**0.99999999999999 ),
    sorting_fuction(radix_sort_py,     lambda s:0.00031232545846613*s**0.91436832994485 ),
    sorting_fuction(radix_sort_cpp,    lambda s:0.00133875127950064*s**0.97349651014333 ),

    # Out of class
    sorting_fuction(sorted,            lambda s:0.00003279781910071*s**1.13353352017700 ),
    sorting_fuction(comb_sort,         lambda s:0.00039582242312576*s**1.23196593642214 ),
    sorting_fuction(shellsort,         lambda s:0.00018230709723320*s**1.35183161242285 ),
    sorting_fuction(selection_sort,    lambda s:0.00006167057579155*s**1.80813353046285 ),
    sorting_fuction(cocktail_sort,     lambda s:0.00006015288612914*s**1.95106035784034 ),
    sorting_fuction(stooge_sort,       lambda s:0.00015517254318294*s**2.68735652930718 ),
    sorting_fuction(bogosort,          lambda s:s ** 5 ),
]

#sorts = []

if __name__ == '__main__':
    import random, timeit, math
    def time(func, size, num = 20):
        """
        Takes a sorting function func
        times it
        returns the time in milliseconds
        """
        # Random
        data = [random.randint(100, 1000) for _ in range(size)]
        # Sorted
        #data = list(range(size))
        # Reversed
        #data = list(range(size)).reverse()
        return 1000/num*timeit.timeit(lambda:func(data.copy()), number=num)

    # 100% random data
    # data mostly sorted
    # data only a few swaps
    # data already sorted
    # data sorted, reversed

    for func, eta in sorts:
        print(f'"{func.__name__}",')
        print("{")
        for binsize in range(3, 20):
            t = time(func, 1<<binsize)
            print(f"{{{1<<binsize},{t}}},")
            if t > 7:
                break
            t = time(func, 3<<(binsize-1))
            print(f"{{{3<<(binsize-1)},{t}}},")
        print("},")
        continue
        # pass to other code for analysis

        size_high = 6
        while 20 * eta(size_high) < 1000:
            size_high += 1
        size_high -= 1
        size_low = int(size_high / 2)

        time_s8 = time(func, size_low)
        time_s10 = time(func, size_high)
        # functions are probably in the form t = exp(m*s+b)

        # t == Exp[m * s + b]
        m = -(math.log(time_s10)-math.log(time_s8))/(size_low-size_high)
        b = (size_low*math.log(time_s10) - size_high*math.log(time_s8))/(size_low-size_high)

        #print(f"m={int(m*100)/100}\nb={int(b*100)/100}")
        print(f"math.exp({int(m*100)/100}*s-{-int(b*100)/100})")

        #for s in range(8, 11):
        #    print(s, math.exp(m*s+b))
