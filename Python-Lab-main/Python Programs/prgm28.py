list1=input("enter the color list1")
list2=input("enter the color list2")
result=[]
c=list1.split()
d=list2.split()
list=[x for x in c if x not in d]
print(list)

      
