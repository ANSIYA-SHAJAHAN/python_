class employee:
   
    def __init__(self,name,emp_id,monthly_salary,department):
       
        self.name=name;
        self.emp_id=emp_id;
        self.monthly_salary=monthly_salary;
        self.department=department;
       
    def display(self):
       
        print("name=",self.name);
        print("emp id=",self.emp_id);
        print("monthly salary=",self.monthly_salary);
        print("department=",self.department);
print("enter the number of employee");
n=int (input());
list = []


for i in range(1,n+1):
    print("enter your employee id")
    i=int(input())
    print("enter your employee name")
    name=(input())
    print("enter your employee salary")
    s=int(input())
    print("enter your employee department")
    de=(input())
    list.append(employee(i,name,s,de));
for obj in list:    
    if(obj.monthly_salary==15000):
        obj.display();
