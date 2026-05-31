import time

def bubble_sort(arr):
    arr =arr[:]
    for i in range(len(arr)):
        for j in range(len(arr) - i -1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
    return arr

def zmer(name,function):
    start = time.perf_counter()
    function()
    cas = time.perf_counter - start
    print(f'{name} cas  {cas}')
    
for n in [10,500,1000000]:
    data = list(range(n,0,-1))
    print(f'Bubble sort n ={n}',lambda data=data: bubble_sort(data))