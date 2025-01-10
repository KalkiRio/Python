# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].
# nums=[-4,-1,0,3,10]
# res=[0]*len(nums)
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

#Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

# Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

# The tests are generated such that there is exactly one solution. You may not use the same element twice.

# Your solution must use only constant extra space.

 

# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
# Example 2:

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
# Example 3:

# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#1st sol
# num=[2,7,11,15]
# m=1
# target=9
# for i in range(len(num)):
#     for j in range(m,len(num)):
#         if (num[i]+num[j])==target:
#             print([i+1,j+1])
#             break
#     m+=1

# num=[2,7,11,15]
# target=9
# l=0
# r=len(num)-1
# while l<r:
#     if num[l]+num[r]<target:
#         l+=1
#     elif num[l]+num[r]>target:
#         r-=1
#     else:
#         print([l+1,r+1])
#         break

#Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.

# A substring is a contiguous sequence of characters within a string

 

# Example 1:

# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
# ["hero","as"] is also a valid answer.
# Example 2:

# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# Example 3:

# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
# words = ["leetcode", "et", "code"]
# res=[]
# for i in words:
#     for j in words:
#         if i!=j and i in j:
#             res+=[i]
# print(res)

#                         *    
#                         * *  
#     *       * * * e e e * * *
#   * *       * * *       * *  
# * * * e e e * * *       *    
#   * *                        
#     *                        
n=int(input("enter a number: "))
for i in range(1,((n*3)-2)+1):
    for j in range(1,(n*5)+1):
        print('-',end=' ')
    print()