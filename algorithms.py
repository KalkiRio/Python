"""bubble sort"""
def bubble_sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j]>nums[j+1]:
                nums[j],nums[j+1]=nums[j+1],nums[j]
    return nums

nums=[5,3,8,6,7,2]
print(bubble_sort(nums))

"""selection sort"""
