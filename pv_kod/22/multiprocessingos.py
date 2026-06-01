import time
from multiprocessing import Process


def bubble_sort(arr):
    arr = arr[:]
    for i in range(len(arr)):
        for j in range(len(arr)-i -1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1] ,arr[j]
                
    return arr

def zmer(name,func):
    start = time.perf_counter()
    func()
    cas = time.perf_counter() - start
    print(f'{name} {cas}s ')

def spust_bubble(n):
    data = list(range(n,0,-1))
    zmer(f"Bubble sort n={n}",lambda data=data: bubble_sort(data))

if __name__ == "__main__":
    for n in [100,500,10000]:
        
        p1=Process(target=spust_bubble, args=(n,))
        p2=Process(target=spust_bubble, args=(n,))
   
        start = time.perf_counter()

        p1.start()
        p2.start()

        p1.join()
        p2.join()

        cas = time.perf_counter() - start
        print(f'dva procesy bubble sort n={n} {cas}s')