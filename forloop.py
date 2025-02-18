# t=(10,20,'hello')
# for i in t:
#     print(i)

# for i in t[-1]:
#     print(i)

# l=[12,34,67,'hello']
# for i in l:
#     print(i)

# for i in l[-1]:
#     print(i)

# s={12,'hello','hi',80.6}
# for i in s:
#     print(i)

# for i in s:
#     print(i,end='\t')

# d={'a':1,'b':2}
# for i in d:
#     print(i) #prints the keys

# for i in d.items():
#     print(i[0]) #prints the keys from items of dict after using items() method

# for i in d.items():
#     print(i[1]) # prints values from list of tuples generated after using items() method

# for i in d.values():
#     print(i) # prints values

# for i in d.keys():
#     print(i) # prints keys

#remove duplicate values
# l=[10,10,20,40,30,30,50]
# out=[]
# for i in l:
#     if i not in out:
#         out.append(i)
# print(out)

#append int values from tuple to list
# t=(10,'20','hello',20,40,'hi',True,10.5)
# l=[]
# for i in t:
#     if type(i)==int:
#         l.append(i)
# print(l)

#reverse of string using for loop
# s='python'
# s2=''
# for i in s:
#     s2=i+s2
# print(s2)

#reverse a tuple
# t=(12,20,30,40)
# out=()
# for i in t:
#     out=(i,)+out
# print(out)

#reverse a list
# lst=[10,20,'hi','hello',True,50]
# ol=[]
# n=len(lst)
# for i in lst:
#     ol=[i]+ol
# print(ol)

#2nd solution:
# for i in range (n//2):
#     lst[i],lst[n-1-i]=lst[n-1-i],lst[i]
# print(lst)

#3rd solution:
# lb=0
# ub=len(lst)
# while lb<ub:
#     lst[lb],lst[ub-1]=lst[ub-1],lst[lb]
#     lb+=1
#     ub-=1
# print(lst)

# Q1
# for i in range(10):
#     print(i)

#Q2
# for i in range(1,11):
#     print(i)

#Q3
# for i in range(20):
#     if i%2==0:
#         print(i)

#Q4
# for i in range(20):
#     if i%2!=0:
#         print(i)

#Q5
#s='hello'
# for i in range(len(s)):
#     print(f"index of {s[i]} is {i}")

#for i in s:
#    print(s.index(i),i)

#Q6
# for i in range(20,-1,-1):
#     print(i)

#Q7
##l=['apple','banana','orange','pine','grapes']
##for i in range(len(l)):
##    if l[i][0] in 'aeiouAEIOU':
##        print(l[i][::-1])
##    else:
##        print(l[i])

#Q8
# t=(10,20,'hello',True,'world',(10,20,30))
# for i in t:
#     if type(i) in (int,float,bool,complex):
#         print(i)

#Q9
# l=[10,20,30,'hello',40,50]
# n=len(l)
# for i in range(n//2):
#     l[i],l[n-1-i]=l[n-1-i],l[i]
# print(l)

# s='hello world'
# sout=''
# for i in range(len(s)):
#     sout=s[i]+sout
# print(sout)

# t=(10,20,'hello',89,40)
# t2=()
# for i in t:
#     t2=(i,)+t2
# print(t2)

# d = {1: 10, 2: 20, 3: 30, 4: 40}
# d2 = {}
# n=len(d)
# for i in range(n):
#     index = n - i - 1
#     for key in d:
#         if index==0:
#             d2[key] = d[key]
#         index -= 1
# print(d2)
#OR with methods
# d={10:'a',20:'b',30:'c'}
# d2={}
# l=list(d.items())
# n=len(l)
# for i in range(len(l)//2):
#     l[i],l[n-1-i]=l[n-1-i],l[i]
# for i in l:
#     d2[i[0]]=i[1]
# print(d2)
#OR with methods
# d={10:'a',20:'b',30:'c'}
# d2={}
# l=list(d.items())
# n=len(l)
# for i in range(len(l)-1,-1,-1):
#     d2[l[i][0]]=l[i][1]
# print(d2)


#Q10
# s='hello'
# count=0
# for i in s:
#     count+=1
# print(count)

#Q11
# l=[10,10,20,40,50,60,50,30,50,30]
# l2=[]
# for i in l:
#     if i not in l2:
#         l2+=[i]
# print(l2)

#Q12
# l=['hello','ten']
# d={}
# for i in l:
#     d[i]=len(i)
# print(d)

#Q13
# s='hello chello'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# print(d)

# for j in d:
#     print(f"{j} exists {d[j]} times")

#Q14
# l=['hello','guy','hey']
# l2=[]
# for i in l:
#     for j in range(1):
#         l2=l2+[i[-1]]
# print(l2)

#Q15
# s='aello world'
# s2=''
# s3=''
# if s[0] in 'aeiouAEIOU':
#     for i in range(len(s)):
#         if i%2==0:
#             s3+=s[i]
#     print(s3)
# elif s[0].isalpha():
#     for i in s:
#         s2=i+s2
#     print(s2)

# l=['hello','bello','chello','ananta','amrit']
# l2=[]
# for i in l:
#     if i[0] in 'aeiouAEIOU':
#         l2.append(i[::2])
#     elif i[0].isalpha():
#         l2.append(i[::-1])
# print(l2)

#Q16
# s="hello world welcome to python programming language"
# l=s.split()
# d={}
# for i in l:
#     if i[-1] in 'aeiouAEIOU':
#         d[i]=len(i)
# print(d)

#Q17
# l=['welcome','python','java','programming','spring','django']
# d={}
# for i in l:
#     if len(i)>5:
#         d[i]=len(i)
# print(d)

#Q18
# l=['joi.com','fb.py','qspy.in']
# l1=[]
# l2=[]
# for i in l:
#     l1+=i.split('.')
# for i in range(1,len(l1),2):
#     l2.append(l1[i])
# print(l2)

#19
# l=[10,20,30,40,50]
# s=''
# for i in l:
#     s=s+str(i)+' '
# print(s)

#Q20
# l='just looking like a wow'
# l1=[]
# s=''
# l2=l.split()
# for i in l2:
#     word=''
#     if len(i)%2==0:
#         word+=i[:-1]+chr(ord(i[-1])-32)
#         l1.append(word)
#         s+=word+' '
#     else:
#         for j in i:
#             word+=chr(ord(j)-32)
#         l1.append(word)
#         s+=word+' '
# print(l1) #list output
# print(s) #string output

# for i in range(1,4):
#     for j in range(1,4):
#         print(f"{i},{j}")

#Q
# s='hai hello priya'
# d={}
# l=s.split()
# for i in l:
#     c=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             c+=1
#     d[i]=c
# print(d)

#Q
# s='Python is very easy'
# l=s.split()
# print(l)
# d={}
# for i in l:
#     c=0
#     for j in i:
#         if j in 'AEIOUaeiou':
#             c+=1
#     d[i]=[i,c,i[::-1]]
# print(d)

#Q
# s='aaaabbbacccbca'
# d={}
# for i in s:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# res = ''
# for key, value in d.items():
#     res += f"{key}{value}"
# print(res)

#2nd solution
# res=''
# for i in s:
#     c=0
#     for j in s:
#         if i==j:
#             c+=1
#     if i not in res:
#         res+=f"{i}{c}"
# print(res)

##s='abcaabbsdabc'
##target='abbs'
##for i in range(len(s)-(len(target)+1)):
##    found=True
##    for j in range(len(target)):
##        if s[i+j]!=target[j]:
##            found=False
##            break
##    if found:
##        print(i)

#09/jan/2025
#Q1
# s = 'kabab is love'
# l = s.split()
# d = {}
# for i in range(len(l)):
#     count = 0
#     for j in range(len(l[i])):
#         if l[i][j] in 'aeiouAEIOU':
#             count += 1
#     if l[i]==l[-1]:
#         if l[i] not in d:
#             d[l[i][::-1]]=[l[i][::-1],count,l[i][::2]]
#     else:
#         if l[i] not in d:
#             d[l[i]] = [l[i][::-1], count, l[i][::2]]
# print(d)

# 2nd solution for the above question
# s = 'kabab is love'
# l = s.split()
# d = {}
# for i in l:
#     count=0
#     for j in i:
#         if j in 'aeiouAEIOU':
#             count+=1
#     if i==l[-1]:
#         if i not in d:
#             d[i[::-1]]=[i[::-1], count, i[::2]]
#     else:
#         if i not in d:
#             d[i]=[i[::-1], count, i[::2]]
# print(d)

# Q2
# l=[100,200,35,40,60]
# res=[]
# sum=0
# for i in l:
#     sum+=i
# for i in l:
#     res.append(sum-i)
# print(res)

# Q3
# s = 'kabab is love'
# l = s.split()
# d = {}
# for i in l:
#     count = 0
#     consonant = ''
#     for j in i:
#         if j not in 'AEIOUaeiou':
#             count += 1
#             consonant += j
#     key = f'{i[0]}{i[-1]}'
#     if key not in d:
#         d[key] = (consonant, count, consonant[::-1])
# print(d)

# Q4
# d={10:'star',20:'bye',30:'moon',40:'apple'}
# d2={}
# for i in d.items():
#     vowels=''
#     for j in i[1]:
#         if j in 'aeiouAEIOU':
#             vowels+=j
#     if i[0] not in d2:
#         d2[i[0]]=vowels
# print(d2)

# Q
s='A1B2C3D4'
"""o/p: D4C3B2A1"""
# s2=''
# l=[]
# for i in s:
#     s2+=i
#     if i.isdigit():
#         l.append(s2)
#         s2=''
# print(''.join(l[::-1]))
#or
# s2=''
# s3=''
# for i in s:
#     s2+=i
#     if i.isdigit():
#         s3=s2+s3
#         s2=''
# print(s3)
#or
# l=[i for i in s if i.isalpha()][::-1]
# l2=[i for i in s if i.isdigit()][::-1]
# for i,j in zip(l,l2):
#     print(i,j,sep='',end='')

#Q
s='A1B2C3D4'
"""o/p: D1C2B3A4"""
# l=[]
# l2=[]
# for i in s:
#     if i.isdigit():
#         l2.append(i)
#     else:
#         l.append(i)
# for i,j in zip(l[::-1],l2):
#     print(i,j,sep='',end='')
#or
# l=[i for i in s if i.isalpha()][::-1]
# l2=[i for i in s if i.isdigit()]
# for i,j in zip(l,l2):
#     print(i,j,sep='',end='')

s="abc*ef/gh"
"""o/p: hgf*ec/ba"""
# d={}
# for i,j in enumerate(s):
#     if not j.isalnum():
#         d[j]=i
# rl=[i for i in s if i.isalnum()][::-1]
# for i in d.items():
#     rl.insert(i[1],i[0])
# print(''.join(rl))
