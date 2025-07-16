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
# target=9
# for i in range(len(num)):
#     for j in range(i+1,len(num)):
#         if (num[i]+num[j])==target:
#             print([i+1,j+1])
#             break

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

# class Solution:
#     def hasDuplicate(self, nums) -> bool:
#         hashset=set()
#         for i in nums:
#             if i in hashset:
#                 return True
#             hashset.add(i)
#         return False
# nums: int = [1,2,3,3]
# answer=Solution()
# print(answer.hasDuplicate(nums))


# from collections import Counter
# def anagram(s,t)->bool:
#     hashmap=Counter(s)
#     if len(s)!=len(t):
#         return False
#     else:
#         for i in t:
#             if i in hashmap:
#                 hashmap[i]-=1
#         for value in hashmap.values():
#             if value!=0:
#                 return False
#         return True
#or
# def anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
#     return Counter(s) == Counter(t)
#or
# def anagram(s: str, t: str) -> bool:
#     if len(s) != len(t):
#         return False
    
#     count_s = {}
#     for char in s:
#         count_s[char] = count_s.get(char, 0) + 1

#     for char in t:
#         if char in count_s:
#             count_s[char] -= 1
#             if count_s[char] == 0:
#                 del count_s[char]
#         else:
#             return False

#     return len(count_s) == 0
# s = "name"
# t = "mane"
# print(anagram(s,t))



# nums=[15,7,2,1]
# nums=[1,7,3,2]
# target=9
# def twosum(nums:[int],target:int)->str:
#     i=0
#     j=len(nums)-1
#     while i<j:
#         if nums[i]+nums[j]>target:
#             if nums[i]>nums[j]:
#                 i+=1
#             elif nums[i]<nums[j]:
#                 j-=1
#         elif nums[i]+nums[j]<target:
#             if nums[i]>nums[j]:
#                 j-=1
#             elif nums[i]<nums[j]:
#                 i+=1
#         elif nums[i]+nums[j]==target:
#             return f'index are: {i}, {j}' #O(n^2) time and O(1) space complexity
#or
# def twosum(nums:[int],target:int)->str:
#     hashmap={}
#     for i in range(len(nums)):
#         diff=target-nums[i]
#         if diff in hashmap:
#             return f'{hashmap[diff]},{i}'
#         hashmap[nums[i]]=i  # O(n) time and O(n) space complexity
# print(twosum(nums,target))

# s="naman"
# l=0
# r=len(s)-1
# pali=False
# while l<r:
#     if s[l]==s[r]:
#         l+=1
#         r-=1
#         pali=True
#     else:
#         break
# if pali:
#     print("string is a palindrome")
# else:
#     print("string is not a palindrome")

# num=1245421
# reverse=0
# temp=num
# while temp>0:
#     digit=temp%10
#     reverse = reverse*10+digit
#     temp//=10
# if reverse==num:
#     print("palindrome number")
# else:
#     print("not a palindrome")

# num=153
# temp=num
# sum=0
# len_num=len(str(num))
# while temp>0:
#     digit=temp%10
#     sum+=digit**len_num
#     temp//=10
# if sum==num:
#     print("this is an armstrong number")
# else:
#     print("this is not armstrong number")

# def fact(n):
#     """recursive method """
#     # if n==0 or n==1:
#     #     return 1
#     # else:
#     #     return n*fact(n-1)
#     """iterative method """
#     # result=1
#     # for i in range(1,n+1):
#     #     result*=i
#     # return result
# def strong(num):
#     """armstrong number program"""
#     temp=num
#     sum=0
#     while temp>0:
#         digit=temp%10
#         sum+=fact(digit)
#         temp//=10
#     if sum==num:
#         return f"{num} is a strong number"
#     return f"{num} is not a strong number"
# num=int(input("enter a number to check for strong number: "))
# print(strong(num))
# print(fact.__doc__)

# def fib(n):
#     if n<=0:
#         return 0
#     elif n==1:
#         return 1
#     """iterative method"""
#     # a,b=0,1
#     # for i in range(2,n+1):
#     #     a,b=b,a+b
#     # return b
#     """recursive method"""
#     # return fib(n-1)+fib(n-2)

# n=int(input("enter a number: "))
# for i in range(n):
#     print(fib(i))

