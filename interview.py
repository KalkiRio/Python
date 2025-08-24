def fact(num):
    for i in range(1, num):
        num*=i
    return num
print(fact(5))

def fib(num):
    a,b=0,1
    print(a,b, end=' ')
    for i in range(num):
        a,b=b,a+b
        print(b, end=' ')
fib(10)

