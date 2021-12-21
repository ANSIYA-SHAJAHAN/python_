class student:
    def __init__(self,rollno,name,m1,m2,m3,average):
        self.rollno=rollno;
        self.name=name;
        self.m1=m1;
        self.m2=m2;
        self.m3=m3;
        self.average=average;
    def display(self):
        print("rollno=",self.rollno);
        print("name=",self.name);
        print("average=",self.average);
print("enter the number of students");
n=int(input());
list = []
for i in range(1,n+1):
    print("Enter the roll no")
    r=int(input())
    print("Enter the name")
    name=input()
    print("Enter the m1")
    m1=int(input())
    print("Enter the m2")
    m2=int(input())
    print("Enter the m3")
    m3=int(input())
    total=m1+m2+m3;
    average=(total*3)/100;
    list.append( student(r,name,m1,m2,m3,average));
for obj in list:
    obj.display();
