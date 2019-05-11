def merge(a, b):
	index_a = 0
	index_b = 0 
	c = []

	while index_a < len(a) and index_b < len(b):

		if a[index_a] < b[index_b]:

			c.append(a[index_a])
			index_a += 1

		else:
			c.append(b[index_b])
			index_b+=1

	c.extend(a[index_a:])
	c.extend(b[index_b:])

	return c

#  O(n*log(n))
def mergesort(List):
	if len(List) == 0 or len(List) == 1 :
		return List


	mid = len(List)//2
	lower = List[:mid]
	upper = List[mid:]

	new_lower = mergesort(lower)
	new_upper = mergesort(upper)

	return merge(new_lower,new_upper)

# O(n^2)
def selection_sort(List):
	for i in range (len(List)):
		min_index = i

		for j in range (i+1, len(List)):
			if List[j] < List[min_index]:
				min_index = j
		if min_index != i :
			List[i], List[min_index] = List[min_index], List[i]

		return List
# O(n^2)
def insertion_sort(List):

	for i in range(1, len(List)):
		min_num = List[i]
		j = i - 1

		while j >= 0 and  min_num < List[j]:
			List[j+1] = List[j]
			j -=1 

		List[j+1] = min_num

	return List
	
# O (n*log(n))
def quick_sort(x):
    if len(x) == 0 or len(x) == 1:
        return x
    pivot =x[int(len(x)/2)]
    pivot_index = int(len(x)/2)
    low = [x[i] for i in range(pivot_index) if x[i] <= pivot]
    low += [x[i] for i in range(pivot_index+1, len(x)) if x[i] <= pivot]
    high = [x[i] for i in range(pivot_index) if x[i] >pivot]
    high += [x[i] for i in range(pivot_index+1, len(x)) if x[i] > pivot]

    return quick_sort(low) + [x[pivot_index]] + quick_sort(high)
x=[2,1,3,10,7,1,20,13]

print(mergesort(x))