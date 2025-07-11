import csv

# path=r"C:\Users\Ribhu\Downloads\sample.log"

# with open(path) as file:
#     print(file.read())

# path=r"C:\Users\Ribhu\Downloads\vaccine.csv"

#write the data

# with open('demo.txt','w') as file:
#     file.write("soon We will complete the python class\nwelcome to python class")
#     data1 = "Soon we will complete the class\n"
#     data2 = "welcome to python class"
#     file.writelines([data1,data2])

#read the data

# with open('demo.txt') as file:
    # data = file.read()
    # print(data)
#    data1 = file.readline()
#    data2 = file.readline()
#    data3 = file.readline()
#    data4 = file.readline()
#    data5 = file.readline()
#    print(data1)
#    print(data2)
#    print(data3)
#    print(data4)
#    print(type(data5))
    # data = file.readlines()
    # print(data)

# with open('demo.txt') as file:
#     data = file.read()
#     count = 0
#     for i in data.split():
#         if i == 'python':
#             count+=1
#     print(count)

# with open("simple.txt","x") as file:
#     pass


# path = r"D:\Python\sample.log"
# with open(path) as file:
#     data = file.readlines()
#     for i in data:
#         print(i)





'''
# Before handling any files get the accessibility of a File
#In python open() function is used to get the acessibility of a file
#In python close() is used to close the file

WE CAN GET THE ACCESSIBILITY IN TWO WAYS:
--> without context manager(not using keyword with)
--> with context manager(using with keyword)

-->without context manager:
    if we open a file without context manager explicitly we have to
    close the file using close function else the data will be destroyed
SYNTAX:
    variable = open('file_path/filename','mode')
    variable.close()

--> with context manager:
    if we open a file using with context manager no need
    to close the file explicitly 
SYNTAX:
    with open('file_name/file_path','mode') as ALIAS:
        -----Statement Block--------

MODE:
#It defines based on what requirement we are going to take the 
accessibility

mode:
    1.write --> w
    http://2.read --> r
    3.append --> a
    4.create --> x
#Bt default it opens in the file in read mode

1.write mode(w):
    *It is used to create the data into the file
    *In this case is the file is not existing then control will create a new file data will be written
    *If the file is already exist then control will overwrite the data by the new data

TO CREATE THE DATA WE HAVE TO USE
    1.write()
    2.writelines()

1.write():
    *By using write function it is possible to write a single line of data to the file
    *It accepts string
SYNTAX:
    variable/alias_name.write('new_data'/variable)


2.writelines():
    *By using this function it is possible to write multiple lines of data in the form of list

SYNTAX:
    varible/alias_name.writelines(['line1','line2','line3'......'line n'])

write() W.R.T with context manager:
with open('demo.txt','w') as file:
    file.write("soon We will complete the python class\nwelcome to python class")

write() W.R.T without context manager:
file = open('demo.txt','w')
file.write("Hello world")
file.close()

writelines() W.R.T with context manager:
with open('demo.txt','w') as file:
    data1 = "Soon we will complete the class\n"
    data2 = "welcome to python class"
    file.writelines([data1,data2])

    
writelines() W.R.T without context manager:
file = open('demo.txt','w'):
data1 = "Soon we will complete the class\n"
data2 = "welcome to python class"
file.writelines([data1,data2])
file.close()
'''






#--------------------------------------------------------------------
# append mode (a):
#     *It is similar to write mode but if the file is already
# exist it will not destroy the previous data just it will add the
# new data to a file 
#     *Overwriting will not happen
# with open('sample.txt','a') as file:
    # file.write("hello world welcome")
    # file.write("Today's concept is file handling")
    # data1 = "today because of informals students are not allowed\n"
    # data2 = "because they are taking the advantage of the trainer\n"
    # data3 = "trainer is more strict\n"
    # data1 = "Take it as serious\n"
    # file.writelines([data1,data3])
#----------------------------------------------------------------
#read mode (r):
#     *By using read mode it is possible to read the data from the
# File
#     *In this case if the file is not exist then control is going to
# throw an error
#     *Reading the data from the file can written by following functions
#     http://1.read() --> string
#     2.readline() --> string 
#     3.readlines() --> list

# read mode (r):
#     *By using read function it is possible to get the entire content
# as it is from the file
#     *The return type of this function is string
# SYNTAX:
#     variable = var/alias.read()


# with open('sample.txt') as file:
#     data = http://file.read()
    # print(data.count('s'))
    # out = 0
    # for i in data:
    #     if i == 's':
    #         out+=1
    # print(out)

#----------------------------------------------------
# readline mode ():
#     *By using this function it is possible to get line by line data
# from the file
#     *The return type of this function is string
# SYNTAX:
#     variable = var/alias.readline()


# with open("sample.txt") as file:
#     data1 = file.readline()
#     data2 = file.readline()
#     print(data1)
#     print(data2)

#----------------------------------------------------------------


# readlines mode ():
# *By using this function we can get complete data from the file
# in the form of list
# SYNTAX:
#     variable = var/alias.readlines()


# with open('sample.txt') as file:
#     data = file.readlines()
#     # print(data)
#     print(data[2])

# path = r"D:\Python\sample.log"

# with open(path) as file:
#     data = file.readlines()
#     for i in data:
#         out = i.split()
#         print(out[1])


# To open multiple file:

# path = r"D:\Python\sample.log"
# path1 = r"D:\Python\dinga.txt"

# with open(path) as file, open(path1) as file1:
#     data = file1.readlines()
#     print(data)


# path = r"D:\Python\sample.log"
# with open(path) as file:
#     data = file.readlines()
#     for i in data:
#         out = 0
#         for j in i:
#             if j == ' ':
#                 out+=1
#         print(out)


#csv file handling

# import csv
#FOR READER
# path = r"C:\Users\VASIM\OneDrive\Desktop\samsung.csv.txt"
# with open(path) as file:
#     print(csv.reader(file)) #<_csv.reader object at 0x000001B27049D420>
#     reader_obj = csv.reader(file)
#     print(list(reader_obj))
#     for i in reader_obj:
#         print(i)

#FOR DICTREADER
# path = r"C:\Users\VASIM\OneDrive\Desktop\samsung.csv.txt"
# with open(path) as file:
#     dict_obj = csv.DictReader(file)
#     print(dict_obj) #<csv.DictReader object at 0x000002C1F15F81D0>
#     print(list(dict_obj))
#     for i in dict_obj:
#         print(i)



# path = r"C:\Users\VASIM\OneDrive\Desktop\samsung.csv.txt"
# with open(path) as file:
#     data = reader(file)
#     for i in data:
#         print(i)


# path = r"D:\Python\vaccine.csv"
# with open(path) as file:
    # reader_obj = DictReader(file)
    # # reader_obj = reader(file)
    # for i in reader_obj:
    #     print(i)



# syntax:
#     reader(csv_file_address)
#         or
#     csv.reader(csv_file_address)


# syntax:
#     DictReader(csv_file_address)
#         or
#     csv.DictReader(csv_file_address)


# import csv

# path = r"D:\Python\vaccine.csv"
# with open(path) as file:
#     obj = csv.DictReader(file)
#     # for i in obj:
#     #     print(i[5])
#     for i in obj:
#         print(i['TOTAL_VACCINATIONS'])



import csv
#writer:

# with open("table.csv",'w') as file:
    # data = csv.writer(file)
    # # data.writerow(['name','placement','pending'])
    # # data.writerow(['abhi','ongoing','django'])
    # data.writerows([['name','age','gender'],['anu','22','female','python'],['nitin',23,'male']])


#DictWriter:

#writerow():

# with open("table.csv",'w') as file:
    # data = csv.DictWriter(file,["name","age","gender"])
    # data.writeheader()
    # data.writerow({"name":"nitin","age":23,"gender":"male"})
    # data.writerow({"name":"lax","age":23,"gender":"male"})

#writerows():

with open("table.csv",'w') as file:
    data = csv.DictWriter(file,["name","age","gender"])
    data.writeheader()
    data.writerows([{"name":"akash","age":24,"gender":"female"},{"name":"anu","age":22,"gender":"female"}])
    


# with open('table.csv') as file:
#     data = csv.DictReader(file)
#     for i in data:
#         print(i.values())
 

# Feb 07 - 3:41 pm
"""
file = open("demo.txt","w")
# file.write("Hello Guy's Today is the last day of python\n")
data1 = "Hello EveryOne\n"
data2 = "Gud Evevning\n"
data3 = "About to complete\n"
data4 = "File Handling"
file.writelines([data1,data2,data3])
"""

"""
file = open("demo.txt",'a')
# file.write("\nHi Nikhil dost nahi hai isiliye shaanth ho\n")
data1 = "Nikhil is going to"
data2 = "Give the rose on rose day"
data3 = "To her GF In Australia"
file.writelines([data1,data2,data3])
"""
"""
with open("demo.txt","a") as file:
    file.write("Very Boaring")
    d1 = "\nShatadru Roy"
    d2 = "perwaj Alam\n"
    d3 = "Vishal\n"
    d4 = "Sahil Sheron\n"
    d5 = "Muskan jhamb"
    file.writelines([d1,d2,d3,d4,d5])
"""
"""
with open("jhamb.txt",'x') as file:
    ...
"""
# read()
"""
with open("demo.txt") as file:
    # print(http://file.read())
    # print(len(http://file.read()))
    data = http://file.read()
    # print(len(data))
    # print(len(data.split()))
    l = []
    for i in data.split():
        if len(i)%2 == 1 :
            l.append(i)
    print(l)
"""

# readline()

"""
with open("demo.txt") as file:
    data1 = file.readline()
    data2 = file.readline()
    data3 = file.readline()
    print(data1)
    print(data2)
    print(data3)
"""


# readlines()

"""
with open("demo.txt") as file:
    data = file.readlines()
    print(data)
    print(len(data))
"""    

"""
path = """r"D:\Notes\sample.log""""

with open(path) as file:
    print(http://file.read())

"""
# CSV FILE HANDLING

import csv

"""
path = """r"a3_oops\example.csv""""
with open(path) as file:
    # print(file)
    data = csv.reader(file)
    # print(data)
    for i in data:
        print(i)
"""



"""
path = """r"a3_oops\example.csv""""
with open(path) as file:
    # print(file)
    data = csv.DictReader(file)
    # print(data)
    for i in data:
        print(i)
"""

"""
path =r"D:\Downloads\Python\vaccine.csv"
with open(path) as file:
    data = csv.DictReader(file)
    # print(data)
    count = 0
    for i in data:
        if i["TOTAL_VACCINATIONS"].strip(' '):
            # print(type(int((i['TOTAL_VACCINATIONS']))))
            count += int(i["TOTAL_VACCINATIONS"])
    print(count)
        
"""
path =r"D:\Downloads\Python\vaccine.csv"
with open(path) as file:
    data = csv.DictReader(file)
    d = {}
    for i in data:
        if i['WHO_REGION'] not in d:
            d[i["WHO_REGION"]] = [i["COUNTRY"]]
        else:
            d[i["WHO_REGION"]] += [i["COUNTRY"]]
    print(d)







