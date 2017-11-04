
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


# Export to CSV
df.to_csv('fail_name',index=False)
