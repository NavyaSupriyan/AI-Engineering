#Goal: To predict if a passenger survived using their details

#Step 1: Import libraries
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.tree import plot_tree

import matplotlib.pyplot as plt

#Step 2: Loading dataset
df = pd.read_csv('resources/titanic.csv')

#Step 3 Understand the dataset
print(df.head())

print(df.columns)

print(df.isnull().sum())

#Step 4: Clean Data
df['Age'] = df['Age'].fillna(df['Age'].median()) #median preferred as it is less affected my extreme values

df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()) #since only 2 missing so used most freq to fill null

df = df.drop('Cabin', axis = 1) #Too many missing values

df = df.drop(['PassengerId', 'Name', 'Ticket'], axis = 1) #dropping unnecessary columns

#Step 5: Encode Categorical values (ML models needs numbers)

df['Sex'] = df['Sex'].map({
    'male':0,
    'female': 1
})

df['Embarked'] = df['Embarked'].map({
    'S': 0,
    'C': 1,
    'Q': 2
})

print(df.head())

#Step 6: Seperate features and target

#target
y = df['Survived']

#Features
X = df.drop('Survived', axis = 1)

#Step 7: Split train test data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size= 0.2, random_state=42)
#random_state is simply a seed for the random number generator. It ensures that the "random" choices are reproducible.

#Step 8: Train the decision tree
model = DecisionTreeClassifier(random_state= 42) #controls models internal random choices
model.fit(X_train, y_train)

#Step 9: make predictions
predictions = model.predict(X_test)
print(predictions)

#Step 10: Evaluate the model
accuracy = accuracy_score(y_test, predictions)
print('Accuracy: ',accuracy)

#Step 11: visualize the tree
plt.figure(figsize = (15,8)) #width as 15inches and height as 8 inches

plot_tree(
    model,
    feature_names= X.columns,
    class_names = ['No', 'Yes'], #The Decision Tree predicts classes as numbers. This is mapped to No and yes
    filled = True #Color each node based on the predicted class and how pure it is. Suppose a node contains:value = [100, 0] 100 died, 0 survived. The node is very pure, so the color is dark blue.
    #value = [60, 40] It's still predicting "No", but the classes are more mixed. So it becomes a lighter blue.
)
plt.show()
    #             Sex <= 0.5
    #            /           \
    #       True             False
    #     (Male)           (Female)
    #       |                 |
    #  Age <= 10          Fare <= 30
    #   /     \            /      \
    # Yes     No         Yes      No

#Step 12: Predict fro a new passenger
new_passenger = [[3,0,22,1,0,7.25,0]]
prediction = model.predict(new_passenger)
print(prediction)