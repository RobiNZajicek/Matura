def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

import time
def zmer(nazev,func):
    start = time.perf_counter()
    func()
    cas = time.perf_counter() -start
    print(f'{nazev} {cas} s')
    
for n in [100,200,10000]:
    data = list(range(n,0,-1))
    zmer(f'Bubble sort n={n}',lambda data=data: bubble_sort(data))
    