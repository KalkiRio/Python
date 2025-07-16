#here we will discuss about the data types in python
#the 4 data types below are single valued data types/ individual
a=20
b=19.67
c=4+3j
d=True
#the 5 data types below are multi valued data types/ collection
mystring='hello'
mylist=['rio','killua','norman','peter']
mytuple=('hello','world')
myset={'hello','and','good','morning'}
mydict={'hello':'world',
        'name':'rio',
        'place':'india'}
#let's do some work on these data types in the following section:
#let's see data type of the variables above using the type() function
print(type(a),type(b),type(c),type(d),sep='\n')
print(type(mystring),type(mylist),type(mytuple),type(myset),type(mydict),sep='\n')
#to know the address location of a value in a variable we can use id() function
print("address of a is: ",id(a))
#id() returns the address in integer and to convert it in hexadecimal we can use hex() function
print(hex(id(b)))
#we can get octal by using oct() and binary using bin()
print(oct(id(b)),bin(id(b)),sep='\n')
#checking the default values of the single valued data types below
print(complex(),int(),float(),bool(),sep='\n')
print(a>b)

