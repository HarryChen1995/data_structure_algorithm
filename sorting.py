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

def bubble_sort(List):
	for i in range(len(List)):
		for j in range (len(List)-i-1):
			if List[j] > List[j+1]:
				List[j], List[j+1] = List[j+1], List[j]


def partition(List,Low,High):
	i = Low - 1
	pivot = List[High]

	for j in range(Low, High):
		if List[j] <= pivot:
			i += 1 
			List [i], List [j] = List [j], List [i]
	List [i+1], List [High] = List[High], List [i+1]
	return i + 1


# O (n^2)
def quick_sort(x,low ,high):
	if low < high:
		pivot = partition(x,low,high)
		quick_sort(x, low, pivot-1)
		quick_sort(x, pivot+1, high)



x=[50,2,1,3,10,7,1,20,13]
bubble_sort(x)
print(x)

