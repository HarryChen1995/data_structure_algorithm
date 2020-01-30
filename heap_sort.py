
left = lambda i : i*2+1
right = lambda i: i*2+2

def max_heapify(arr, size , i):
    largest = i
    if left(i) < size  and arr[left(i)] > arr[largest]:
        largest = left(i)
    if right(i) < size  and arr[right(i)] > arr[largest]:
        largest = right(i)

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr,size,largest)


def build_max_heap(arr):

    for i in reversed(range(0, len(arr)//2)):
        max_heapify(arr, len(arr) , i)


def heap_sort(arr):
    build_max_heap(arr)
    index = 0
    for i in reversed(range(1, len(arr))):
        arr[0], arr[i] = arr[i] , arr[0]
        index += 1
        max_heapify(arr, len(arr)-index ,0)

x = [3,2,5,1,10,12,9]
heap_sort(x)
print(x)

