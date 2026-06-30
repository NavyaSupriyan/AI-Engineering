#Exploratory data analysis - EDA

import pandas as pd
import numpy as np

df = pd.read_csv('resources/titanic.csv')

print(df.head())

print(df.tail())

print(df.shape)

print(df.columns)

print(df.dtypes)

print(df.info())

print(df.describe())

print(df.isnull().sum())

#How many passengers traveled in each class
print(df['Pclass'].value_counts())

#How many males and females
print(df['Sex'].value_count())

#numerical analysis

print(df['Age'].mean())
print(df['Age'].median())
print(df['Age'].min())
print(df['Age'].max())

#Filtering

print(df[df['Age'] > 60])
print(df[['Sex'] == 'female'])

#Avg fare by class
print(df.groupby('Plcass')['Fare'].mean())

#sorting
print(df.sort_values('Age', ascending = False))

#How many passengers are there
print(df.shape[0])

#How many survived
print(df[df['Survived'] == 1].shape[0])

#What percentage survived
print((df['Survived'].mean())*100)

#Avg age
print(df['Age'].mean())

#Which class paid the highest avg fare
avg_fare = df.groupby('Pclass')['Fare'].mean()
print(avg_fare.idxmax())

#Which gender has the highest survival rate
survival_by_gender = df.groupby('Sex')['Survived'].mean()
print(survival_by_gender.idxmax())

#which passenger paid the max fare
max_fare = df['Fare'].max()
print(df[df['Fare'] == max_fare])

#Which columns has most missing values
missing = df.isnull().sum() #column wise sum
print(missing.idxmax())

#How many children on board
child = df[df['Age']<18]
print(len(child))