import csv
with open('whoknows.csv', newline='') as csvfile:
 data = csv.DictReader(csvfile)
 for row in data:
   print(row['NAME'], row['ROLL NO'])
