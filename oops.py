# class A3:
#     pass

# obj1 = A3()
# obj2 = A3()
# print(A3) #o/p -> <class '__main__.A3'>
# print(obj2)
# print(obj1)

# class Demo:
#     a,b=10,20

# a1=Demo()
# a2=Demo()

# Demo.a=100
# print(Demo.a)
# print(a1.a)
# print(a2.a)

# class Mall:
#     m_name='Ambience'
#     m_address='sec -14 Gurugram'
#     m_phno=9876543213
#     m_mail='mall@mail.com'
#     m_branch='Gurugram'

#     def customer(self,name,mail,address,phno,gender):
#         self.name=name
#         self.mail=mail
#         self.address=address
#         self.phno=phno
#         self.gender=gender

#     def cust_info(self):
#         print(self.name,self.mail,self.address,self.phno,self.gender,self.m_name,sep='\n')

# c1=Mall()
# c1.customer('rio','rio@gmail.com','gurugram',9876545654,'Male')
# c1.cust_info()

# class Python:
#     trainer='Nadim Sir'
#     topics='OOPS'
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#     def display(self):
#         print(self.name,self.id)

# s1=Python('vishal',1001)
# s1.display()

# import time
# class Company:
#     c_name='Vertical Labs'
#     c_loc = 'Gurugram'
#     c_phno=9876564534
    
#     def __init__(self,ename,eid,sal,comm):
#         self.ename=ename
#         self.eid=eid
#         self.sal=sal
#         self.comm=comm
#     def display(self):
#         print(self.ename,self.eid,self.sal,self.comm,self.c_loc,self.c_name,self.c_phno)
#     def rename(self,n_name):
#         self.ename=n_name
#     def ch_sal(self,nsal):
#         self.sal=nsal

# emp1=Company('vishal',101,6700000,None)
# emp2=Company('SSR',102,7600000,200)
# emp3=Company('Rio',103,6700000,200)

# emp3.ch_sal(6800000)
# emp1.rename('Hiranyakashyap')
# emp1.display()
# time.sleep(2)
# emp3.display()
# time.sleep(2)
# Company.display(emp2)

# class Bank:
#     b_name='Kotak'
#     b_name='Gurugram'
#     ifsc='KKBK000726'
#     balance=0
    
#     def __init__(self,name,accno,ph):
#         self.name=name
#         self.accno=accno
#         self.ph=ph
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"after deposit the balance is {self.balance}")
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"balance is {self.balance}")
#         else:
#             print("insufficient balance")
#     def show_bal(self):
#         print(f"your balance is {self.balance}")

# ob1=Bank('nitin',98765645443,9876543245)
# ob1.deposit(200000)
# ob1.withdraw(30000)

# class Demo:
#     a=10
#     _b=20
#     __c=30
#     def display(self):
#         print(self.a,self._b,self.__c)
#     def getters(self):
#         return self.__c
#     def setters(self,new):
#         self.__c=new
# ob1=Demo()
# ob1.display()

# abstraction:
# from abc import ABC,abstractmethod
# import abc
# class Whatsapp(abc.ABC):
#     @abc.abstractmethod
#     def chat(self):
#         ...
#     @abc.abstractmethod
#     def camera(self):
#         ...
#     @abc.abstractmethod
#     def status(self):
#         ...
# class Dev1(Whatsapp):
#     def chat(self):
#         print("chat is being worked on")
# class Dev2(Dev1):
#     def camera(self):
#         print("camera is being worked on ")
# class Dev3(Dev2):
#     def status(self):
#         print("status is being worked on")

# d1=Whatsapp()
# d1.status()
# d1.camera()
# d1.chat()
