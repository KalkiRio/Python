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
# if len(str(num))==1:
#     print("single digit number")
# elif len(str(num))==2:
#     print("double digit number")
# elif len(str(num))==3:
#     print("triple digit number")
# else:
#     print("larger than 3 digits")

#Q: middle value of tuple is int or not
# data=(10,5,50,3+3j,'hello')
# m_index = len(data)//2
# if type(data[m_index]) == int:
#     print("it is integer")
# else:
#     print("it is not an integer")

#Q: relation between two integers
num=int(input("enter a number: "))
num2=int(input("enter another number: "))