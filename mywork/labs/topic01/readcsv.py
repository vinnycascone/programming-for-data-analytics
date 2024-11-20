import csv #importing the csv module
FILENAME= "data.csv" #specifying the name of the file
DATADIR = "../topic01/" # specifying the name of the directory we is located
with open (DATADIR + FILENAME, "rt") as fp: #opening the file in a read text mode with its full path
 #with ensures that the file is properly closed after
 reader = csv.DictReaderreader(fp, delimiter=",", quoting=csv.QUOTE_NONNUMERIC) #processing the file treating each row as a string
 #reading it as a dictionary object
 linecount = 0 # tracking the number of the rows processed, starting from 0
 total = 0 # accumulate the sum of values in the second column
 for line in reader : # Check if this is the first row (header)
   if not linecount : # first row
     pass
   else: # all subsequent rows 
    total+= int(line[1]) # Add the value in the second column
    linecount += 1 # Increment linecount for every row
#Header Row: If linecount == 0 (first row), do nothing (pass).
#Data Rows: Convert the value in the second column (line[1]) to an integer and add it to total.
#linecount is incremented for every row (header + data)

print(f"average is {total/(linecount-1)}")
# The average is calculated as:
#total: The sum of the second-column values.
#(linecount - 1): The number of data rows (excluding the header row).
# Prints the result in a formatted string.


