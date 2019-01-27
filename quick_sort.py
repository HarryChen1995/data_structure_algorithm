
def sort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    pivot =x[int(len(x)/2)]
    pivot_index = int(len(x)/2)
    low = [x[i] for i in range(pivot_index) if x[i] <= pivot]
    low += [x[i] for i in range(pivot_index+1, len(x)) if x[i] <= pivot]
    high = [x[i] for i in range(pivot_index) if x[i] >pivot]
    high += [x[i] for i in range(pivot_index+1, len(x)) if x[i] > pivot]

    return sort(low) + [x[pivot_index]] + sort(high)

x=[3,2,4,1,19]
print("Before quick_sort:")
print(x)
print("After quick_sort:")
print(sort(x))


