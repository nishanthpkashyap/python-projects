import csv
from pprint import pprint

with open("cea.csv") as f:
    file = csv.reader(f)
    data = list(file)
    specific = data[0][:-1]
    general = [['?' for i in range(len(specific))] for j in range(len(specific))]

    for i in data:
        if i[-1] == 'Yes':
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    specific[j] = '?'
                    general[j][j] = '?'
        else:
            for j in range(len(specific)):
                if i[j] != specific[j]:
                    general[j][j] = specific[j]
                else:
                    general[j][j] = '?'

        print(f'Step {data.index(i)+1}:\nGeneral:\n{general}\nSpecific:\n{specific}')

    gh = []
    for i in general:
        for j in i:
            if j != '?':
                gh.append(i)
    print(f'General:\n{gh}\nSpecific:\n{specific}')
