#comprehensions

#it is  a phenomenon of creating a new collection by writing less lines of instructions to increase the efficiency of program
# comprehensions can be applied only for mutable data types.
#types of comprehensions: list, set, dictionary

#list comprehension: it is a process of creating a new list by considering less lines of instructions.
#syntax:
#only for tsb: var=[tsb for var in collection]
#for and if: var=[tsb for var in collection if <condition>]
#for if and else: var=[tsb if <condition> else fsb for var in collection]

# l=['apple','banana','mango','cherry']
# l2=[i for i in l if i[-1] in 'aeiouAEIOU']
# print(l2)

# l3=[i for i in range(1,101) if i%2==1]
# print(l3)

# s='hello python welcome to the world'
# l=[i[::-1] if len(i)%2==0 else i for i in s.split()]
# print(l)

#set comprehension: it is a process of creating a new set by considering less lines of instructions.
#syntax:
#only for tsb: var={tsb for var in collection}
#for and if: var={tsb for var in collection if <condition>}
#for if and else: var={tsb if <condition> else fsb for var in collection}

# s={i for i in range(1,21) if i%2==1}
# print(s)

# s='hello'
# s2={(s[i],i) for i in range(len(s))}
# print(s2)

# dict comprehension: it is a process of creating a new dictionary by considering less lines of instructions.
# syntax:
# only for loop: var={key:value for var in collection}
#for and if: var={key:value for var in collection if <condition>}
#for if and else: var={key:value if <condition> else value for var in collection}

#wap to add words as key and length as value
# s='hello world welcome'
# d={i:len(i) for i in s.split()}
# print(d)

# l=[1,2,2,3,4,4,5,5]
# t=('one','two','three','four','five')
# """{1:'one', 2:'two',3:'three',4:'four'}"""
# seen = set()
# l2 = [i for i in l if not (i in seen or seen.add(i))]
# d={i:j for i,j in zip(l2,t)}
# print(d)

# #wap to extract value having more than two or more 'a' in string
# l=['allen','amazon','flipkart','anabella','banana','broadcast']
# d={j:i for i,j in enumerate(l) if j.count('a')>=2}
# print(d)

#wap to create a dictionary if the string ends with vowels reverse and add i else add the first character of string as its value
# s="come on guys we'll do party"
# d={i:i[::-1] if i[-1] in 'aeiouAEIOU' else i[0] for i in s.split()}
# print(d)

#wap to build list of names ends with consonant from given collection take 
names=['jatin','anshu','manish','nikita','nitin']
#wap to build a list of numbers which are divisible by 5 from 1 to 100
#wap to build a list of tuple string and its length pair only if the strings have even length.
#wap to check each item of the collection which is having only individual datatype values and add to the new set else reverse of item.
data=[10,'alan',[10,20,30],True,10+2j]
#waptobuild a dictionary of each letter and its ascii code only if the ascii code is odd number take string
s='hello world'
#wap to take a number and print it's divisors in a list.