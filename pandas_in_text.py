
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


# Reading from CSV
Location = '/Users/jangsanghoon/Desktop/src_scraping/ch4/iris.csv'
df = pd.read_csv(Location, [header=None,names=['a','b']] ) # The arguments in [] is option.
# The header argument is to make header [0,1,2,3] numbers, the original header moves to next LOW.
# The names argument is to add header, the original header moves to next LOW.


# Export to CSV
df.to_csv('fail_name',index=False)
