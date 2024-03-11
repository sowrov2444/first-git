#first program
import turtle

print("hablu")

#comment deya
'''2nd commnt type'''

#pip moduel diye je kono module install korte pari

#python variables
name="Sowrov"#sowrov ta hocche variables

'''data type'''
#str type #name decler er somoy laste number deya jai
file1="pala"
file="hab34"#double cotesion a ja thakbe tai str type
print(file1 +' '+ file)

#number type
# int type
file=345
print(file)
#floating type
file=12.4
print(file)
#complex type
file=34j#j chara onno kichu deya jabe na
print(file)

#boolien type
file=True
print(file)
file=False
print(file)
x=3
y=7
print(x>y)
print(x<y)

#string formating
x=3
y=5
print(f"result is = {x+y}")

#binary type, range holo 256 porjonto
file=[2,4,54,64,65]
file=bytes(file)
print(file)
file=[34,53,87,93]
file=bytearray(file)
print(file)

#none type #valu less #0 and true false none type na
file=None
print(file)

#sequence type
#list type #mutable
file=["file","name","age"]

#tuple type #inmutable
file=("file","name","age")
print(file)
#range type
for i in range(5):
    print("file")

#operators
#addition (+)
x=10
y=5
z=(x+y)
print(z)
#subtraction (-)
x=10
y=5
z=(x-y)
print(z)
#division (/)
x=10
y=5
z=(x/y)
print(z)
#multiplication (*)
x=10
y=5
z=(x*y)
print(z)
#modulus (%)
x=10
y=5
z=(x%y)
print(z)
#exponentiaton (**)
x=10
y=5
z=(x**y)
print(z)
#floor division (//)
x=10
y=5
z=(x//y)
print(z)

#assignment operators
x=5
y=x+10
print(y)
#sort
x+=10
print(x)

#comparison operators
#equal (==)
x=10
y=10
print(x==y)
#not equal (!=)
x=10
y=5
print(x!=y)
#greater than (>)
x=10
y=5
print(x>y)
#less than (<)
x=10
y=15
print(x<y)
#greater than or equal to (>=)
x=15
y=10
print(x>=y)
#less than or equal to (<=)
x=10
y=15
print(x<=y)

#swapping
x=5
y=10
x,y=y,x
print(x,y)

#type casting
x="12345"
x=int(x)
print(x)
x=float(x)
print(x)

#list niye kaj kora
lis=[1,3,5,"file",True]
print(lis[3])
lis[0]=22
print(lis)

#access list item
file=["name","age","school","villige","city"]
print(file[1])

#change list item
file=["name","age","school","villige","city"]
file[4]="town"
print(file)

#add list item
file=["name","age","school","villige","city"]
file.append("town") #append mathod last a item add kore
print(file)
file.insert(4,"dristik")
print(file)

#remove list
file=["name","age","school","villige","city"]
file.remove("age")#remove mathod a name bole dite hobe
print(file)
file.pop()#nije nije remove kore
print(file)
del file[0]
print(file)

#clear list
file=["name","age","school","villige","city"]
file.clear()
print(file)

#loop list
file=["name","age","school","city"]
for i in file:
    print(i)
for i in range(len(file)):
    print(i)
x=0
while x<len(file):
    print(file[x])
    x+=1
x=0
while x<4:
    print(file[x])
    x+=1

#list comprehension
file=[1,3,5,6,9]
for i in file:
    print(i * 2)
file1=[i *2 for i in file] #+,-,/,* sob kora jabe
print(file1)

#sort list
file=[8,3,1,5,6,9,2]
file.sort()
print(file)
file.sort(reverse=True)
print(file)
file.reverse()
print(file)
file=["name","age","school","city"]
file.sort()
print(file)

#copy list
file=[1,3,5,6,9]
file1=file.copy()
print(file1)

#join list
file=[1,3,5,6,9]
file1=["file","age","school"]
file.extend(file1)
print(file)

#count list
file=[1,3,5,5,6,6,9]
print(file.count(5))

#matrix
file=["name",["date","time"],["minit","secend"]]
print(file[1][1])

#tuple type immutable
file=("name","age","school","city")
print(file)
print(file[-3]) #-mane last theke asbe
print(file[2])
print(file[1:4])

#update tuple
file=("name","age","school","city")
file= list(file)
file.insert(2,"old")
print(file)
file=tuple(file)
print(file)

#unpake tuple
file=("name","age","school","city")
a,b,*c=file
print(a,b,c)
*a,b=file
print(b,a)

#join tuple
file=("name","age","school","city")
file1=("old","collage","town")
file2=file+file1
print(file2)
file=("name","age","school","city")#number o hobe
print(file*3)

#loop tuple
file=("name","age","school","city")
for i in file:
    print(i)
for i in range(len(file)):
    print(i)
for i in range(len(file)):
    print(file[i])
x=0
while x < len(file):
    print(file[x])
    x+=1
file=("name","age","school","city")
print(file.count("name"))
print(file.index("school"))

#set type #unchaneable but remove and add item support
file={"name","age","school","school","city"}#dubble item not support
print(file)#seriel not suppor random vabe hobe
print(len(file))

#access set item
file={"name","age","school","city"}
print("school"in file)

#add set item
file={"name","age","school","city"}
file.add("town")
print(file)
file={"name","age","school","school","city"}
file1={"first","secend"}
file2=["wow","nice"]
file.update(file1)
file1.update(file2)
print(file)
print(file1)

#remove set item
file={"name","age","school","city"}
file.remove("name")
print(file)
file.discard("age")#thakle remove korbe na thkle error dibe na
print(file)
file.pop()
print(file)
file.clear()
print(file)

#loop list
file={"name","age","school","city"}
for i in file:
    print(i)

#join set
file={"name","age","school","city"}
file1={2,3,5,}
file2=file.union(file1)
print(file2)

#dictionaries
document={"1file":
              {"name":"sowrov",
                   "age":19,
                   "school":"gazipur"},
          "2file":
              {"name":"topu",
               "age":18.4,
               "school":"uttra"},
          "file":"hardilk",}
print(document["1file"]["age"])
#access dictionaries
print(document.keys())
print(document.get("file"))
print(document.values())
#update dictionaries
document["1file"]["name"]="rashedul"
print(document["1file"])
document.update({"file":"lion"})
print(document["file"])
#remove dictionaries
document={"1file":
              {"name":"sowrov",
                   "age":19,
                   "school":"gazipur"},
          "2file":
              {"name":"topu",
               "age":18.4,
               "school":"uttra"},
          "file":"hardilk",}
document.pop("file")
print(document)
document.popitem() #popitem nmae dhore ba lasterta remove hobe
print(document)
document.clear()
print(document)
#del mathod diye sob remove kore print korle error asbe

#loop dictionari
document={"1file":
              {"name":"sowrov",
                   "age":19,
                   "school":"gazipur"},
          "2file":
              {"name":"topu",
               "age":18.4,
               "school":"uttra"},
          "file":"hardilk",}
for i in document:
    print(i)
for i in document.values():
    print(i)
for i in document.keys():
    print(i)
for i in document.items():
    print(i)

#copy dictionaries
document={"1file":
              {"name":"sowrov",
                   "age":19,
                   "school":"gazipur"},
          "2file":
              {"name":"topu",
               "age":18.4,
               "school":"uttra"},
          "file":"hardilk",}
document1=document.copy()
print(document1)
document2=dict(document)
print(document2)

#if statements
a=5
b=10
if a==b:
    print("equel")
elif a<b:
    print("b is big")
elif a>b:
    print("a is big")
elif a!=b:
    print("right")
else:print("good bye")
file=["sobji","piyas","alu"]
for i in file:
    if i=="piyas":
        break
    print(i)

#finsion
def file(a,b):
    file=(a+b)
    print(file)

file(40,45)

def file1(a,b):
    file1=(a-b)
    print(file1)

file1(23,45)

#break and continu
file=[1,5,6,7,3,4,2]
for i in file:
    if i==5:
        break
    print(i)
file=[5,6,7,8]
for i in file:
    if i==6:
        continue
    print(i)

#recursion #limit 1000 hajar porjonto
def file():
    print("hello")
    file()
    file()

#zep file #aktar sate arakta join hobe
file=["sobji","piyas","alu"]
file1=["file","age","school"]
file2=list(zip(file,file1))
print(file2)

#debuging
x=0
while x<5:
    print(x)
    x+=1

#lamda
def file(a,b):
    file1=(a-b)
    print(file1)
file(34,54)
file= lambda a,b,c,d:(a+b)+(c-d) #funsion er vitor sortcut a kaj kora
print(file(11,54,6,6))

#array #list er moto sob kichu kora jai
#array holo list er caite sort space to fast kaj kore
filee=["name","school","collage","age"]
print(filee)

#classes and objects
class file:
    school = ""
    name = ""
    age = ""

x=file
x.age=19
#x=file.name="sojib"
print(x.age)
y=file
y.school="high school"
print(y.school)

#inheritance
class pirson:
    canname="bmw"
    model="rb1"
    no=100
class pirson1(pirson):
    rode=20
    brand="BMW"
x=pirson1()
print(x.model)

#multiple inheritance
class pirson2:
    canname="bmw"
    model="rb1"
    no=100

class pirson3(pirson2):
    car="audi"
    number=193
    date=12-3
class pirson4(pirson3):
    compani="bd"
    country="bangladesh"
hi=pirson4
print(hi.canname)

#iterators
file=["name","age","school",3,6,66]
file=iter(file)
print(file.__next__())
print(next(file))

#scope
a=44 #global sobai use korte pare
def scope():
    t=50 #local shudu nije use korte parbo
    print(t)
    print(a)
scope()
print(a)
#print(t)

#datetime
import datetime
a=datetime.datetime.now()
print(a)
print(a.strftime("%A"))
print(a.strftime("%d"))

#math module
file=[33,65,73,9,23,5]
print(min(file))
print(max(file))
print(abs(-344))#(-)ke (+) kore
print(pow(3,4)) #3 4bar gun hobe

#try and except
try:
    file=["jablu","lablu"]
except:
    ablu=["jadu","hablu",hala]
    print(ablu)
print(file)

#file opening
file=open("module.py","r")
print(file.read())

#file write
file=open("module.py","w")#w dile sob chole jabe #a dile sob thakbe
file.write("hello vai")   #w thakle read use korte parbo
file.write("oiiii \n")#\n dile niche line hobe
#print(file.read())

#delet file
import os
#os.remove("file1.text") #run korar por delet hoi pore run korle error ashe
#os.rmdir("adobe")#folder deler korar jonno

#reger #aro onek ache nije nije shikte hobe
file="hello vaisobai kemon acho"
import re
file=re.findall("[a-f]",file)
print(file)
file="hello"
file=re.findall(file,file)
#print(file)
if file:
    print("yes")
else:
    print("no")

#creating your own module
import module1 #1
file=module1.file1
import module1 as A #2
file=A.tasin
from module1 import file1 #3
module1.file1

#constructor
class fajlami:
    def fajlami1(self,name,age):
        print(f"hello vai {name},ki khobor {age}")
f=fajlami() #() dite hobe
f.fajlami1("hablu:",10)
f.fajlami1("balb",29)
#parameterized constructor
class fajlami1:
    def __init__(self,name,age):
        print(f"hii how are you {name},your age {age}")
f=fajlami1("harba",35)

#class meathod #static meathod #instence meathod
class file3:
    def file4(self): #instence meathod
        print("hello instence meathod")
    @classmethod  #class meathod
    def file5(cls):
        print("hello class meathod")
    @staticmethod #staticmethod easy uses no argument
    def file6():
        print("hello static meathod")
f1=file3() #instence meathod ei vabe
f1.file4()
file3.file5() #class meathod a sort a pawa jai
file3.file6()#staticmethod easy uses no argument

#polymorphism  akta diye sob khane
class poly:
    def __init__(self,name,model,number,registry,make):
        self.name=name
        self.model=model
        self.number=number
        self.registry=registry
        self.make=make
class all(poly):
    pass
plane=all("fly","505","11","2021","bd")
print(plane.registry)
car=all("BMW","443","6555","2022","chaina")
print(car.registry,car.number)

#incapsulation (__)ba kono kichu hide kora ja khane kaj korbo oi khane dekha jabe
class poly:
    def __init__(self,name,model,number,registry,make):
        self.__name=name
        self.__model=model
        self.__number=number
        self.__registry=registry
        self.__make=make

    class all(poly): #incapsulation #shudhu vitore pawa jabe
        pass

    plane = all("fly", "505", "11", "2021", "bd")
    print(plane.registry)

#moduel er vitor ki ki ache ta ber kora
import timeit
print(dir(timeit))

#math moduel er kaj
import math
print(math.pi)
print(math.pow(3,5))
print(math.sqrt(15))
print(math.floor(3.7))
print(math.ceil(5.3))
#open browser
import webbrowser as we
#url="https://www.youtube.com/watch?v=huRCktXW0ao" #link dite hobe cotesoner vitor
#we.open(url)
True

import sys
print(sys.path)

#fibonacchi number
def file(x):
    if x<=2:
        return 1
    fix,fix1=1,1
    i=3
    while i<=x:
        i+=1
        fix,fix1=fix1,fix+fix1
    return fix1
for i in range(1,11):
    print(file(i))

file=3,3
print(file)

import calendar
fil=calendar.monthcalendar(2024,1)
print(fil)

def fib(n):
    if n<=2:
        return 1
    x,next=1,1
    i=3
    while i<=n:
        i+=1
        x,next=next,x+next
        return next
def list(n):
    list1=[1,1]
    if n<=2:
        return list1[:n]
    x,next=1,1
    i=3
    while i<=n:
        i+=1
        x,next=next,x+next
        list1.append(next)
    return list1
for i in range(1,2):
    print(fib(i))
    print(list(1))
    print(list(2))
    print(list(10))

"""monte=turtle.Turtle()
fonte=turtle.Turtle()"""




#user input
name=input("inter your name:")
password=input("inter your password:")
print(name)
print(password)

"""file={"pirsion":{
    "name":"sowrov",
    "age":14,
    "school":"gazipur",},
"pirsion1":{
    "name":"safi"
},"farabi":"jamila"}
print(file)"""

