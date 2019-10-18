#!Python3
"""
word tokenization is the process of splitting a large sample of
text into words.
clean_and_count_tokens.py - this program clean a file and count the
words in it. ou can run it by using the following command in the
terminal:

./clean_and_count_tokens.py<input_file><output_file>
"""

import re
import sys

inFile = sys.argv[1] #input
outFile = sys.argv[2]   #output

with open(inFile, "r", encoding='UTF-8') as f:
    txt = f.read()

#Remove the tag  <...></something>
x = re.sub("<(\/)?\w+(\/)?>", "" , txt)
x = re.sub("<\w+\s.{0,300}\">", "", x)

#remove numbers and symbols
x = re.sub("\d|[=://@!#$%^&*(+{}:\"?>;.,)\[\]\|-]", "", x)
x = re.sub("_", " ", x)
x = re.sub("(\'\')", "", x)
x = x.lower()
x = re.sub("\s+", " ", x)

#convert the string to an array
x = x.split(" ")

# delete all the empty item
for word in x:
    if word == '':
        x.remove(word)

#create a new dictionary
wordDict = {}

#count the word and make a dictionary

for word in x:
    if word not in wordDict:
        wordDict[word] = 1
    elif word in wordDict:
        wordDict[word] = wordDict[word] + 1



#open a new File
newFile = open(outFile, "w", encoding ='UTF-8')

#print wordDict and store it as a string called result_txt
result_txt = ""

for word in wordDict:
    result_txt = result_txt + str(wordDict.get(word)) + " " + \
                 word + " " + "\n"

#write the result into a new txt
newFile.write(result_txt)
newFile.close()


"""
reference
1. How to convert int to string https://www.techwalla.com/
articles/how-to-convert-int-to-string-in-python
2. How to use inFile and outFile https://stackoverflow.com/questions/20157824/
how-to-take-input-file-from-terminal-for-python-script
3. Justin's helped me
"""