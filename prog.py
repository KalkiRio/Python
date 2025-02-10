#syntax to see the keywords in python below
# import keyword
# print(keyword.kwlist)
# print('hello world')
#\u is used to represent unicode characters \u is followed by 4 unicode characters
#\U is followed by eight hexadecimal digits to use unicode characters

# Name, percentage, degree, university, yop = "Shatadru Roy", 80, "BCA", "Gurugram University", 2025
# print(f"""\nHello, my name is {Name} \U0001F600
#       studying in {university} with average percentage of {percentage}
#       in {degree} degree and my year of passing(expected) is {yop} \u2603
#       """)


# s="hello world how are you doing"
#solution without using any method:
# l=[]
# s2=''
# for i in s:
#     if i==' ':
#         l+=[s2]
#         s2=''
#     else:
#         s2+=i
# l+=[s2]
# for i in l[::-1]:
#     print(i, end=' ')

#solution using method:
# l=s.split()
# print(*l[::-1])