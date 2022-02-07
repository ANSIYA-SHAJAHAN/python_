import csv

mydict=[{'Name':'Ansiya','Department':'Computer','Roll No':'12'},
        {'name':'Afsal','Department':'Commerce','Roll No':'10'},
        {'name':'Suhail','Department':'Science','Roll No':'36'}]

fields=['Name','Department','Rollno']

with open('whoknows.csv','r+') as new_csvfile:

    writer = csv.DictWriter(new_csvfile,fieldnames=fields)

    writer.writeheader()

    writer.writerows(mydict)

    new_csvfile.close()
    
with open('whoknows.csv','r') as csvfile:

    read=csv.reader(csvfile)
    for rows in read:
        print(rows)
