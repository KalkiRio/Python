# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# nums=[-4,-1,0,3,10]
# res=[]
# l=0
# r=len(nums)-1
# for i in range(len(nums)-1,-1,-1):
#     if abs(nums[l])>abs(nums[r]):
#         res[i]=nums[l]**2
#         l+=1
#     else:
#         res[i]=nums[r]**2
#         r-=1
# print(res)