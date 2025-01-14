##n=int(input('enter a range:'))
##i=1
##while(i<=n):
##    print(i)
##    i+=1
# import time
# n=int(input('enter a range for getting odd numbers: '))
# i=1
# while(i<=n):
#     print(i)
#     i+=2

# n=int(input('enter a range for even numbers: '))
# i=0
# while(i<=n):
#     print(i)
#     i+=2

# time.sleep(2)
# i=1
# while(i<=30):
#     if i%3==0:
#         print(i)
#     i+=1

# s=input('enter a string: ')
# i=0
# while(i<len(s)):
#     print(s[i])
#     i+=2

# s=input('enter a string with special characters: ')
# i=0
# while(i<len(s)):
#     if s[i].isalnum()==False:
#         print(s[i])
#     i+=1

#Q
##i=0
##while i<10:
##    print(i)
##    i+=1
##
###Q
##s='hello'
##i=0
##while i<len(s):
##    print(f"{i}:{s[i]}")
##    i+=1
##
###Q
##i=20
##while i>=0:
##    print(i)
##    i-=1

#Q
##l=['apple','banana','orange','pine','grapes']
##i=0
##l2=[]
##while i<len(l):
##    if l[i][0] in 'aeiouAEIOU':
##        l2.append(l[i][::-1])
##    else:
##        l2.append(l[i])
##    i+=1
##print(l2)

#Q
# t=(10,20,'hello',True,'world',(10,20,30))
# i=0
# while i<len(t):
#     if type(t[i]) in (int,bool,float,complex):
#         print(t[i])
#     i+=1

#Q
# l=['hello',10,20,40,10.5,11]
# i=0
# j=len(l)-1
# while i<=(len(l)//2) and j>=(len(l)//2):
#     l[i],l[j]=l[j],l[i]
#     i+=1
#     j-=1
# print(l)
# #or
# j=len(l)
# while i<(len(l)//2):
#     l[i],l[j-1-i]=l[j-1-i],l[i]
#     i+=1
# print(l)

# t=('hello',10,20,40,10.5,11)
# res=()
# i=0
# while i<len(t):
#     res=(t[i],)+res
#     i+=1
# print(res)

# s='hello world'
# s2=''
# i=0
# while i<len(s):
#     s2=s[i]+s2
#     i+=1
# print(s2)

# d={10:'a',20:'b',30:'c',40:'d'}
# d2={}
# l=list(d.items())
# i=len(l)-1
# while i>=0:
#     d2[l[i][0]]=l[i][1]
#     i-=1
# print(d2)

#Q
# s='hello world'
# i=0
# length=0
# while True:
#     if s[i]==s[-1]:
#         length+=1
#         break
#     else:
#         length+=1
#     i+=1
# print(length)

#Q
# l=[10,20,10,40,30,30,20]
# l2=[]
# i=0
# while i<len(l):
#     if l[i] not in l2:
#         l2.append(l[i])
#     i+=1
# print(l2)

#Q
# l=['hello','ten']
# d={}
# i=0
# while i<len(l):
#     d[l[i]]=len(l[i])
#     i+=1
# print(d)

#Q
# s='hello world hi'
# d={}
# i=0
# while i<len(s):
#     if s[i] in d:
#         d[s[i]]+=1
#     else:
#         d[s[i]]=1
#     i+=1
# print(d)

#Q
# l=['hello','guy','hey']
# l2=[]
# i=0
# while i<len(l):
#     l2.append(l[i][-1])
#     i+=1
# print(l2)

#Q
# s='hello world'
# s2=''
# s3=''
# i=0
# if s[0] in 'aeiouAEIOU':
#     while i<len(s):
#         s2+=s[i]
#         i+=2
#     print(s2)
# elif s[0].isalpha():
#     while i<len(s):
#         s3=s[i]+s3
#         i+=1
#     print(s3)

# l=['hello','bello','chello','ananta','amrit']
# l2=[]
# i=0
# while i<len(l):
#     if l[i][0] in 'aeiouAEIOU':
#         l2.append(l[i][::2])
#     elif l[i][0].isalpha():
#         l2.append(l[i][::-1])
#     i+=1
# print(l2)

#Q
# s='hello world welcome to python programming language'
# d={}
# l=s.split()
# i=0
# while i<len(l):
#     if l[i][-1] in 'aeiouAEIOU':
#         d[l[i]]=len(l[i])
#     i+=1
# print(d)

#Q
# l=['welcome','python','java','programming','spring','django']
# d={}
# i=0
# while i<len(l):
#     if len(l[i])>5:
#         d[l[i]]=len(l[i])
#     i+=1
# print(d)

#Q
# l=['joi.com','fb.py','qspy.in']
# l2=[]
# l3=[]
# i=0
# while i<len(l):
#     l2+=l[i].split('.')
#     i+=1
# i=1
# while i<len(l2):
#     l3.append(l2[i])
#     i+=2
# print(l3)

#Q
# l=[10,20,30,40,50]
# s=''
# i=0
# while i<len(l):
#     s+=str(l[i])+' '
#     i+=1
# print(s)

#Q
# l='just looking like a wow'
# l2=l.split()
# s=''
# i=0
# while i<len(l2):
#     word=''
#     if len(l2[i])%2==0:
#         word+=l2[i][:-1]+chr(ord(l2[i][-1])-32)
#         s+=word+' '
#     else:
#         j=0
#         while j<len(l2[i]):
#             word+=chr(ord(l2[i][j])-32)
#             j+=1
#         s+=word+' '
#     i+=1
# print(s)