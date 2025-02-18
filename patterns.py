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

#                         *    
#                         * *  
#     *       * * * e e e * * *
#   * *       * * *       * *  
# * * * e e e * * *       *    
#   * *                        
#     *                        
# n=int(input("enter a number: "))
# for i in range(n-1):
#     for j in range(n*4):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*', end=' ')
#     print()
# for i in range(n):
#     for j in range(i,n-1):
#         print(' ',end=' ')
#     for j in range(i+1):
#         print('*', end= ' ')
#     for j in range(n):
#         if i==n-1:
#             print('e',end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(n):
#         print('*',end=' ')
#     for j in range(n):
#         if i==0:
#             print('e', end=' ')
#         else:
#             print(' ',end=' ')
#     for j in range(i,n):
#         print('*',end=' ')
#     print()
# for i in range(n-1):
#     for j in range(i+1):
#         print(' ', end=' ')
#     for j in range(i,n-1):
#         print('*',end=' ')
#     for j in range(n):
#         print(' ',end=' ')
#     print()

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i):
#         if j==0 or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     for j in range(i+1):
#         if j==i or i==n-1:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(1,6):
#     for j in range(1,6):
#         if i in (1,5) or j in (1,5):
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i ==1 or j==1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i ==5 or j==1:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i ==1 or j==5:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i ==5 or j==5:
#             print("*",end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(1,6):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()

# for i in range(1,6):
#     for j in range(5,0,-1):
#         if j<=i:
#             print("*", end=' ')
#         else:
#             print(' ', end=' ')
#     print()

# for i in range(1,6):
#     for j in range(5,0,-1):
#         if i<=j:
#             print('*',end=' ')
#         else:
#             print(' ',end=' ')
#     print()