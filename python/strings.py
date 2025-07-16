#this file is for string and methods used on strings
#types of strings:
name='Rio'
name2 = "Roy"
ranstr='''bduebuybduyby
eygudygeiugye
geydguydgie
'''
ranstr2="""gbdygfciugdbyscgry
gcbywgeiugybuycge
ycveygwuigcyfegiu
"""
'''can be used for
multiline comments, the reason for why
it is also called docstring for use in 
documentation within program'''

print(name,name2,ranstr,ranstr2,sep='\n')

#dir() gives methods and contents associated to what is written within it
print(dir(str))
a='hello world'

#len() func is used to find the length of a collection dt or amt of individual values
print(f'\nlength of string "a" is {len(a)}')

#string methods

#upper() is used to convert all characters to upper case
print(a.upper())

b='hEllO woRld'
#lower function is used to convert all characters to lower case
print(b.lower())

#title() converts first letter of each word it encounters to upper case and rest to lower case
print(b.title())

#capitalize() converts first letter of an entire string to upper case and rest to lower case 
print(b.capitalize())

#replace(old,new) is used to replace old string or substring with new value
name_1='HIMANSHU GOSWAMI1'
name_2='Gangwani'
print(name_1.replace(name_1,name_2))
print(name_1.replace('GOSWAMI1','Gangwani'))
print(name_1.replace('GOSWAMI1',name_2))
print(name_2.replace('n','a'))
#print(name_2.replace()) typer error

#isupper() is used to check whether entire string is in upper case
name_3='CHAITANYA'
print(name_3.isupper())
print(name_2.isupper())
print(name_1.isupper())

#islower() is used to check whether entire string is in lower case or not
name_4='sukumar'
name_5="john wick 4"
print(f'\n{name_1.islower()}')
print(name_4.islower())
print(name_5.islower())

#isalpha() is used to check whether entire string is in alphabets
print(f'\n{name_4.isalpha()}')
print(name_5.isalpha())

#isdigit() is used to check whether entire string is in numeric characters
ph='8978978379'
print(f'\n{ph.isdigit()}')
print(name_5.isdigit())

#swapcase() is used to interchange the case of string i.e. upper case to lower and vice versa
s="Hello WoRlD"
print(s.swapcase())
#print(s.swapcase(s)) typeerror takes no arg
#print(s.swapcase(q)) nameerror q is not defined

#count() used ot count no. of occurences of value/substring
s='Hello World'
print(s.count('l'))
print(s.count('ello'))
print(s.count('')) #12 as it counts no of empty substrings
#print(s.count()) typeerror takes one arg none given

#startswith() checks whether a string starts with a particular subsrting
print(s.startswith('H'))
print(s.startswith('HeLL')) #case sensitive

#endswith() checks whether a string ends with particular substring or not
print(s.endswith('d'))
print(s.endswith('rld'))

#split() splits string based on characters in a substring default space
#output: list
s1='good-morning-world'
print(s.split())
print(s1.split('-'))
print(s1.split())

#find() is used to find the index position for a substring/character
print(s1.find('-'))
print(s1.find('q'))#-1 if value is not found

#rfind() is used to find index from right side
print(s1.rfind('-'))

#strip() used to remove beginning and ending space/character
s2='    hello   '
s3='-----hello-----'
print(s2.strip())
print(s3.strip('-'))

#lstrip() used to remove beginning space/character
print(s2.lstrip())
print(s3.lstrip('-'))

#rstrip() used to remove ending space/ character
print(s2.rstrip())
print(s3.rstrip('-'))

#join() used to particular character between all the characters
s='hello world'
s1='rakesh'
print('-'.join(s))
print('$'.join(s1))

#escape character usage
st='he\'s my cousin'
print(s)

#raw string
path=r"C:\Users\Ribhu\Documents\oracle sql files\assignment1.LST"
print(path)

#formatting string
print(f"default value of integer is {int()} and float is {float()}")