"""bubble sort"""
# def bubble_sort(nums):
#     for i in range(len(nums)-1,0,-1):
#         for j in range(i):
#             if nums[j]>nums[j+1]:
#                 nums[j],nums[j+1]=nums[j+1],nums[j]
#     return nums

# nums=[5,3,8,6,7,2]
# print(bubble_sort(nums))

"""selection sort"""
# def selection_sort(nums):
#     for i in range(len(nums)):
#         minposition=i
#         for j in range(i,len(nums)):
#             if nums[j]<nums[minposition]:
#                 minposition=j
#         nums[i],nums[minposition]=nums[minposition],nums[i]
#         # print(nums)
#     return nums

# nums=[5,3,8,6,7,2]
# print(selection_sort(nums))

"""merge sort"""
# def merge_sort(nums):
#     if len(nums)>1:
#         nums_left=nums[:len(nums)//2]
#         nums_right=nums[len(nums)//2:]

#         merge_sort(nums_left)
#         merge_sort(nums_right)

#         i,j,k=0,0,0
#         while i<len(nums_left) and j<len(nums_right):
#             if nums_left[i]<nums_right[j]:
#                 nums[k]=nums_left[i]
#                 i+=1
#             else:
#                 nums[k]=nums_right[j]
#                 j+=1
#             k+=1

#         while i<len(nums_left):
#             nums[k]=nums_left[i]
#             i+=1
#             k+=1
#         while j<len(nums_right):
#             nums[k]=nums_right[j]
#             j+=1
#             k+=1
#         return nums

# nums=[5,3,8,6,7,2,1,4,9]
# print(merge_sort(nums))

# l = [5,3,8,6,7,2,1,4,9,0]
# data = [(1,3),(2,1),(1,2)]

# for i in range(len(data)-1, -1, -1):
#     for j in range(i):
#         if data[j][1]>data[j+1][1]:
#             data[j],data[j+1] = data[j+1], data[j]
# print(data)

# for i in range(len(l)):
#     minpos = i
#     for j in range(i,len(l)):
#         if l[j]<l[minpos]:
#             minpos = j
#     l[minpos], l[i] = l[i], l[minpos]
#     # print(l)
# print(l)

