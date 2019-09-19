

def convert_to_set(arr):
    x = [ i for i in arr if i]
    return x

def find_all_subset(arr):
     subset = [None]*len(arr)
     find_subset(subset,arr,0)


all_sub_set = []
def find_subset(subset,arr,i):
        if i == len(subset):
            all_sub_set.append(convert_to_set(subset))
            
        else:
            subset[i] = None
            find_subset(subset,arr,i+1)
            subset[i] = arr[i]
            find_subset(subset,arr,i+1)

x =[1,2,3,4]

find_all_subset(x)
print(all_sub_set)