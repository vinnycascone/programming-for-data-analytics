import re #importing regex

regex = ".*" #.* matches zero or more of any character (except newlines). 
#In this case, it effectively matches every line of the file since all lines fit this pattern.
filename = "./quiz.txt" #Opens the file quiz.txt in read mode, ensuring proper resource management with with.

# Looping through the lines
with open(filename) as quizFile: # Opens the file quiz.txt in read mode, ensuring proper resource management with with.
    for line in quizFile : # Iterates through each line of the file.
        searchResult = re.search(regex, line) 
        #Searches the line for the regex pattern (.*). 
        # Since the pattern matches all lines, searchResult will always be truthy unless the line is empty.
        if (searchResult) :
            matchingLine = line
            print(matchingLine, end="")
            #If a match is found, the line is assigned to matchingLine and printed without adding an extra newline 
            #(end="" prevents a double newline since line already contains one).

# The code essentially prints the entire contents of the file quiz.txt to the console because the regex pattern (.*) matches all lines.
