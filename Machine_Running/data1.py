import csv

f1 = open('data1.csv', 'w', encoding='utf8', newline='')
wr1 = csv.writer(f1, delimiter=',', quotechar='"')

wr1.writerow([73,80,75,152])
wr1.writerow([93,88,93,185])
wr1.writerow([89,91,90,180])
wr1.writerow([96,98,100,196])
wr1.writerow([73,66,70,142])
wr1.writerow([53,46,55,101])
wr1.writerow([69,74,77,149])
wr1.writerow([47,56,60,115])
wr1.writerow([87,79,90,175])