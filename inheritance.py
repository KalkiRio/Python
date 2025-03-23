# Inheritance
"""
1.Single level Inheritance
2.Multi level Inheritance
3.Multiple level Inheritance
4.Hierarchical level Inheritance
5.Hybrid level Inheritance
"""
# 1.Single level Inheritance

"""
class Father:
    def land(self):
        print("12 Acres")

class Son(Father):
    def business(self):
        print("Dairy Farm")

s = Son()
s.land()
s.business()
"""

"""
class Father:
    def land(self):
        print("12 Acres Of Land")

class Son(Father):
    def land(self):
        # super().land()
        Father().land()
        print("15 Acres of land")

s = Son()
s.land()
"""
"""
class Father:
    def __init__(self):
        print("Parent class is executing")

class Son(Father):
    def __init__(self):
        super().__init__()
        print("Son class is Executing")
Son()
"""

# 2.Multi level Inheritance

"""
class GrandFather:

    def land(self):
        print("24 Acres of land")


class Father(GrandFather):

    def land(self):
        # super().land()
        print("12 Acres of Land")


class Son(Father):

    def land(self):
        GrandFather().land()
        Father().land()
        print("10 Acres of Land")



s = Son()
s.land()
"""
"""
class GrandFather:
    def __init__(self):
        print("GrandFather class is executing")
class Father(GrandFather):
    def __init__(self):
        # super().__init__()
        super().__init__()
        print("Father class is executing")


class Son(Father):
    def __init__(self):
        # super().__init__()
        super().__init__()
        print("Son class is executing")

Son()
"""

# 3.Multiple level Inheritance

"""
class Father:

    def land(self):
        print("24 Acres of land")

class Mother:

    def gold(self):
        print("10Kg of gold")


class Son(Father,Mother):

    def business(self):
        print("spending money to girlfriend")


s = Son()
s.land()
s.gold()
s.business()
"""


"""
class Father:

    def land(self):
        print("24Acres of land")


class Mother:

    def land(self):
        print("10Acres of land")


class Son(Father,Mother):

    def land(self):
        Father().land()
        Mother().land()
        print("8 Acres of land")

s = Son()
s.land()
"""




"""
class Father:

    def __init__(self):
        print("24Acres of land")


class Mother:

    def __init__(self):
        print("10Acres of land")


class Son(Father,Mother):

    def __init__(self):
        Father()
        Mother()
        print("8 Acres of land")

Son()
"""
# 4.Hierarchical level Inheritance


"""
class Parent:
    def land(self):
        print("24 acres")

class Child1(Parent):
    def robbery(self):
        print("1lakh per month")


class Child2(Parent):
    def begger(self):
        print("50k per month")

class Child3(Parent):
    def engineer(self):
        print("Berozgar")


mama = Child1()
mama.robbery()
mama.land()

mama = Child2()
mama.begger()
mama.land()


mama = Child3()
mama.engineer()
mama.land()
"""

"""
class Parent:
    def engineer(self):
        print("Berozgar on that time")

class Child1(Parent):
    def enginner(self):
        super().engineer()
        print("Berozgar mai bhi hogaya")


class Child2(Parent):
    def engineer(self):
        print("Papa Just miss hoke mai bhi ban gaya")



class Child3(Parent):
    def engineer(self):
        print("Lucky se pass kardaiya but job mile tak mai bhi berozgar hun")

mama = Child1()
mama.enginner()
"""

# 5.Hybrid Inheritance

"""
class Father:
    def display(self):
        print("Father class is executing")

class Mother:

    def m_display(self):
        print("Mother class is executing")


class Son1(Father,Mother):
    def s1_display(self):
        print("Son class is executing")

class Son2(Son1):
    def s2_display(self):
        print("Son2 class is executing")


s = Son2()
s.m_display()
s.display()
s.s1_display()
s.s2_display()
"""
"""
class GPay:
    ...


class Whatsapp(GPay):
    ...

class Amazon(GPay):
    ...

class Flipkart(GPay):
    ...

"""


# class FlightBooking:
#     ...

# class TrainBooking:
#     ...

# class MakeMyTrip(FlightBooking,TrainBooking):
#     ...







