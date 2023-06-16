import csv, numpy

# data_lst = []
def sort_age_group(myDict):


def sort_dict(myDict):
    myKeys = list(myDict.keys())
    myKeys.sort()
    sorted_dict = {i: myDict[i] for i in myKeys}
    return sorted_dict

# print(data_lst)
#Sort by age groups
def count_age_group(data):
    age_dict = {}
    for line in data:
        # print(line)
        age = line.get('age')
        if age in age_dict:
            age_dict[age]+=1
        else:
            age_dict[age]=1
    age_dict = sort_dict(age_dict)
    print(age_dict)

with open('insurance.csv','r', newline='') as csv_file:
    reader = csv.DictReader(csv_file)
    # for line in reader:
    #     print(line.get('age'))
    count_age_group(reader) # age range collected 18->64


# What the average bmi for certain age groups (20s,30s,40s)




# Same but with the amount of money insurance

# No of babies for female below 25s

#Difference between non-smokers and smokers, no of babies, insurance cost?

#Average age to have a baby 