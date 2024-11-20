FILENAME = "data.csv"
DATADIR = "../lec1/"

import pandas
df = pandas.read_csv(DATADIR + FILENAME)
print (df)
