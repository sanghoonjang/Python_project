
import pandas as pd


# Set A DataFrame
var = [1,2,3,4,5]

df = pd.DataFrame(var)
df # 

# Change column's name
df.columns = "var"

# Adding column
df["num"] = 1

# Delete a column
del df["num"]
