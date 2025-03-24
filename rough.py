# print(dir(tuple))
# print(dir({}))
# print(dir([]))
# t=(10,10,20,'hello')
#print(t.index()) --> type error
#print(t.index(100)) --> value error as 100 is not present in the tuple

# l=[2,5,7,9,2,8]
# l2=sorted(l)
# for i in range(3):
#     print(l2[i],end='')

# l=[3,7,1,5,8,5]
# l2=sorted(l)
# for i in range(3):
#     print(l2[i],end='')

# n=8
# [0,1,2,3,4,5,6,7]
# o/p: [[0,1,2],[3,4,5]]
# n=8
# l=[i for i in range(n)]
# l2=[]
# for i in range(0,len(l),3):
#     l2.append(l[i:i+3])
# if len(l2[-1])<3:
#     l2.pop()
# print(l2)

# s="abbbcsadasssalkkdliehhgsjygddddddddddd"
# l=list({(i,s.count(i)) for i in s})
# max=l[0][1]
# max_char=l[0][0]
# for i in range(len(l)):
#     if l[i][1]>max:
#         max=l[i][1]
#         max_char=l[i][0]
# print(f"{max_char} is the most occurring character")