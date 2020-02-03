#time complexity O(nlog(n))
def Sum2(nums, target):

    arr = []
    for i in range(0, len(nums)-2):
        if i == 0 or (i>0 and nums[i] != nums[i-1]):
            sum = target - nums[i]
            l = i+1
            r = len(nums) -1
            while l <= r:
                    mid = l + (r-l)//2
                    if nums[mid] == sum:
                            arr.append([nums[i],nums[mid]])
                            break
                    elif nums[mid] < sum:
                            l = mid+1
                    else:
                            r = mid -1
    return arr


x  = [0,0,1,1,2,3,4,5,6,7,7,7,8,8,8,9,9,9,10,10]
print(Sum2(x,10))

