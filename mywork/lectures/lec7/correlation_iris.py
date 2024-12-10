import pandas as pd

# Load the dataset
dataurl = "https://gist.githubusercontent.com/netj/8836201/raw/6f9306ad21398ea43cba4f7d537619d0e07d5ae3/iris.csv"
irisdf = pd.read_csv(dataurl)

# Exclude non-numeric columns
numeric_columns = irisdf.select_dtypes(include=['float', 'int'])

# Compute correlation matrix
correlation_matrix = numeric_columns.corr()

# Print the correlation matrix
print(correlation_matrix)
