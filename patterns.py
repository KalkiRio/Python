#           1 
#         2 1 2 
#       3 2 1 2 3
#     4 3 2 1 2 3 4
#   5 4 3 2 1 2 3 4 5
# n=5
# for i in range(n):
#     num=i+1
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(num, end=" ")
#         num-=1
#     for j in range(i):
#         print(num+2, end=" ")
#         num+=1
#     print()

#           1 
#         2 3 2 
#       3 4 5 4 3 
#     4 5 6 7 6 5 4 
#   5 6 7 8 9 8 7 6 5 
# n=5
# for i in range(n):
#     num=i+1
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(num, end=" ")
#         num+=1
#     for j in range(i):
#         print(num-2, end=" ")
#         num-=1
#     print()


#           1 
#         2 3 4 
#       3 4 5 6 7 
#     4 5 6 7 8 9 10 
#   5 6 7 8 9 10 11 12 13 
# n=5
# for i in range(n):
#     num=i+1
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i+1):
#         print(num, end=" ")
#         num+=1
#     for j in range(i):
#         print(num, end=" ")
#         num+=1
#     print()
