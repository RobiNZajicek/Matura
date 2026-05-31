import time

def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)- i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] , arr[j]
    return arr

def zmer(name,funca):
    start = time.perf_counter()
    funca()
    cas = time.perf_counter() - start
    print(f'{name} {cas} s')
    
    
for n in [100,500,1000]:
    data = list(range(n,0,-1))
    zmer(f'BubbleSort n={n}', lambda data=data: bubble_sort(data))
            
    