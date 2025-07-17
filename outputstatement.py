#output statement
a,b,c=10,20,30
print(a)
print(b)
print(c)
#the above will do execution in one line by line
print(a,b,c)
print(a)
#the above will print values with one space because of sep being a default space value in argument
print(a,b,c,sep='!')
#the above will give output 10!20!30 as separator is !
print(a,end='')
print(b,end='')
print(c)
print(a)
print(b,end='n\n')
#the output for above will be
#102030
#10
#20n
print(a,b,sep='@')
#here in the above the separator is a tab space
print()
#the above will print an empty line as we don't have any arguments