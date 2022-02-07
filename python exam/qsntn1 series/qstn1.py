import csv
dict_value = [
{"Name":"Ansiya","MFC":88,"DC":99,"DS":78,"ASE":58},
{"Name":"Afsal","MFC":78,"DC":69,"DS":77,"ASE":58},
{"Name":"Sahal","MFC":68,"DC":99,"DS":58,"ASE":78},
{"Name":"Suhail","MFC":68,"DC":69,"DS":73,"ASE":88},
{"Name":"Safa","MFC":85,"DC":69,"DS":76,"ASE":78},
{"Name":"Arif","MFC":58,"DC":99,"DS":75,"ASE":78},
{"Name":"Amina","MFC":84,"DC":95,"DS":98,"ASE":70},
{"Name":"Fahad","MFC":48,"DC":99,"DS":98,"ASE":79},
{"Name":"Badusha","MFC":89,"DC":89,"DS":78,"ASE":68},
{"Name":"Bilal","MFC":85,"DC":79,"DS":88,"ASE":78},]


fields = ["Name","MFC","DC","DS","ASE"]

with open('book1.csv','w') as csvfile:
    writer = csv.DictWriter(csvfile,fieldnames=fields)
    writer.writeheader()
    writer.writerows(dict_value)
    csvfile.close()
print("percentage\n")
mfc=0
dc=0
ds=0
ase=0

with open('book1.csv','r') as csvfiles:
    readerobj = csv.DictReader(csvfiles)
    for row in readerobj:
         print(row['Name'],":",float(float(int(row['MFC'])+int(row['DC'])+int(row['DS'])+int(row['ASE']))/400)*100,"%")
         mfc=mfc+int(row['MFC'])
         dc=dc+int(row['DC'])
         ds=ds+int(row['DS'])
         ase=ase+int(row['ASE'])
print("average ")
print("MFC",mfc/10)
print("DC",dc/10)
print("DS",ds/10)
print("ASE",ase/10)
