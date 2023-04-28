##l=10
##b=4
##print("addition:",(l&b))#9
##print("addition:",(l|b))#-5
##print("addition:",(l^b))#14
##print("addition:",(~b))#3.5
##print("addition:",(l>>2))#1
##print("addition:",(l<<2))#-5
###print("addition:",(l//b))
##num=int(input("Enter the length:"))#56
##print(num)
##num=input("Enter the length:")#56,fghj
##print(num)
##number=int(input("Enter the number:"))
##print(type(number))
##print("You have enter the number is:",number)
##print("binary number of",number,"is",bin(number))
##print("binary number of",number,"is",oct(number))
##print("binary number of",number,"is",hex(number))
##a=1.908
##print(type(a))
#String="networkz system"
##print(String)
##print("Welcome"+String)
##print(String*2)
##print(String[5])
##print(String[0:6])
##print(String[2:])
##print(String[:3])
##print(len(String))
##print(max(String))
##print(min(String))
##print(String.upper())
##print(String.lower())
##print(String.title())
##print(String.capitalize())
##list=["ab","bc",2,4,5]
##list[2:3]=[8,9,10]
###list.insert(0,6)
##print(list)
##del list[1]
##print(list)
##aset={2,3,5,10,6,7,4}
##print(aset)
##setone={"apple","grapes","banana"}
##print(setone)
##number={ 0 : 0, 1 : 4, 2 : 9, 3 : 49, 4 : 72 }
##print(len(number))
##print(sorted(number))
##print(number.pop(1))
##class Employee:
##    employeeId="101"
##    employeeName="Anadh"
##detailobj=Employee()
##print("Employee Id is:",detailobj.employeeId)
##print("Employee Name is:",detailobj.employeeName)
##
##class Rectangle:
##    l=8
##    b=7
##rectangleobj=Rectangle()
##print("Length is%d,Breadth is %d"%(rectangleobj.l,rectangleobj.b),
##      "=",rectangleobj.l*rectangleobj.b)

##class rect:
##    l=9
##    b=7
##    def rectArea(self):
##        return rect.l*rect.b
##rectobj=rect()
##print("Area of rectangle is:",rectobj.rectArea())


##class rect:
##  
##    def __init__(self,l,b):
##        self.l=l
##        self.b=b
##    def rectarea(self):
##        return self.l*self.b
##rectobj=rect(4,5)
##print("Area of rectangle is:",rectobj.rectarea())
##

##class Employee:
##    def __init__(self,name,salary,address):
##        self.name=name
##        self.salary=salary
##        self.address=address
##    def printEmpDetail(self):
##            print("Employee Name is:",self.name,"\n",
##                  "Employee salary is:",self.salary
##                  ,"\n","Employee Address is:",self.address)
##empobj=Employee("Anadh","6000000","Marthandam")
##print("Anadh Detail........")
##print(empobj.printEmpDetail())
##print("Sanjay deatail.........")
##empobj1=Employee("Sanjay","45567","Pallapalam")
##print(empobj1.printEmpDetail())

##class book:
##    price=100
##    @classmethod
##    def display(cls):
##        print(cls.price)
##    def show(self,x):
##        self.price=x
##        print(self.price)
##    
##b=book()
##b.display()
##book.display()
##b.show(200)

##class book:
##    @staticmethod
##    def display():
##        l=20
##        print("the value of l is:",l)
##b=book()
##book.display()
##b.display()



##class Rectangle:
##    def __init__(self,l,b):
##        self.l=l
##        self.b=b
##    def rectarea(self):
##        return self.l*self.b
##class Triangle (Rectangle):
##    def __int__(self):
##        Rectangle.__init__(self)
##    def trianglearea(self):
##        return 1/2*self.l*self.b
##obj=Triangle(4,6)
##print("Area of rectangle:",obj.rectarea())
##print("Area of Traiangle is",obj.trianglearea())

##class rect:
##    def __init__(self):
##        self.l=8
##        self.b=5
##    def area(self):
##        return self.l*self.b
##class triangle:
##    def __init__(self):
##        self.x=17
##        self.y=13
##    def area(self):
##        return 1/2*self.x*self.y
##class both(triangle,rect):
##    pass
##r=both()
##print("Area of rectangle is ",r.area())
##
##class samsungmobile:
##    def __init__(self,name,device,ram):
##        self.name=name
##        self.device=device
##        self.ram=ram
##    def mobiledetail(self):
##        print("Mobile name:",self.name,"\n","Device is:",
##              self.device,"\n","Ram is:",self.ram)
##class Redmi(samsungmobile):
##    def __init__(self,name,device,ram):
##        samsungmobile.__init__(self,name,device,ram)
##    def mobiledetail(self):
##        print("Mobile name:",self.name,"\n","Device is:",
##              self.device,"\n","Ram is:",self.ram)
##s=samsungmobile("xx","and","4")
##print(s.mobiledetail())
##r=Redmi("yy","vv","7")
##print(r.mobiledetail())
##n=nokia("ff","yy","8")
##print(n.mobiledetail())
##        
####        
##class SomeObj:
##
##    def __init__(self):
##        print('The object is created.')
##
##    def __del__(self):
##        print('The object is destroyed.')
##
##obj1 = SomeObj()
##obj2 = obj1
##obj3 = obj1
##print("Set obj1 to None...")
##obj1 = None
##print("Set obj2 to None...")
##obj2 = None
##print("Set obj3 to None...")
##obj3 = None

##import calendar
##year=int(input("Enter year: "))
##calendar.prcal(year)
##f=open("aboutpython.txt","r")
##line=f.readline()
##print("A line from files is :",line)
##f.seek(5)
##line=f.readline()
##print("The line from character 6 till end of line is :", line)
##print("The pointer is at location",f.tell())
##f.seek(10)
##line=f.read(20)
##print("The fifteen character starting at location 11 are as: ", line)


##str="Hello World"
##f=open("binary.bin","wb")
##f.write(str.encode('utf-8'))
##f.close()
##f=open("binary.bin","rb")
##fcontent=f.read()
##f.close()
##print("The content in the file is :")
##print(fcontent.decode('utf-8'))
##import csv
##with open("anne.csv","r") as f:
##    data=csv.reader(f)
##    for i in data:
##        print(i)



##import csv
##heading=["S.No","Name","Place"]
##content=[["1","shalini","kollemcode"],
##         ["2","lini","kollemcode"],["3","shalini","kollemcode"]]
##with open("an.csv","w") as f:
##    data=csv.writer(f)
##    data.writerow(heading)
##    data.writerows(content)
a=10
try:
    print (a/0)
except Exception as ex:
    print(ex)
finally:
    print("fghj")
    





