
import csv

# When use Pandas
import pandas as pd

filename = "test.csv"
df = pd.read_csv(filename, index_col=0)


# When use csv module
import csv codecs

filename = "test.csv"
df = codecs.open(filename, "r", "shift_jis")

reader = csv.reader(df, delimiter=",", quotechar='"')
