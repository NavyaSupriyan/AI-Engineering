# Pandas is an open source python library that provides easy to use data structures and data analysis tools. 
# It's widely used for data mainupulation, data analysis and data cleaning task in the field of data science and machine learning.
# Built on top of NumPy

import pandas as pd
import numpy as np

##Panda series: It's like a column in a table; a 1D array holding data of a type

country = ['Germany', 'italy', 'India', 'Japan']
print(pd.Series(country))

# 0    Germany
# 1      italy
# 2      India
# 3      Japan
# dtype: str

marks = [71, 82, 92, 94, 77]
subject = ['english', 'physics', 'chem', 'math', 'cs']
print(pd.Series(marks, index = subject, name = 'Rohan Marks'))

# english    71
# physics    82
# chem       92
# math       94
# cs         77
# Name: Rohan Marks, dtype: int64

## Series from dict

marks = { 'english' : 77, 'physics':67, 'chemistry':43, 'maths':54, 'IT':98}
marks_series = pd.Series(marks)

#size
print(marks_series.size)

#data type
print(marks_series.dtype)

#is_unique: If every single value in series is unique then returns True. So here it returns True if all subjects have diff score
print(marks_series.is_unique)

#index: returns the identifier assigned to each value instead of the value itself
print(marks_series.index)
# Index(['english', 'physics', 'chemistry', 'maths', 'IT'], dtype='str')

#values
print(marks_series.values)
#[77 67 43 54 98]

## Series Indexing

import pandas as pd
x = pd.Series([34,56,78,34,23,32,56,76,57,83])
print(x[0]) #34

print(x[2:5]) 
# 2    78
# 3    34
# 4    23
# dtype: int64

#fancy indexing
print(x[[1,4,3,2]])

# 1    56
# 4    23
# 3    34
# 2    78
# dtype: int64

## Editing series

x[0] = 89

marks_series['sst'] = 80 #Adds new index as it does not exist

marks_series[2:4] = [50, 51]

#fancy indexing

marks_series[[0,3,4]] = [0,0,0]
# english       0
# physics      67
# chemistry    50
# maths         0
# IT            0
# sst          91
# dtype: int64

#Arithmetic operators

print(100 - marks_series)
# english      100
# physics       33
# chemistry     50
# maths        100
# IT           100
# sst            9
# dtype: int64


print(x >= 50)

# 0     True
# 1     True
# 2     True
# 3    False
# 4    False
# 5    False
# 6     True
# 7     True
# 8     True
# 9     True
# dtype: bool

# To count for a particular value
print(x[x >= 50].size)


## Data Frame: Any structure that got rows and columns is called a dataframe

students_data = [
    [100,80,10],
    [93,76,7],
    [120,97,14],
    [80,50,2]
]
print(pd.DataFrame(students_data, columns = ['iq', 'marks', 'package']))

#     iq  marks  package
# 0  100     80       10
# 1   93     76        7
# 2  120     97       14
# 3   80     50        2

import pandas as pd
students_dict = {
    'name':['Ankit','Gaurav','Sonalika','Rashmi','Shivani'],
    'iq':[100,90,120,102,98],
    'marks':[80,70,98,89,87],
    'package':[10,7,14,4,20]
}
students = pd.DataFrame(students_dict)
students.set_index('name', inplace = True)
print(students)

#The inplace=True parameter modifies the DataFrame directly in place, meaning it updates the existing students variable rather than creating a new one.
#            iq  marks  package
# name                         
# Ankit     100     80       10
# Gaurav     90     70        7
# Sonalika  120     98       14
# Rashmi    102     89        4
# Shivani    98     87       20

print(students.values)
# array([[100,  80,  10],
#        [ 90,  70,   7],
#        [120,  98,  14],
#        [102,  89,   4],
#        [ 98,  87,  20]])

print(students.sum())
# iq         510
# marks      424
# package     55
# dtype: int64

print(students.sum(axis = 1))
# name
# Ankit       190
# Gaurav      167
# Sonalika    232
# Rashmi      195
# Shivani     205
# dtype: int64

print(students.mean())
# iq         102.0
# marks       84.8
# package     11.0
# dtype: float64

print(students.max())
# iq         120
# marks       98
# package     20
# dtype: int64

print(students.min())
# iq         90
# marks      70
# package     4
# dtype: int64

#standard deviation
print(students.std())
# iq         11.045361
# marks      10.473777
# package     6.244998
# dtype: float64

#variance
print(students.var())
# iq         122.0
# marks      109.7
# package     39.0
# dtype: float64

#Renaming columns
students.rename(columns = {'marks': 'percent', 'package':'lpa'})



movies = pd.read_csv('resources/movies.csv')
print(movies.head(2))

print(movies.shape)
#(1629, 18)

print(movies.dtypes)
# title_x                 str
# imdb_id                 str
# poster_path             str
# wiki_link               str
# title_y                 str
# original_title          str
# is_adult              int64
# year_of_release       int64
# runtime                 str
# genres                  str
# imdb_rating         float64
# imdb_votes            int64
# story                   str
# summary                 str
# tagline                 str
# actors                  str
# wins_nominations        str
# release_date            str
# dtype: object


print(movies.index)
# RangeIndex(start=0, stop=1629, step=1)

print(movies.columns)
# Index(['title_x', 'imdb_id', 'poster_path', 'wiki_link', 'title_y',
#        'original_title', 'is_adult', 'year_of_release', 'runtime', 'genres',
#        'imdb_rating', 'imdb_votes', 'story', 'summary', 'tagline', 'actors',
#        'wins_nominations', 'release_date'],
#       dtype='str')

print(movies.tail(3))

# returns n random rows
print(movies.sample(5))

#.info() focuses on the structure and metadata (data types, missing values, memory usage). This is a printing function so no need to print
movies.info()
# <class 'pandas.DataFrame'>
# RangeIndex: 1629 entries, 0 to 1628
# Data columns (total 18 columns):
#  #   Column            Non-Null Count  Dtype  
# ---  ------            --------------  -----  
#  0   title_x           1629 non-null   str    
#  1   imdb_id           1629 non-null   str    
#  2   poster_path       1526 non-null   str    
#  3   wiki_link         1629 non-null   str    
#  4   title_y           1629 non-null   str    
#  5   original_title    1629 non-null   str    
#  6   is_adult          1629 non-null   int64  
#  7   year_of_release   1629 non-null   int64  
#  8   runtime           1629 non-null   str    
#  9   genres            1629 non-null   str    
#  10  imdb_rating       1629 non-null   float64
#  11  imdb_votes        1629 non-null   int64  
#  12  story             1609 non-null   str    
#  13  summary           1629 non-null   str    
#  14  tagline           557 non-null    str    
#  15  actors            1624 non-null   str    
#  16  wins_nominations  707 non-null    str    
#  17  release_date      1522 non-null   str    
# dtypes: float64(1), int64(3), str(14)
# memory usage: 229.2 KB

#.describe() focuses on the statistical summary of the data values (mean, min, max, distributions)
#This is a data engineering function. It calculates statistics and bundles them into brand new DataFrame hence we need to print
print(movies.describe())
#        is_adult  year_of_release  imdb_rating     imdb_votes
# count    1629.0      1629.000000  1629.000000    1629.000000
# mean        0.0      2010.263966     5.557459    5384.263352
# std         0.0         5.381542     1.567609   14552.103231
# min         0.0      2001.000000     0.000000       0.000000
# 25%         0.0      2005.000000     4.400000     233.000000
# 50%         0.0      2011.000000     5.600000    1000.000000
# 75%         0.0      2015.000000     6.800000    4287.000000
# max         0.0      2019.000000     9.400000  310481.000000


print(movies.isnull().sum())
# title_x                0
# imdb_id                0
# poster_path          103
# wiki_link              0
# title_y                0
# original_title         0
# is_adult               0
# year_of_release        0
# runtime                0
# genres                 0
# imdb_rating            0
# imdb_votes             0
# story                 20
# summary                0
# tagline             1072
# actors                 5
# wins_nominations     922
# release_date         107
# dtype: int64

# Tells you exact no. of duplicate rows in the dataset
print(movies.duplicated().sum())

#In Pandas, a DataFrame is the entire table (2D), while a Series is a single row or column (1D) extracted from that table.

print(type(movies['title_x']))
#<class 'pandas.Series'>

#slicing multiple cols
print(movies[['title_x','year_of_release','actors']])

#Selecting rows from a dataframe

#iloc searches using index positions

#single row
print(movies.iloc[0])

#multiple rows
print(movies.iloc[5:16:2]) #starting from 5 to 15 with step as 2

#fancy indexing
print(movies.iloc[[0,4,5]])

#loc searches using ndex labels
print(students.loc['Gaurav'])

#slicing
print(students.loc['Ankit':'Sonalika'])

#fancy indexing
print(students.loc[['Ankit','Shivani','Rashmi']])


print(students.iloc[:4])

movies = pd.read_csv('resources/movies.csv')
#selcting both rows and columns
print(movies.iloc[0:4, 0:4])

#                                 title_x  ...                                          wiki_link
# 0              Uri: The Surgical Strike  ...  https://en.wikipedia.org/wiki/Uri:_The_Surgica...
# 1                         Battalion 609  ...        https://en.wikipedia.org/wiki/Battalion_609
# 2  The Accidental Prime Minister (film)  ...  https://en.wikipedia.org/wiki/The_Accidental_P...
# 3                       Why Cheat India  ...      https://en.wikipedia.org/wiki/Why_Cheat_India


#Filtering a dataframe

import pandas as pd
ipl = pd.read_csv('resources/IPL_Matches_Result_2008_2022.csv')

#Find all winner teams
print(ipl[ipl['MatchNumber'] == 'Final'][['Season','WinningTeam']])

#How many super over finishes are done
print(ipl[['SuperOver'] == 'Y'].shape)

#How many matches has csk won in kolkata
print(ipl[(ipl['City'] == 'Kolkata') & (ipl['WinningTeam'] == 'Chennai Super Kings')].shape[0])

#Percentage of toss winner being the winner of match
print((ipl[ipl['TossWinner'] == ipl['WinningTeam']].shape[0]/ipl.shape[0])*100)

#movies with rating higher that 8 and votes > 10000
print(movies[(movies['Rating'] > 8) & (movies['Votes'] > 10000)].shape[0])

#Action movies with rating higher than 7.5
A = movies['genre'].str.split('|').apply(lambda x:'Action' in x)
B= movies['Rating'] >7.5
print(movies[A&B].shape[0])

#Write a function to print track record of 2 teams against each other
def team_track_record(team1, team2, ipl):
    matches = ipl[((ipl['Team1'] == team1) & (ipl['Team2'] == team2)) | ((ipl['Team1'] == team2) &(ipl['Team2'] == team1))]
    team1_wins = (matches['WinningTeam'] == team1).sum()
    team2_wins = (matches['WinningTeam'] == team2).sum()
    total_matches = len(matches)

    return{
        f"{team1} wins": team1_wins,
        f"{team2} wins": team2_wins,
        "Total Matches": total_matches
    }

team1 = "Mumbai Indians"
team2 = "Chennai Super Kings"
track_record = team_track_record(team1, team2, ipl)
print(track_record)

#Adding new columns
movies['Country'] = 'India'

#Dropping rows with missing values
movies.dropna(inplace = True)

#Getting elad actors
movies['lead actors'] = movies['actors'].str.split('|').apply(lambda x:x[0])

#By default, pandas often stores integers as int64, which allocates 64 bits of memory per number.
#Changing it to int32 cuts the memory usage for that column exactly in half.
ipl['ID'] = ipl['ID'].astype('int32')

#The Season column contains text or years that repeat many times (e.g., "2023", "2024", "2025"). 
# Storing text repeatedly as strings wastes a massive amount of memory.
# Changing it to category tells pandas to create a hidden lookup table of unique seasons.E
# very row now stores a tiny integer code pointing to that table instead of the full text string.
ipl['Season'] = ipl['Season'].astype('category')



list = [10, 20, 30, 40, 50]
labels = ['A', 'B', 'C', 'D', 'E']
arr = np.array([10,20,30,40,50])
dic = {'A':10,'B':20,'C':30, 'D':40, "E":50}

pd.Series(list)
# 0    10
# 1    20
# 2    30
# 3    40
# 4    50
# dtype: int64

pd.Series(data = list, index = labels) #pd.Series(list, labels)
# A    10
# B    20
# C    30
# D    40
# E    50
# dtype: int64

pd.Series(arr, labels) #same

#Arithmetic operations on series
ser1 = pd.Series(data, labels)
ser2 = pd.series(dic)

ser1+ser2
# A     20
# B     40
# C     60
# D     80
# E    100
# dtype: int64

#DataFrame: A two-dimensional labeled data structure, similar to a spreadsheet or SQL table, with columns of potentially different data types.

dict1 = {
    "name":['harry','rohan','ajay','shubh'],
    "marks":[92,54,65,19],
    "city":['rampur','kolkata','barielly','delhi']
}
df = pd.DataFrame(dict1)
print(df)
#     name  marks      city
# 0  harry     92    rampur
# 1  rohan     54   kolkata
# 2  ajay     65  barielly
# 3  shubh     19     delhi

df.to_csv('friends.csv')

df.index = [1,2,3,4]
#     name  marks      city
# 1  harry     92    rampur
# 2  rohan     54   kolkata
# 3  ajay     65  barielly
# 4  shubh     19     delhi


#This uses NumPy to generate a grid of random float numbers between 0.0 and 1.0. 335 rows and 5 columns with index as 0 to 334
newdf=pd.DataFrame(np.random.rand(335,5),index=np.arange(335))

print(type(newdf))
#<class 'pandas.DataFrame'>


#Data Alignement
#Whenever pandas tries to perform math between a valid number and a missing value, the result is always NaN.
series1 = pd.Series([10, 20, 30], index=['A', 'B', 'C'])
series2 = pd.Series([100, 200, 300], index=['B', 'C', 'D'])

# Performing addition on two Series with different indices
result = series1 + series2
print(result)
# A      NaN
# B    120.0
# C    230.0
# D      NaN
# dtype: float64


#Missing data handling
data = {
    'A': [1, 2, None, 4],
    'B': [5, None, 7, 8],
}
df = pd.DataFrame(data)

print(df.isnull())

#        A      B
# 0  False  False
# 1  False   True
# 2   True  False
# 3  False  False

# Filling missing values with a specific value
filled_df = df.fillna(0)
print(filled_df)
#      A    B
# 0  1.0  5.0
# 1  2.0  0.0
# 2  0.0  7.0
# 3  4.0  8.0

# Dropping rows with missing values
dropped_df = df.dropna()
print(dropped_df)
#      A    B
# 0  1.0  5.0
# 3  4.0  8.0

#sort index 0,1...
df.sort_index(axis=0,ascending=False)

#sort by col names
df.sort_index(axis=1,ascending=False)

newdf.loc[0,0]=654 #1st row 1st col value as 654

newdf.loc[0,'A']=65445 #No column as 'A' so adds that and only for 1st row puts this value and for rest NaN

#Drop column
newdf.drop(0, axis = 1) #returns a new dataframe with 1st col drop

#Drop row
newdf.drop(0, axis = 0) #returns a new dataframe with 1st row drop

newdf = newdf.drop(0, axis = 0)

#values of 2nd and 3rd row and column: sepal length and petal length
df.loc[[1,2],['sepal length','petal length']]

#values of 2nd and 3rd row and all columns
df.loc[[1,2],:]

#values of all rows and column: sepal length and petal length
df.loc[:,['sepal length','petal length']]
