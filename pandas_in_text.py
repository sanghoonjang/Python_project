
import pandas as pd


# Set A DataFrame
var = [1,2,3,4,5]

df = pd.DataFrame(var)
df """   0
      0  1
      1  2
      2  3
      3  4
      4  5 
   """

# Change column's name
df.columns = ['var']


# Adding column
df["num"] = 1


# Delete a column
del df["num"]


# Select data
df[0] # Only select data by Column(s)'s name
df.loc[0:3,0] # Select data by Low(s)'s and Column(s)'s name
df.iloc[0:3] # By index number select data


# Solting
solted = df.solt_values(['column_name'], ascending=False)
df['column_name'].max()


# Groupby
group = df.groupby('column_name')
df = group.sum()


# Reading from CSV
Location = '/Users/jangsanghoon/Desktop/src_scraping/ch4/iris.csv'
df = pd.read_csv(Location, [header=None,names=['a','b']] ) # The arguments in [] is option.
# The header argument is to make header [0,1,2,3] numbers, the original header moves to next LOW.
# The names argument is to add header, the original header moves to next LOW.


# Export to CSV
df.to_csv('file_name.csv',index=False)


# To JSON From JSON
df.to_json('file_name.json')
df2 = pd.read_json('file_name.json')

# Zip
i = ['a','b']
j = [1,2]

li = list(zip(i,j)) # Output of zip is Tuple
li # [('a', 1), ('b', 2)]

