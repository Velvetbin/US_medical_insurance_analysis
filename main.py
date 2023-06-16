import csv, numpy

with open('insurance.csv','r', newline='') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(', '.join(row))
under_20s = []
#Sort by age groups
for row in reader:
    if row[0] < 20:
        under_20s.append(row)
print(under_20s)

# What the average bmi for certain age groups (20s,30s,40s)




# Same but with the amount of money insurance

# No of babies for female below 25s

#Difference between non-smokers and smokers, no of babies, insurance cost?

#Average age to have a baby 