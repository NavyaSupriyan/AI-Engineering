import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('resources/titanic.csv')
print(df.head())
print(df.info())

#Line Plot
plt.plot(df['Age'].head(20))
plt.title('Age of first 20 passengers')
plt.xlabel('Index of passenger')
plt.ylabel('Age of passenger')
plt.show()

#Histogram
#df["Age"].dropna(): This strips out any missing or empty (NaN) values from the Age column before plotting.
#bins=20: This divides the entire range of ages (from your youngest to oldest person) into 20 equal intervals.
plt.hist(df['Age'].dropna(), bins = 20)
plt.title('Age Distribution')
plt.xlabel('Age')
plt.ylabel('Number of passengers')
plt.show()

#Bar chart
#value_counts: It loops through the Pclass column, identifies every unique value, and counts how many times each value appears.
df['Pclass'].value_counts().plot(kind = 'bar') #internally it does: plt.bar(x_values, y_values)
plt.title('Passenger by class')
plt.xlabel('Passenger Class')
plt.ylabel('Count')
plt.show()



#plt.show() is a blocking function by default.When Python hits plt.show(), it completely pauses your script's execution to 
# keep the interactive graph window open so you can zoom, pan, or save the image. The script will only finish running and 
# exit the terminal after you manually close the graph window.

#Scatter plot

plt.scatter(df['Age'], df['Fare'])
plt.title('Age vs Fare')
plt.xlabel('Age')
plt.ylabel('Fare')
plt.show()

#What Does One Point Represent? -> Exactly one individual passenger from your dataset.
#What Relationships Can Scatter Plots Show? ->Scatter plots are specifically designed to reveal correlations (patterns or connections) between two numeric variables.

avg_fare = df.groupby('Pclass')['Fare'].mean()
avg_fare.plot(kind = 'bar')

plt.title('Avg Fare by passenger class')
plt.xlabel('Passenger Class')
plt.ylabel('Avg Fare')
plt.show()