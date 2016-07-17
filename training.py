import csv as csv
from sklearn import tree

parameters = []
with open ('without_survived.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        sex = 0 if row[3] == 'female' else 1
        age = 0 if row[4] == '' else int(float(row[4]))
        parameters.append([int(row[1]), sex, age])

survived = []
with open ('with_survived.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    for row in reader:
        survived.append(float(row[0]))

print parameters
print survived
clf = tree.DecisionTreeClassifier()
clf = clf.fit(parameters, survived)
print clf


# test_data = []
# with open ('test_data.csv', 'rb') as csvfile:
    # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # for row in reader:
        # test_data.append([int(row[1]), 0 if row[3] == 'female' else 1])

# actual_survivability = []
# with open ('gender_model.csv', 'rb') as csvfile:
    # reader = csv.reader(csvfile, delimiter=',', quotechar='"')
    # for row in reader:
        # survived.append(int(row[0]))

output = clf.predict(parameters)

# percentage of wrong predictions (using same set of data to train and test)
print sum(map(lambda a: float(abs(a[0] - a[1])), zip(output, survived))) / output.size

