#Q1
# def square(n):
#    if type(n) == int:
#        print(n**2)

# square(10)

# def even_odd(n):
#    if n%2==0:
#        print("no is even")
#    else:
#        print("no is odd")
# even_odd(10)

# ##def seq(a,b):
#    for i in range(a,b+1):
#        print(i)
# seq(1,10)

# def palindrome(n):
#    r=0
#    temp=n
#    while n>0:
#        rem=temp%10
#        r=r*10+rem
#        temp//=10
#    if r==n:
#        print("palindrome")
#    else:
#        print("not a palindrome")
# num=int(input("enter a number to check for palindrome: "))
# palindrome(num)

#fibonacci
# def fib(n):
#     a,b=0,1
#     for i in range(n):
#         print(a, end=' ')
#         a,b=b,a+b
# fib(10)
# r=int(input("enter no of rows:"))
# for i in range(r):
#     print(' '*(r-i-1),end =' ')
#     print('*' * (2*i+1), end=' \n')

#Q
# def armstrong(num):
#    temp = num
#    n=num
#    sum=0
#    count=0
#    while n>0:
#        rem=n%10
#        count+=1
#        n//=10
#    while temp>0:
#        n=temp%10
#        sum += n**count
#        temp//=10
#    if num==sum:
#        return "it is armstrong number"
#    else:
#        return "it is not an armstrong number"
# num=int(input("enter a number to check for armstrong: "))
# print(armstrong(num))
##1634 is armstrong
##
###Q
# def count_special(st):
#    count=0
#    for i in st:
#        if not 'a'<=i<='z' and not 'A'<=i<='Z' and not '0'<=i<='9':
#            count+=1
#    return count
# word=input("enter a string with special characters: ")
# print(f"count of special characters are: {count_special(word)}")

#Q
# def len_col(col):
#     length=0
#     for i in col:
#         length+=1
#     return length
# col=eval(input("enter a collection: "))
# print(f"length of collection is {len_col(col)}")

# def bio(name,place='bangalore',date='20-01-25'):
#     return name
# print(bio(place='gurugram',name='elon'))
