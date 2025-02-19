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

