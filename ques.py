#Q:whether last item of collection is int/float/complex/bool/collection
# data = [10,10.6,'RUCHI',True,[10,20,30]]
# if type(data[-1]) == int:
#     print("it is integer")
# elif type(data[-1]) == float:
#     print("it is float")
# elif type(data[-1])== complex:
#     print("it is complex")
# elif type(data[-1])== bool:
#     print("it is boolean")
# else:
#     print("data is a collection")

# Q:
# char=input("enter a character here: ")
# if 'A'<=char<='Z':
#     print(ord(char))
# elif 'a'<=char<='z':
#     print(chr(ord(char)-32))
# elif '0'<=char<='9':
#     print(int(char)**2)
# else:
#     print(char)

#Q1:
# job_loc=input("enter your job location: ")
# if job_loc.lower() =='bangalore':
#     name=input("enter your name for registration :")
#     email=input("enter your email id: ")
#     print(f"you have been registered for our company, {name} with mail {email}")
# else:
#     print("Sorry, you can only register if you are from Bangalore.")

#Q2:
# num=int(input("enter a number: "))
# if num%2==0:
#     print(f"Happy {num}")
# else:
#     print(num)

#Q3:
# num=int(input("enter a number: "))
# if 5<=num<=10:
#     print("number is between 5 to 10")
# else:
#     print("number is not between 5 to 10")

#Q4:
# string=input("enter a string: ")
# if len(string)>3:
#     print("string is longer than 3 characters")
# else:
#     print("string is shorter than 3 characters")

#Q5:
# num=int(input("enter a number: "))
# if len(str(num))==4:
#     print(f"{num} has 4 digits.")
# else:
#     print(f"{num} does not have 4 digits.")

#Q6:
# char=input("enter a character: ")
# if char.lower() in 'aeiou':
#     print(f"{char} is a vowel.")
# else:
#     print(f"{char} is not a vowel.")

#Q7:
# num=int(input("enter a number: "))
# if num%2==0 and num%5==0:
#     print("the number is even and multiple of 5")
# else:
#     print("either the number is not even or not multiple of 5")

#Q8:
# string=input("enter a string: ")
# if len(string) == 1:
#     print(f"'{string}' is a single character.")
# else:
#     print(f"'{string}' is not a single character.")

#Q9:
# string=input("enter a string: ")
# if string.isupper() and string.isalpha():
#     print("it has uppercase alphabets")
# else:
#     print("it does not have uppercase alplabets")

#for single character strings we can also use:
# string=input("enter a string: ")
# if 'A'<=string<='Z':
#     print("it has uppercase alphabet")
# else:
#     print("it does not have uppercase alplabet")

#Q10:
# string=input("enter a string: ")
# if string[::-1] == string:
#     print(f"{string} is palindrome")
# else:
#     print("string is not palindrome")

#Q11:
# col_param = int(input("Enter the color parameter 1 for green, 0 for pink: "))
# if col_param == 1:
#     print("The parrot is green.")
# elif col_param == 0:
#     print("The parrot is pink.")
# else:
#     print("Invalid parameter")

#Q12:
# string = input("Enter a string: ")
# if len(string) > 3:
#     print(f"The length of the string is {len(string)}.")
# else:
#     print(f"The string is: {string}")

#Q: fizz if divisible by 3, buzz if divisible by 5 else fizzbuzz
# num=int(input("enter a number: "))
# if num%3==0:
#     print("fizz")
# elif num%5==0:
#     print("buzz")
# else:
#     print("fizzbuzz")

#Q: single/double/triple/more digit for a number
# num=int(input("enter a number: "))
# if -9<=num<=9:
#     print("single digit")
# elif -99<=num<=99:
#     print("double digit")
# elif -999<=num<=999:
#     print("triple digit")
# else:
#     print("larger than 4 digits")

#Q: middle value of tuple is int or not
# data=(10,5,50,3+3j,'hello')
# m_index = len(data)//2
# if type(data[m_index]) == int:
#     print("it is integer")
# else:
#     print("it is not an integer")

#Q: relation between two integers
# num=int(input("enter a number: "))
# num2=int(input("enter another number: "))
# if num == num2:
#     print("both are equal")
# if num>num2:
#     print("first number is greater than second")
# else:
#     print("second number is greater")

#Q: nested if last item collection/not
# data=[10,10.5,True,'apple']
# if type(data[-1])==str:
#     if 'a'<=data[-1][0]<='z' or 'A'<=data[-1][0]<='Z':
#         if data[-1][0] in 'aeiouAEIOU':
#             print(ord(data[-1][0]))
#         else:
#             print("no ascii for you")
#     else:
#         print("not alphabet")
# else:
#     print("not string")

#Q: collection even/odd int/square
# data=[5,'Hi',10.5,'hello']
# if len(data)%2==0:
#     if type(data[0]) == int:
#         if data[0]%2 == 1:
#             print(data[0]**2)
#         else:
#             print("no square, even data")
#     else:
#         print("not integer")
# else:
#     print("odd no. of elements")

#Q: input starts with alphabet, ascii even/not, if even square
# data=input("enter something: ")
# if 'a'<=data[0]<='z' or 'A'<=data[0]<='Z':
#     if ord(data[0])%2==0:
#         print((ord(data[0]))**2)
#     else:
#         print("ascii is odd")
# else:
#     print("first letter is not an alphabet")