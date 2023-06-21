from pprint import pprint

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

data = pd.read_csv("nbc.csv")

x = data.iloc[:, :-1]
y = data.iloc[:, -1]

le_Pregnancies = LabelEncoder()
x.Pregnancies = le_Pregnancies.fit_transform(x.Pregnancies)

le_Insulin = LabelEncoder()
x.Insulin = le_Insulin.fit_transform(x.Insulin)

le_BloodPressure = LabelEncoder()
x.BloodPressure = le_BloodPressure.fit_transform(x.BloodPressure)

le_Glucose = LabelEncoder()
x.Glucose = le_Glucose.fit_transform(x.Glucose)
# Pregnancies Insulin Glucose BloodPressure

le_BMI = LabelEncoder()
x.BMI = le_BMI.fit_transform(x.BMI)

le_Age = LabelEncoder()
x.Age = le_Age.fit_transform(x.Age)

le_Diabetics = LabelEncoder()
x.Diabetics = le_Diabetics.fit_transform(x.Diabetics)

le_SkinThickness = LabelEncoder()
x.SkinThickness = le_SkinThickness.fit_transform(x.SkinThickness)

pprint(f'The test data is:\n{x.head()}')

le_Outcome = LabelEncoder()
y = le_Outcome.fit_transform(y)

print(f'The test output is:\n{y}')
# BMI Age Diabetics SkinThickness Outcome

x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.2)

gnb = GaussianNB()
gnb.fit(x_train, y_train)

print(f'The accuracy score is:\n{accuracy_score(gnb.predict(x_test), y_test)}')
